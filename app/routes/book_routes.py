
################## 03 Building an API: comment the following
# from flask import Blueprint, abort, make_response
# from app.models.book import books

# books_bp = Blueprint("books_bp", __name__, url_prefix="/books")




# # Use the books_bp blueprint with a decorator to define a GET request endpoint
# @books_bp.get("")
# # @books_bp.get("", strict_slashes=False)
# def get_all_books():
#     books_response = []
#     for book in books:
#         books_response.append(
#             {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }
#         )
#     return books_response

# @books_bp.get("/<book_id>")
# def get_one_book(book_id):
#     book = validate_book(book_id)

#     return {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description,
#     }


# def validate_book(book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         # When book_id is not a number
#         response = {"message": f"book {book_id} invalid"}
#         abort(make_response(response, 400))

#     for book in books:
#         if book.id == book_id:
#             return book

#     # When book_id does not exist in books
#     response = {"message": f"book {book_id} not found"}
#     abort(make_response(response, 404))

################## END 03 Building an API: comment the following


################## 03 Building an API:Create

from flask import Blueprint, abort, make_response, request
from app.models.book import Book
from ..db import db

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

@books_bp.post("")
def create_book():
    request_body = request.get_json() # use request to accesss to incoming request data
    title = request_body["title"]
    description = request_body["description"]

    new_book = Book(title=title, description=description)
    db.session.add(new_book) # Add new_book to the database
    db.session.commit() # database commit the changes

    response = {
        "id": new_book.id,
        "title": new_book.title,
        "description": new_book.description,
    }
    return response, 201