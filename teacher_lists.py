from flask import render_template, request, redirect, url_for, flash
from app_pre import db, app
from new_control.Course import Course1

@app.route('/courses')
def courses():
    all_courses = Course1.get_all_courses(session=db.session)
    return render_template('courses.html', courses=all_courses)

