from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email

class registerForm(FlaskForm):
    email = StringField('E-mail address', validators=[DataRequired(), Email()])
    password = StringField('Password', validators=[DataRequired()])
    first_name = StringField('First name', validators=[DataRequired()])
    last_name = StringField('Last name', validators=[DataRequired()])
    mobile = StringField('Mobile phone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    postcode = StringField('Post code', validators=[DataRequired()])
    course = StringField('Course', validators=[DataRequired()])

class loginForm(FlaskForm):
    email = StringField('email', validators=[DataRequired(), Email()])
    password = StringField('password', validators=[DataRequired()])

class changePassword(FlaskForm):
    old_password = StringField('Actual password', validators=[DataRequired()])
    new_password = StringField('New password', validators=[DataRequired()])

class updateProfile(FlaskForm):
    mobile = StringField('Mobile phone', validators=[DataRequired()])
    address = StringField('Address', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    postcode = StringField('Post code', validators=[DataRequired()])
    course = StringField('Course', validators=[DataRequired()])

class buyTicket(FlaskForm):
    event_id = StringField('', validators=[DataRequired()])
    user_id = StringField('', validators=[DataRequired()])

class createEvent(FlaskForm):
    user_id = StringField('user_id', validators=[DataRequired()])
    category_id = StringField('Category', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    venue = StringField('Venue', validators=[DataRequired()])
    description = StringField('Description', validators=[DataRequired()])
    slots_available = StringField('Slots available', validators=[DataRequired()])
    datetime = StringField('Datetime', validators=[DataRequired()])
    entry_price = StringField('Price per ticket', validators=[DataRequired()])