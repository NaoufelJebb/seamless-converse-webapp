from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class SignUpForm(FlaskForm):
    """User registration form."""

    email = StringField(
        'Email Address',
        validators=[
            DataRequired(),
            Length(min=5, max=64),
            Email(message='Please enter a valid email address.'),
        ]
    )

    name = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=2, max=32),
        ]
    )

    password = PasswordField(
        'Enter Your Password',
        validators=[
            Length(min=10, max=64, message='Please provide a stronger password.'),
            DataRequired(),

        ]
    )

    password_confirm = PasswordField(
        'Confirm Your Password',
        validators=[
            DataRequired(),
            EqualTo('password', message='Passwords must match.')
        ]
    )

    recaptcha = RecaptchaField()
    submit = SubmitField('Register')


class SignInForm(FlaskForm):
    """User login form."""

    email = StringField(
        'Email Address',
        validators=[
            DataRequired(),
            Email(message='Please enter a valid Email Address.')
        ]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
        ]
    )

    submit = SubmitField('Log In')


class ContactUsForm(FlaskForm):
    """Contact form."""

    name = StringField(
        'User Name',
        validators=[
            DataRequired(),
            Email(message='Please enter a valid Email Address.')
        ]
    )

    email = StringField(
        'Email Address',
        validators=[
            DataRequired(),
        ]
    )

    message = StringField(
        'Message',
        validators=[
            Length(max=1024, message="Message is too long."),
            DataRequired(),
            Email(),
        ]
    )
