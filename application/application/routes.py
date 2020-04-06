from flask import Flask, render_template, request, flash, redirect, session, url_for
from werkzeug.security import generate_password_hash, check_password_hash
import json
import jwt
import datetime

from application import app
from application.database import db_session
from application.forms import registerForm, loginForm, changePassword, updateProfile, buyTicket, createEvent

from application.models.User import User
from application.models.Event import Event
from application.models.Booking import Booking
from application.models.Category import Category

def get_user():
    token = jwt.decode(session['token'], app.config['SECRET_KEY'])
    user = User.query.filter_by(id=token['id']).first()
    return user

@app.before_request
def require_login():
    """
    all routes are protected except the ones from  allowed_routes
    if a session is initialized with a valid token the access is granted
    """
    allowed_routes = ['login', 'register', 'static']
    if request.endpoint not in allowed_routes and 'token' not in session:
        return redirect(url_for('login'))

@app.route('/login/', methods=['GET','POST'])
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
                    {'id': _user.id, 'exp': datetime.datetime.utcnow() + datetime.timedelta(days=365)},
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

@app.route('/register/', methods=['GET','POST'])
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
            is_admin=False
        )

        if request.form.getlist('is_guest'):
            _user.is_guest = True
        else:
            _user.is_guest = False

        db_session.add(_user)

        try:
            db_session.commit()
            return redirect(url_for('login'))
        except:
            flash('Email address already taken')
            return redirect(url_for('register'))

    return render_template('register.html', form=form)

@app.route('/logout/')
def logout():
    del session['token']
    return redirect(url_for('index'))
    
@app.route('/my_profile/', methods=['GET', 'POST'])
def my_profile():
    _user = get_user()
    form = changePassword()
    form2 = updateProfile()

    if "form-submit" in request.form and form.validate_on_submit():
        actual_password = str(form.old_password.data)
        new_password = str(form.new_password.data)

        if check_password_hash(_user.password, actual_password):
            _user.password = generate_password_hash(str(form.new_password.data), method='sha256')
            db_session.commit()
            flash('Password updated')
        else:
            flash('This is not your password')

    if "form2-submit" in request.form and form2.validate_on_submit():
        _user.mobile = str(form2.mobile.data)
        _user.address = str(form2.address.data)
        _user.city = str(form2.city.data)
        _user.postcode = str(form2.postcode.data)
        _user.course = str(form2.course.data)

        db_session.commit()
        flash('Profile updated')

    return render_template('my_profile.html', user=_user, form=form, form2=form2)

@app.route('/my_bookings')
def my_bookings():
    _user = get_user()
    _bookings = db_session.query(Booking, Event).join(Event).filter(Booking.user_id == _user.id)
    return render_template('my_bookings.html', user=_user, bookings=_bookings)

@app.route('/')
def index():
    _user = get_user()
    return render_template('index.html', user=_user)

@app.route('/events', methods=['GET'])
def events():
    # the data is structured into a list where 
    # 0 is the index for event 
    # 1 for category
    _user = get_user()
    all_categories = Category.query.all()
    all_events = db_session.query(Event, Category).join(Category).all()

    if request.args.get('name') or request.args.get('location') or request.args.get('category'):
        all_events = db_session.query(Event, Category).join(Category).filter(
            Event.name.like('%' + request.args.get('name') + '%'),
            Event.venue.like('%' + request.args.get('location') + '%'),
            Event.category_id.like('%' + request.args.get('category') + '%'))
    return render_template('events.html', events=all_events, categories=all_categories, user=_user)

@app.route('/event/<int:id>', methods=['GET', 'POST'])
def event(id):
    form = buyTicket()
    _user = get_user()
    _event = Event.query.filter(Event.id == id).first()

    if form.validate_on_submit():
        event_id = str(form.event_id.data)
        user_id = str(form.user_id.data)
        booking = Booking(
            user_id=user_id,
            event_id=event_id
        )

        if Booking.query.filter(Booking.user_id == user_id, Booking.event_id == event_id).first():
            flash('It seems like you already bought a ticket for this event. Leave some for the others')
        else:
            db_session.add(booking)
            db_session.commit()
            flash('Ticket bought successfully')


    return render_template('event.html', event=_event, user=_user, form=form)

@app.route('/contact_us/')
def contact_us():
    _user = get_user()
    return render_template('contact_us.html', user=_user)

@app.route('/faq/')
def faq():
    _user = get_user()
    return render_template('faq.html', user=_user)

@app.route('/dashboard/', methods=['GET', 'POST'])
def dashboard():
    form = createEvent()
    _user = get_user()
    _event = Event.query.filter(Event.user_id == _user.id).all()
    all_categories = Category.query.all()

    if form.validate_on_submit():
        _event = Event(
            user_id=str(form.user_id.data),
            name=str(form.name.data),
            venue=str(form.venue.data),
            description=str(form.description.data),
            slots_available=str(form.slots_available.data),
            datetime=str(form.datetime.data),
            entry_price=str(form.entry_price.data),
            event_type="test",
            category_id=str(form.category_id.data),
        )
        db_session.add(_event)
        try:
            db_session.commit()
            flash('New event created')
            return redirect(url_for('dashboard'))
        except:
            pass

    return render_template('dashboard.html', form=form, user=_user, events=_event, categories=all_categories)