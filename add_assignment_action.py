from flask import render_template, request, redirect, url_for, flash
from new_control.assign import create_assignq
from app_pre import db,app
from co_ import AssignQ, session, Course

@app.route('/create_assignq', methods=['GET', 'POST'])
def create_assignq_route():
    if request.method == 'POST':
        cname = request.form.get('cname')
        print(f"Received cname: {cname}")
        qtext = request.form.get('qtext')
        category = request.form.get('category')
        picturename = request.form.get('picturename')
        try:
            db = app.extensions['sqlalchemy'].db
            with db.session.begin():
                course = db.session.query(Course).filter_by(CName=cname).first()
                print(f"Found course: {course}")
                if not course:
                    flash(f"错误: 课程名称 '{cname}' 不存在!", 'error')
                    return render_template('create_assignq.html')

                new_question = AssignQ(qtext=qtext, category=category, picturename=picturename, course=course)
                db.session.add(new_question)
            print(f"New question created with qid: {new_question.qid}")
            flash(f'新问题创建成功, qid: {new_question.qid}', 'success')
        except Exception as e:
            print(e)
            flash(str(e), 'error')
    return render_template('create_assignq.html')