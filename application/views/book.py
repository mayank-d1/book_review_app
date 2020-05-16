import csv
import os

import requests

from application.models.book import Book, db


def store_books_in_db():
    book = Book.query.limit(1).all()
    if book:
        return "BOOKS ALREADY THERE IN DB"
    with open('books.csv')as f:
        data = csv.DictReader(f)
        book_obj_list = []
        for book_info in data:
            book_obj = Book(isbn=book_info["isbn"], title=book_info["title"],
                            author=book_info["author"], year=int(book_info["year"]))
            book_obj_list.append(book_obj)

        db.session.bulk_save_objects(objects=book_obj_list)
        db.session.commit()

    return "BOOKS SAVED IN DB"


def get_book_listing(page_no, page_size):
    offset = (page_no - 1) * page_size
    if offset < 0:
        offset = 0
    books = Book.query.offset(offset).limit(page_size).all()
    return books


def search_book(data):
    search_type = data.get("option")
    search_text = data.get("search-text")
    books = Book.query.filter((getattr(Book, search_type).ilike('%' + search_text + '%'))).all()
    # books = map(get_good_reads_data, books)
    return books


def get_all_data_of_book(book_isbn):
    book = Book.query.filter_by(isbn=book_isbn).first()
    res = requests.get("https://www.goodreads.com/book/review_counts.json",
                       params={"key": os.environ.get("GOOD_READ_KEY"), "isbns": book_isbn})
    if res.status_code == 200:
        res = res.json()
        book.no_of_ratings = res["books"][0]["work_ratings_count"]
        book.avg_rating = res["books"][0]["average_rating"]

    else:
        book["no_of_ratings"] = 0
        book["avg_rating"] = 0
    return book

