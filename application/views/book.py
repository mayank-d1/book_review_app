import csv

from application.models.book import Book, db


def store_books_in_db():
    with open('books.csv')as f:
        data = csv.DictReader(f)
        book_obj_list = []
        for book_info in data:
            book_obj = Book(isbn=book_info["isbn"], title=book_info["title"],
                            author=book_info["author"], year=int(book_info["year"]))
            book_obj_list.append(book_obj)

        db.session.bulk_save_objects(objects=book_obj_list)
        db.session.commit()


def get_book_listing(page_no, page_size):
    offset = (page_no - 1) * page_size
    if offset < 0:
        offset = 0
    books = Book.query.offset(offset).limit(page_size).all()
    return books



