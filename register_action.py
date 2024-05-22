from flask import render_template, request, redirect, url_for, flash, session
from new_control.register import Register123
from app_pre import db, app
import random

from s import sendemail
from co_ import User
def set_user_class(user_class,user_email):
    session['uclass'] = user_class
    session['emial'] = user_email
def user_exists(email):
    # 这里的代码需要根据你的数据库访问方式来写
    # 假设使用 SQLAlchemy
    user = db.session.query(User).filter_by(email=email).first()
    if user:
        return True
    return False

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        session['email'] = email  # 将邮箱存储在会话中

        if user_exists(email):
            return render_template('register.html', error_message='此邮箱已注册，无法再次注册。')

        # 生成5位随机数作为验证码
        random_num = random.randint(10000, 99999)
        session['verification_code'] = random_num  # 将验证码存储在会话中

        email_suffix = email.split('@')[-1]

        if email_suffix != 'uic.edu.cn' and email_suffix != 'mail.uic.edu.cn':
            error_message = '只有UIC的教师和学生可以注册。'
            return render_template('register.html', error_message=error_message)

        # 调用发送邮件函数,发送验证码到用户邮箱
        sendemail(email, random_num)

        return redirect(url_for('verify_code'))

    return render_template('register.html')

@app.route('/verify_code', methods=['GET', 'POST'])
def verify_code():
    if request.method == 'POST':
        email = session.get('email')
        password = request.form.get('password')
        verification_code = request.form.get('verification_code')
        confirm_password = request.form.get('confirm_password')
        # 检查密码是否符合要求
        has_uppercase = any(char.isupper() for char in password)
        has_lowercase = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)

        if not (has_uppercase and has_lowercase and has_digit):
            error_message = 'The password must contain at least one uppercase letter, one lowercase letter, and one number.'
            return render_template('verify_code.html', error_message=error_message)

        if (password != confirm_password):
            error_message = "The two passwords do not match. Please re-enter them."
            return render_template('verify_code.html', error_message=error_message)


        # 检查用户输入的验证码是否正确
        if str(verification_code) != str(session.get('verification_code')):
            error_message = 'Invalid verification code.'
            return render_template('verify_code.html', error_message=error_message)

        # 根据邮箱后缀判断用户类别
        email_suffix = email.split('@')[-1]
        uclass = 0 if email_suffix == 'mail.uic.edu.cn' else 1

        try:
            Register123.create_user(uclass, email, password, db.session)
            flash('registered successfully', 'success')
            set_user_class(uclass,email)
            #print(111)
            return redirect(url_for('back'))
        except Exception as e:
            flash(str(e), 'error')

    return render_template('verify_code.html')