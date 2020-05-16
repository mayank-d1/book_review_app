from flask import session
from application.models.user import db, User


def check_and_create_user(data):
    response = dict()
    if data.validate_on_submit():
        existing_user = User.query.filter_by(email=data.email.data).first()
        if existing_user is None:
            user = User(name=data.name.data,
                        email=data.email.data)
            user.set_password(data.password.data)
            db.session.add(user)
            db.session.commit()
            session["user_id"] = user.id
            response["message"] = "Successfully registered"
            response["redirect_to"] = "book.book_listing"

        return response


def check_and_login(data):
    response = dict()
    if data.validate_on_submit():
        user = User.query.filter_by(email=data.email.data).first()  # Validate Login Attempt
        if user and user.check_password(password=data.password.data):
            session["user_id"] = user.id
            response["message"] = "Successfully logged in"
            response["redirect_to"] = "book.book_listing"

    return response
