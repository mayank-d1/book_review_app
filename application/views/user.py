from application.models.user import db, User


def create_user(data):
    user = User(name=data.name.data,
                email=data.email.data)
    user.set_password(data.password.data)
    db.session.add(user)
    db.session.commit()  # Create new user



