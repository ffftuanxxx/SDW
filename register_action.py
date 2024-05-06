from flask import render_template, request, redirect, url_for, flash, session
from new_control.register import create_user
from app_pre import db, app
import random
from s import sendemail

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        session['email'] = email  # 将邮箱存储在会话中

        # 生成5位随机数作为验证码
        random_num = random.randint(10000, 99999)
        session['verification_code'] = random_num  # 将验证码存储在会话中

        # 调用发送邮件函数,发送验证码到用户邮箱
        sendemail(email, random_num)

        return redirect(url_for('verify_code'))

    return render_template('register.html')

@app.route('/verify_code', methods=['GET', 'POST'])
def verify_code():
    if request.method == 'POST':
        uclass = request.form.get('uclass')
        password = request.form.get('password')
        verification_code = request.form.get('verification_code')

        # 检查密码是否符合要求
        has_uppercase = any(char.isupper() for char in password)
        has_lowercase = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)

        if not (has_uppercase and has_lowercase and has_digit):
            error_message = 'Password must contain at least one uppercase letter, one lowercase letter, and one number.'
            return render_template('verify_code.html', error_message=error_message)

        # 检查用户输入的验证码是否正确
        if str(verification_code) != str(session.get('verification_code')):
            error_message = 'Invalid verification code'
            return render_template('verify_code.html', error_message=error_message)

        try:
            create_user(int(uclass), session.get('email'), password, db.session)
            flash('Registration successful!', 'success')
            return redirect(url_for('register'))
        except Exception as e:
            flash(str(e), 'error')

    return render_template('verify_code.html')