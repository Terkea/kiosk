from flask import Flask, render_template, request, flash, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import json
import jwt
import datetime

from application import app
from application.database import db_session
from application.forms import registerForm, loginForm

from application.models.User import User
from application.models.Event import Event
from application.models.Booking import Booking
from application.models.Category import Category

@app.before_request
def require_login():
    """
    all routes are protected except the ones from  allowed_routes
    if a session is initialized with a valid token the access is granted
    """
    allowed_routes = ['login', 'register', 'static']
    if request.endpoint not in allowed_routes and 'token' not in session:
        return redirect(url_for('login'))

@app.route('/login/', methods=['GET', 'POST'])
def login():
    form = loginForm()

    if form.validate_on_submit():
        email = str(form.email.data)
        password = str(form.password.data)

        _user = db_session.query(User).filter(User.email == email).first()
        # if there's a user with the given email grab it and check for the password
        if _user is not None:
            if check_password_hash(_user.password, password):
            # generate token
                token = jwt.encode(
                    {'public_id': _user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=365)},
                    app.config['SECRET_KEY'])
                session['token'] = token
                return redirect(url_for('index'))
                print(f"[INFO] Logged in")
            else:
                flash("Wrong email or password")
        else:
            flash("Wrong email or password")
    else:
        # flash("Wrong email or password")
        print("[INFO] Login form not submited")


    return render_template('login.html', form=form)

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
            password=generate_password_hash(str(form.password.data), method='sha256'),
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
    return redirect(url_for('index'))

@app.route('/my_profile')
def my_profile():
    return render_template('index.html')

@app.route('/my_bookings')
def my_bookings():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact_us')
def contact_us():
    return render_template('index.html')

@app.route('/faq')
def faq():
    return render_template('index.html')