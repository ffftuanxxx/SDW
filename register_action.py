from flask import render_template, request, redirect, url_for, flash
from new_control.register import create_user
from app_pre import db,app

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uclass = request.form.get('uclass')
        email = request.form.get('email')
        password = request.form.get('password')
        # print(uclass,email,password)
        try:
            create_user(int(uclass), email, password, db.session)
            flash('Registration successful!', 'success')
            return redirect(url_for('register'))
        except Exception as e:
            flash(str(e), 'error')
    return render_template('register.html')