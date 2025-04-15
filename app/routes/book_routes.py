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

@books_bp.get("/<book_id>")
def get_one_book(book_id):
    try:
        book_id = int(book_id)
    except ValueError:
        return {"message": f"book {book_id} invalid"}, 400
    
    for book in books:
        if book.id == book_id:
            return {
                "id": book.id,
                "title": book.title,
                "description": book.description,
            }
        
    return {"message": f"book {book_id} not found"}, 404

