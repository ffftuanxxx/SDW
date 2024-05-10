from flask import render_template, request, redirect, url_for, flash, session
from app_pre import db, app

@app.route('/student')
def student():
    return render_template('student.html')
@app.route('/teacher')
def teacher():
    return render_template('teacher.html')
@app.route('/adm')
def adm():
    return render_template('adm.html')