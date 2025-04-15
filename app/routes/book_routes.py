from flask import Blueprint
from app.models.book import books

books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

# Use the books_bp blueprint with a decorator to define a GET request endpoint
@books_bp.get("")
# @books_bp.get("", strict_slashes=False)
def get_all_books():
    books_response = []
    for book in books:
        books_response.append(
            {
                "id": book.id,
                "title": book.title,
                "description": book.description
            }
        )
    return books_response