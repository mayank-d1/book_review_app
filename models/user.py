from models import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Sring(50), nullable=False)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(100), nullable=False)
