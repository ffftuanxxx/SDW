from flask import render_template, request, redirect, url_for, flash
from new_control.register import create_user
from app_pre import db,app
from new_control.LLM import create_llm,delete_llm,update_llm,get_llm,get_all_llms


@app.route('/submit_llm', methods=['GET', 'POST'])
def submit_llm():
    if request.method == 'POST':
        homeproblem = request.form.get('homeproblem')
        usedanswer = request.form.get('usedanswer')
        answerimage = request.form.get('answerimage')
        llmscore = request.form.get('llmscore')
        comments = request.form.get('comments')
        cL = request.form.get('cL')

        try:
            llmscore = float(llmscore)  # 确认 llmscore 是浮点数
            llm_id = create_llm(homeproblem=homeproblem, usedanswer=usedanswer, answerimage=answerimage,
                                llmscore=llmscore, comments=comments, CNumber=cL,session=db.session)
            flash('LLM record created successfully!', 'success')
            return redirect(url_for('submit_llm'))
        except ValueError:
            flash('Invalid input for LLM score. Please enter a valid number.', 'error')
        except Exception as e:
            flash(str(e), 'error')

    return render_template('submit_llm.html')

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
            if llmscore < 0 or llmscore > 54:
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




