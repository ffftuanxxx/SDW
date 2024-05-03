from flask import render_template, request, redirect, url_for, flash
from new_control.register import delete_user
from app_pre import db,app
import register_action
<<<<<<< HEAD
import addcourse_action
=======
import request_action
>>>>>>> 2ced5845fb35431fdfbc0d20f8beead457219b38


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uclass = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'User(id={self.id}, uclass={self.uclass}, email={self.email})'

with app.app_context():
    db.create_all()



@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        user = User.query.filter_by(email=email, password=password).first()
        if user:
            flash('Login successful!', 'success')
            # Add logic for logged-in user
            return redirect(url_for('login'))
        else:
            flash('Invalid email or password', 'error')
    return render_template('login.html')


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



