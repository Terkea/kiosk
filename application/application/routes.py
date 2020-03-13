from flask import Flask, render_template, request, flash, redirect

from application import app
from application.database import db_session
from application.forms import registerForm

from application.models.User import User
from application.models.Event import Event
from application.models.Booking import Booking
from application.models.Category import Category



# @app.before_request
# def require_login():
#     """
#     all routes are protected except the ones from  allowed_routes
#     if a session is initialized with a valid token the access is granted
#     """
#     allowed_routes = ['login', 'register']
#     if request.endpoint not in allowed_routes and 'token' not in session:
#         return redirect(url_for('login'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    pass

@app.route('/register/', methods=['GET', 'POST'])
def register():
    form = registerForm()
    if form.validate_on_submit():
        _user = User(
            first_name=str(form.first_name.data),
            last_name=str(form.last_name.data),
            email=str(form.email.data),
            mobile= str(form.mobile.data),
            address= str(form.address.data),
            city= str(form.city.data),
            postcode= str(form.postcode.data),
            course= str(form.course.data),
            password=str(form.password.data),
            is_admin=False,
            is_guest=False
        )
        db_session.add(_user)
        try:
            db_session.commit()
        except:
            flash('Email address already taken')
            return redirect(url_for('register'))

    return render_template('register.html', form=form)

@app.route('/logout/')
def logout():
    """
    delete the session token
    """
    del session['token']
    return redirect(url_for('login'))


@app.route('/')
def hello_world():
    return render_template('index.html')
