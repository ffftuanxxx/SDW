from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from new_control.register import create_user,delete_user, session


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://llm:2501004@47.109.73.150:3306/llm'

db = SQLAlchemy(app)

