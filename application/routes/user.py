from flask import (Blueprint, render_template, url_for,
                   redirect, flash, request, session)

from application.views.user import check_and_create_user, check_and_login
from application.forms import SignupForm, LoginForm

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
    if request.method == "POST":
        response = check_and_login(data=form)
        if response:
            flash(response["message"], "message")
            return redirect(url_for(response["redirect_to"]))
        flash("Invalid email/password.")
    return render_template('login.html', form=form)


@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    User register page.

    GET: Serve register page.
    POST: Validate form.
    """
    form = SignupForm()
    if request.method == "POST":
        response = check_and_create_user(data=form)
        if response:
            flash(response["message"])
            return redirect(url_for(response["redirect_to"]))

        flash('User already exists with that email address.')
    return render_template('register.html', form=form)


@user_bp.route("/logout", methods=["GET"])
def logout():
    if not session.get("user_id"):
        flash("Please login or register before doing this.")
    session.pop("user_id")
    flash("Logged out Successfully")
    return redirect(url_for("user.login"))
