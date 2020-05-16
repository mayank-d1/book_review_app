from flask import Blueprint, render_template, request, url_for, redirect, flash

from application.views.user import create_user
from application.forms import SignupForm, LoginForm
from application.models.user import User

# Blueprint Configuration
user_bp = Blueprint('user', __name__)


@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    User login page.

    GET: Serve login page.
    POST: Validate form.
    """
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()  # Validate Login Attempt
        if user and user.check_password(password=form.password.data):
            return redirect(url_for('book.book_listing'))
        flash('Invalid username/password combination')
        return redirect(url_for('user.login'))

    return render_template('login.html', form=form)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    User register page.

    GET: Serve register page.
    POST: Validate form.
    """
    form = SignupForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user is None:
            create_user(data=form)
            return redirect(url_for('book.book_listing'))

        flash('A user already exists with that email address.')

    # User sign-up logic will go here.

    return render_template('register.html', form=form)


@user_bp.route("/logout", methods=["GET"])
def logout():
    return "Logged out Successfully"
