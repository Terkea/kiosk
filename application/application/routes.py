from flask import Flask, render_template

from application import app
from application.database import db_session
from application.models.User import User
from application.models.Event import Event
from application.models.Booking import Booking
from application.models.Category import Category

@app.route('/')
def hello_world():
    print(User.query.all())
    return render_template('index.html', content="test")
