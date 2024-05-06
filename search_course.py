from flask import render_template, request, redirect, url_for, flash
from new_control.Course import get_course_name,get_course_num
from app_pre import db,app
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