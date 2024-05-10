from flask import render_template, request, redirect, url_for, flash
from new_control.register import delete_user,is_password_correct
from app_pre import db,app
import register_action
import addcourse_action
import request_action
import search_course
import add_assignment_action
import LLM_action
from flask import session
import stu_tea_adm

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     uclass = db.Column(db.Integer, nullable=False)
#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), nullable=False)
#
#     def __repr__(self):
#         return f'User(id={self.id}, uclass={self.uclass}, email={self.email})'
#
# with app.app_context():
#     db.create_all()

def get_user_class():
    return session.get('uclass')
def set_user_class(user_class):
    session['uclass'] = user_class

def is_student():
    return get_user_class() == 0

def is_teacher():
    return get_user_class() == 1

def is_adm():
    return get_user_class() == 2

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user,uclass=is_password_correct(email,password,db.session)
        set_user_class(uclass)
        if user:
            flash('Login successful!', 'success')
            print("login",uclass)
            if is_student():
                return redirect(url_for('student'))
            elif is_teacher():
                return redirect(url_for('teacher'))
            elif is_adm():
                return redirect(url_for('adm'))
            # Add logic for logged-in user
            return redirect(url_for('login'))
        else:
            flash('Invalid email or password', 'error')
    return render_template('index.html')


@app.route('/delete', methods=['GET', 'POST'])
def deleteacount():
    if request.method == 'POST':
        email = request.form.get('email')
        print(email)
        try:
            delete_user(email,db.session)
            flash('delete successful!', 'success')
            return redirect(url_for('register'))
        except Exception as e:
            flash(str(e), 'error')
    return render_template('delete.html')



