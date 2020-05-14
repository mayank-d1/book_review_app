from flask import Blueprint, render_template, request

from application.views.book import store_books_in_db, get_book_listing

book_bp = Blueprint("book", __name__)


@book_bp.route("/store-books")
def store_book():
    store_books_in_db()
    return "BOOK SAVED IN DB"


@book_bp.route("/book")
def book_listing():
    page_no = int(request.args.get("page", '0'))
    page_size = 16
    books = get_book_listing(page_no=page_no, page_size=page_size)
    return render_template("book_listing.html", books=books, curr_page=page_no or 1)


@book_bp.route("/book/<string:book_isbn>")
def get_book_details(book_isbn):
    pass


@book_bp.route("/book/search", methods=["POST"])
def book_search():
    pass
