from flask import render_template, request, redirect, url_for, flash
from new_control.register import create_user
from app_pre import db,app
from new_control.LLM import create_llm,delete_llm,update_llm,get_llm,get_all_llms


@app.route('/submit_llm', methods=['GET', 'POST'])
def submit_llm():
    if request.method == 'POST':
        answerid = request.form.get('answerid')
        answerimage = request.form.get('answerimage')
        llmscore = request.form.get('llmscore')
        comments = request.form.get('comments')

        try:
            answerid = int(answerid)
            llmscore = float(llmscore)  # 如果LLM分数是浮点类型

            new_llm_id = create_llm(answerid=answerid, answerimage=answerimage,
                                    llmscore=llmscore, comments=comments, session=db.session)
            flash('LLM record submitted successfully!', 'success')
            return redirect(url_for('submit_llm'))
        except ValueError:
            flash('Invalid input values. Please enter valid values for all fields.', 'error')
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
        answerid = request.form.get('answerid')
        answerimage = request.form.get('answerimage')
        llmscore = request.form.get('llmscore')
        comments = request.form.get('comments')

        try:
            answerid = int(answerid)  # 确认 answerid 是整数
            llmscore = float(llmscore)  # 确认 llmscore 是浮点数
            update_llm(llm_id=llm_id, answerid=answerid, answerimage=answerimage,
                       llmscore=llmscore, comments=comments, session=db.session)
            flash('LLM record updated successfully!', 'success')
            return redirect(url_for('update_llm_view', llm_id=llm_id))
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




