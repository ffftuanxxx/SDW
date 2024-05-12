from flask import render_template, request, redirect, url_for, flash
from new_control.assign import get_assignq,update_assignq
from app_pre import db,app
from new_control.LLM import create_llm,delete_llm,update_llm,get_llm,get_all_llms



@app.route('/submit_llm', methods=['GET', 'POST'])
def submit_llm():
    qid = request.args.get('qid')  # 从查询参数获取qid
    error_message = None  # 初始化错误信息变量
    if request.method == 'POST':
        homeproblem = request.form.get('homeproblem')
        usedanswer = request.form.get('usedanswer')
        answerimage = request.form.get('answerimage')
        llmscore = request.form.get('llmscore')
        comments = request.form.get('comments')
        assignq = get_assignq(qid, db.session)

        try:
            max_score = assignq.score if assignq else 5  # 默认最大分数为5，如果找不到assignq记录
            CNumber = assignq.CNumber if assignq else 0

            llmscore = float(llmscore)  # 确认 llmscore 是浮点数
            if llmscore < 0 or llmscore > max_score:
                error_message = f'LLM分数必须在0到{max_score}之间。'
            else:
                llm_id = create_llm(homeproblem=homeproblem, usedanswer=usedanswer, answerimage=answerimage,
                                    llmscore=llmscore, comments=comments, CNumber=CNumber, qid=qid, session=db.session)
                flash('LLM记录创建成功！', 'success')
                return redirect(url_for('llmsqid', qid=qid))  # 重定向到/llms/qid页面
        except ValueError:
            error_message = '请输入有效的数字。'
        except Exception as e:
            error_message = str(e)

    return render_template('submit_llm.html', qid=qid, error_message=error_message)




@app.route('/view_llm/<int:llm_id>')
def view_llm(llm_id):
    llm = get_llm(llm_id=llm_id, session=db.session)
    if llm is None:
        flash(f"LLM ID {llm_id} 不存在!", 'error')
        return redirect(url_for('index'))  # 请根据需要修改跳转的默认页面
    return render_template('llm_view.html', llm=llm)


@app.route('/update_llm/<int:llm_id>', methods=['GET', 'POST'])
def update_llm_view(llm_id):
    llm = get_llm(llm_id=llm_id, session=db.session)
    if llm is None:
        flash('LLM record not found.', 'error')
        return redirect(url_for('some_error_page'))  # 如果LLM记录不存在，重定向到错误页面

    assignq = get_assignq(llm.qid, db.session)  # 使用LLM的qid来获取AssignQ记录
    max_score = assignq.score if assignq else 5  # 默认最大分数为5，如果找不到AssignQ记录
    error_message = None

    if request.method == 'POST':
        llmscore = request.form.get('llmscore')
        comments = request.form.get('comments')

        try:
            llmscore = float(llmscore)  # 确认 llmscore 是浮点数
            if llmscore < 0 or llmscore > max_score:
                error_message = f'LLM score must be between 0 and {max_score}.'
                return render_template('update_llm.html', llm=llm, error_message=error_message)

            update_llm(llm_id=llm_id, llmscore=llmscore, comments=comments, session=db.session)
            flash('LLM record updated successfully!', 'success')
            return redirect(url_for('llmsqid', qid=llm.qid))  # 使用 llm.qid 进行重定向
        except ValueError:
            error_message = 'Invalid input for LLM score. Please enter a valid number.'
        except Exception as e:
            error_message = str(e)

    return render_template('update_llm.html', llm=llm, error_message=error_message)



@app.route('/delete_llm/<int:llm_id>', methods=['POST'])
def delete_llm_view(llm_id):
    llm = get_llm(llm_id=llm_id, session=db.session)  # 首先尝试获取LLM记录以确认存在
    if not llm:
        flash('LLM record not found.', 'error')
        return redirect(request.referrer)  # 如果没有找到记录，重定向回之前的页面

    qid = llm.qid  # 假设你从LLM对象中获取qid
    delete_llm(llm_id=llm_id, session=db.session)  # 删除LLM记录
    flash('LLM record deleted successfully!', 'success')
    return redirect(url_for('llmsqid', qid=qid))  # 重定向到/llms/qid页面


@app.route('/llms/<int:qid>')
def llmsqid(qid):
    all_llms = get_all_llms(db.session)  # 获取所有的llms记录
    filtered_llms = [llm for llm in all_llms if llm.qid == qid]  # 筛选与qid相关的llms记录
    return render_template('llms.html', llms=filtered_llms, qid=qid)


@app.route('/submittoass/<int:llm_id>')
def submittoass(llm_id):
    llm=get_llm(llm_id,db.session)
    ass=get_assignq(llm.qid, db.session)
    update_assignq(llm.qid,ass.aid,ass.qtext,ass.category,llm.answerimage,llm.llmscore,db.session)#qid, aid, qtext, category, picturename, score, session
    return render_template('llm_view.html', llm=llm)

