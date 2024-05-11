from flask import render_template, request, redirect, url_for, flash
from new_control.Course import create_course
from app_pre import db,app

@app.route('/course', methods=['GET', 'POST'])
def create_course_route():
    if request.method == 'POST':
        cname = request.form.get('cname')
        c_descri = request.form.get('c_descri')
        c_cate = request.form.get('c_cate')
        try:
            cnumber = create_course(cname, c_descri,c_cate, db.session)
            flash(f'New course created with number: {cnumber}', 'success')
            return redirect(url_for('courses'))
        except Exception as e:
            flash(str(e), 'error')
    return render_template('course.html')