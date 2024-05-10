from flask import render_template, request, redirect, url_for, flash
from app_pre import db, app
from new_control.Course import create_course, get_course, update_course, delete_course, get_all_courses

# @app.route('/courses')
# def courses():
#     all_courses = get_all_courses(session=db.session)
#     return render_template('courses.html', courses=all_courses)

@app.route('/create_course', methods=['GET', 'POST'])
def create_course_view():
    if request.method == 'POST':
        help_id = request.form.get('help_id')
        cname = request.form.get('cname')
        qid = request.form.get('qid')
        create_course(help_id=help_id, cname=cname, qid=qid, session=db.session)
        flash('Course created successfully!', 'success')
        return redirect(url_for('courses'))
    return render_template('create_course.html')

@app.route('/update_course/<int:cnumber>', methods=['GET', 'POST'])
def update_course_view(cnumber):
    course = get_course(cnumber=cnumber, session=db.session)
    if request.method == 'POST':
        help_id = request.form.get('help_id')
        cname = request.form.get('cname')
        qid = request.form.get('qid')
        update_course(cnumber=cnumber, help_id=help_id, cname=cname, qid=qid, session=db.session)
        flash('Course updated successfully!', 'success')
        return redirect(url_for('courses'))
    return render_template('update_course.html', course=course)

@app.route('/delete_course/<int:cnumber>', methods=['POST'])
def delete_course_view(cnumber):
    delete_course(cnumber=cnumber, session=db.session)
    flash('Course deleted successfully!', 'success')
    return redirect(url_for('courses'))
