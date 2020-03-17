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
