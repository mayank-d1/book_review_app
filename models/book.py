from models import db


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(10), nullable=True)
    title = db.Column(db.String(50), nullable=True)
    author = db.Column(db.String(50), nullable=True)
    year = db.Column(db.Integer, nullable=True)
