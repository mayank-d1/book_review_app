from application import db


class Book(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True)
    isbn = db.Column(db.String(10), nullable=False, unique=True)
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String(50), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    user = db.relationship("BookReview", backref='user_review')


class BookReview(db.Model):
    __tablename__ = "book_review"
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer(), db.ForeignKey("book.id"))
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
    rating = db.Column(db.Float(), nullable=True)
    review = db.Column(db.Text(), nullable=True)
