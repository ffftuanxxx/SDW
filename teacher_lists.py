from flask import render_template, request, redirect, url_for, flash
from app_pre import db, app
from new_control.Course import create_course, get_all_courses

@app.route('/courses')
def courses():
    all_courses = get_all_courses(session=db.session)
    return render_template('courses.html', courses=all_courses)

