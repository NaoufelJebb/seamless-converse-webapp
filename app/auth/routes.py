from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, login_required
from app.auth import auth_bp
from app.auth.forms import SignInForm, SignUpForm, ContactUsForm
from app.auth.models import UserModel
from app.extensions import users_db, login_manager


@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    """doc."""

    form = SignUpForm()

    if form.validate_on_submit():
        registered_user = UserModel.query.filter_by(email=form.email.data).first()
        if registered_user is None:
            new_user = UserModel(
                name=form.name.data,
                email=form.email.data
            )

            new_user.set_password_hash(form.password.data)
            users_db.session.add(new_user)
            users_db.session.commit()
            login_user(new_user)
            return redirect(url_for('/dashboard'))

        flash('A User is already registered with this email address.', 'error')

    return render_template('signup.html', form=form)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """doc."""

    form = SignInForm()

    if form.validate_on_submit():
        registered_user = UserModel.query.filter_by(email=form.email.data).first()
        if registered_user and registered_user.check_password(form.password.data):
            login_user(registered_user)
            return redirect(url_for('/dashboard'))

        flash('Wrong Credentials: Invalid email or password', 'error')

    return render_template('login.html', form=form)

@auth_bp.route('/logout')
@login_required
def logout():
    """doc."""
    logout_user()
    return redirect(url_for('/welcome'))


@auth_bp.route('/contact', methods=['GET', 'POST'])
def contact_us():
    """doc."""
    form = ContactUsForm()

    if form.validate_on_submit():
        flash('Thank you for submitting your response!\n'
              'We will get back to you as soon.',
              'message')

        # Use Flask-Mail ?

    return render_template('contact.html', form=form)


@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    return UserModel.query.get(user_id)


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.login'))
