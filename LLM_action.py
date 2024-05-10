from flask import render_template, request, redirect, url_for, flash
from new_control.assign import get_assignq
from app_pre import db,app
from new_control.LLM import create_llm,delete_llm,update_llm,get_llm,get_all_llms


@app.route('/submit_llm', methods=['GET', 'POST'])
def submit_llm():
    print(1)
    if request.method == 'POST':
        homeproblem = request.form.get('homeproblem')
        usedanswer = request.form.get('usedanswer')
        answerimage = request.form.get('answerimage')
        llmscore = request.form.get('llmscore')
        comments = request.form.get('comments')
        qid = request.args.get('qid')  # 获取qid参数
        CNumber=get_assignq(qid, db.session)
        try:
            CNumber=CNumber.CNumber
        except Exception as e:
            CNumber=0
        print(1)

        try:
            llmscore = float(llmscore)  # 确认 llmscore 是浮点数
            llm_id = create_llm(homeproblem=homeproblem, usedanswer=usedanswer, answerimage=answerimage,
                                llmscore=llmscore, comments=comments, CNumber=CNumber, qid=qid, session=db.session)
            flash('LLM记录创建成功！', 'success')
            return redirect(url_for('llms', qid=qid))  # 重定向到/llms/qid页面
        except ValueError:
            flash('LLM分数输入无效，请输入一个有效的数字。', 'error')
            print(e)
        except Exception as e:
            flash(str(e), 'error')
            print(e)

    qid = request.args.get('qid')  # 获取qid参数
    return render_template('submit_llm.html', qid=qid)
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
    if request.method == 'POST':
        llmscore = request.form.get('llmscore')
        comments = request.form.get('comments')

        try:
            llmscore = float(llmscore)  # 确认 llmscore 是浮点数
            if llmscore < 0 or llmscore > 5:
                flash('LLM score must be between 0 and 54.', 'error')
                return render_template('update_llm.html', llm=llm)

            update_llm(llm_id=llm_id, llmscore=llmscore, comments=comments, session=db.session)
            flash('LLM record updated successfully!', 'success')
            return redirect(url_for('update_llm_view', llm_id=llm_id))
        except ValueError:
            flash('Invalid input for LLM score. Please enter a valid number.', 'error')
        except Exception as e:
            flash(str(e), 'error')

    return render_template('update_llm.html', llm=llm)


@app.route('/llms')
def llms():
    all_llms = get_all_llms(session=db.session)  # 这需要你实现一个 get_all_llms 函数来获取所有记录
    return render_template('llm.html', llms=all_llms)


@app.route('/delete_llm/<int:llm_id>', methods=['POST'])
def delete_llm_view(llm_id):
    delete_llm(llm_id=llm_id, session=db.session)
    flash('LLM record deleted successfully!', 'success')
    return redirect(url_for('llms'))

@app.route('/llms/<int:qid>')
def llmsqid(qid):
    all_llms = get_all_llms(db.session)  # 获取所有的llms记录
    filtered_llms = [llm for llm in all_llms if llm.qid == qid]  # 筛选与qid相关的llms记录
    return render_template('llms.html', llms=filtered_llms)



