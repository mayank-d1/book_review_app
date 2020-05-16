from flask import (Blueprint, render_template, request,
                   redirect, url_for, session, flash)

from application.views.book import (store_books_in_db,
                                    get_book_listing,
                                    search_book,
                                    get_all_data_of_book, store_book_review)

book_bp = Blueprint("book", __name__)


@book_bp.route("/store-books")
def store_book():
    message = store_books_in_db()
    return message


@book_bp.route("/book")
def book_listing():
    if not session.get("user_id"):
        flash("Please login or register to access this.")
        return redirect(url_for("user.login"))
    page_no = int(request.args.get("page", '0'))
    page_size = 12
    books = get_book_listing(page_no=page_no, page_size=page_size)
    return render_template("book_listing.html", books=books, curr_page=page_no or 1)


@book_bp.route("/book/<book_isbn>")
def get_book_details(book_isbn):
    if not session.get("user_id"):
        flash("Please login or register to access this.")
        return redirect(url_for("user.login"))
    book = get_all_data_of_book(book_isbn)
    return render_template("book_detail.html", book=book)


@book_bp.route("/book/search", methods=["POST"])
def book_search():
    if not session["user_id"]:
        flash("Please login or register to access this.")
        return redirect(url_for("user.login"))
    data = request.form
    if not data.get("option"):
        flash("Please choose one option")
        return redirect(url_for("book.book_listing"))
    book_details = search_book(data=data)
    return render_template("book_listing.html", books=book_details, curr_page=1)


@book_bp.route("/book/<book_isbn>/review", methods=["POST"])
def book_review(book_isbn):
    if not session.get("user_id"):
        flash("Please login or register to access this.")
        return redirect(url_for("user.login"))
    data = request.form
    store_book_review(book_isbn, data)
    flash("Review successfully submitted.")
    return redirect(url_for("book.get_book_details", book_isbn=book_isbn))
