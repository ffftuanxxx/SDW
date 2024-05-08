from flask import render_template, request, redirect, url_for, flash, session
from new_control.Course import get_course_name,get_course_num
from app_pre import db,app
from co_ import Course, AssignQ
# 其他代码...

@app.route('/searchcourse', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_type = request.form.get('search_type')
        search_info = request.form.get('search_info')

        if search_type == 'course_name':
            courses = get_course_name(search_info, db.session)
        else:
            course = get_course_num(search_info, db.session)
            courses = [course] if course else []

        return render_template('courseresult.html', courses=courses)
    else:
        return render_template('searchcourse.html')

@app.route('/courseresult', methods=['POST'])
def search_results():
    search_type = request.form.get('search_type')
    search_info = request.form.get('search_info')

    if search_type == 'course_name':
        course = get_course_name(search_info, db.session)
        courses = [course] if course else []
    else:
        course = get_course_num(search_info, db.session)
        courses = [course] if course else []

    return render_template('courseresult.html', courses=courses)




@app.route('/course/<course_number>/assignments')
def course_assignments(course_number):
    course = db.session.query(Course).filter_by(CNumber=course_number).first_or_404()
    assignments = db.session.query(AssignQ).filter_by(CNumber=course.CNumber).all()
    return render_template('course_assignments.html', course=course, assignments=assignments)

@app.route('/quesetion_details/<qid>')
def qDetail(qid):
    details = db.session.query(AssignQ).filter_by(qid=qid).first()
    return render_template('quesetion_details.html', details=details)