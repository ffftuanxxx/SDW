from flask import render_template, request, redirect, url_for, flash
from new_control.assign import create_assignq,session
from app_pre import db,app
from co_ import AssignQ, session, Course

@app.route('/create_assignment', methods=['GET', 'POST'])
def create_assignq_route():
    if request.method == 'POST':
        aid = request.form.get('aid')
        cname = request.form.get('cname')
        print(f"Received cname: {cname}")
        qtext = request.form.get('qtext')
        category = request.form.get('category')
        picturename = request.form.get('picturename')
        try:
                #cname, qtext, category, picturename, session
            new_question=create_assignq(cname, qtext, category, picturename, aid, session)
                #new_question = AssignQ(qtext=qtext, category=category, picturename=picturename, course=course)
                #db.session.add(new_question)
            print(f"New question created with qid: {new_question}")
            flash(f'新问题创建成功, qid: {new_question}', 'success')
        except Exception as e:
            print(e)
            flash(str(e), 'error')
    return render_template('create_assignment.html')