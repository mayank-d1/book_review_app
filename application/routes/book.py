from flask import Blueprint, render_template, request, redirect, url_for

from application.views.book import (store_books_in_db,
                                    get_book_listing,
                                    search_book,
                                    get_all_data_of_book)

book_bp = Blueprint("book", __name__)


@book_bp.route("/store-books")
def store_book():
    message = store_books_in_db()
    return message


@book_bp.route("/book")
def book_listing():
    page_no = int(request.args.get("page", '0'))
    page_size = 12
    books = get_book_listing(page_no=page_no, page_size=page_size)
    return render_template("book_listing.html", books=books, curr_page=page_no or 1)


@book_bp.route("/book/<book_isbn>")
def get_book_details(book_isbn):
    book = get_all_data_of_book(book_isbn)
    return render_template("book_detail.html", book=book)


@book_bp.route("/book/search", methods=["POST"])
def book_search():
    data = request.form
    book_details = search_book(data=data)
    return render_template("book_listing.html", books=book_details, curr_page=1)


@book_bp.route("/book/<book_isbn>/review", methods=["POST"])
def book_review(book_isbn):
    data = request.form
    return redirect(url_for("book.get_book_details", book_isbn=book_isbn))
