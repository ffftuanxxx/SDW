from flask import render_template, request, redirect, url_for, flash
from new_control.register import Register123
from app_pre import db,app
import register_action
import addcourse_action
import request_action
import search_course
import add_assignment_action
import LLM_action
import helpT_action
from flask import session
import stu_tea_adm
import teacher_lists
from co_ import User
import alltopic
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


def set_user_class(user_class,user_email):
    session['uclass'] = user_class
    session['email'] = user_email

def is_student():
    return get_user_class() == 0


def is_teacher():
    return get_user_class() == 1


def is_adm():
    return get_user_class() == 2

def get_emial():
    return session.get('email')


def user_exists(email):
    user = db.session.query(User).filter_by(email=email).first()
    if user:
        return True
    return False
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        if not user_exists(email):
            return render_template('register.html', error_message='该用户不存在')
        user,uclass=Register123.is_password_correct(email,password,db.session)
        set_user_class(uclass,email)
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
@app.route('/back', methods=['GET', 'POST'])
def back():

    if is_student():
        return redirect(url_for('student'))
    elif is_teacher():
        return redirect(url_for('teacher'))
    elif is_adm():
        return redirect(url_for('adm'))
    # Add logic for logged-in user
    return redirect(url_for('login'))


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


@app.route('/logout')
def logout():
    # 清除会话中的所有项目
    session.clear()
    # 重定向到登录页面
    return redirect(url_for('login'))



