from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from new_control.register import create_user,delete_user, session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://llm:2501004@47.109.73.150:3306/llm'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    uclass = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f'User(id={self.id}, uclass={self.uclass}, email={self.email})'

with app.app_context():
    db.create_all()

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        uclass = request.form.get('uclass')
        email = request.form.get('email')
        password = request.form.get('password')
        print(uclass,email,password)
        try:
            create_user(int(uclass), email, password, db.session)
            flash('Registration successful!', 'success')
            return redirect(url_for('register'))
        except Exception as e:
            flash(str(e), 'error')
    return render_template('register.html')

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



if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)