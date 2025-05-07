# app/routes/genre_routes.py
from flask import Blueprint, request
from app.models.genre import Genre
from app.models.book import Book
from .route_utilities import create_model, get_models_with_filters, validate_model

bp = Blueprint("genres_bp", __name__, url_prefix="/genres")

@bp.post("")
def create_genre():
    request_body = request.get_json()
    return create_model(Genre, request_body)

@bp.get("")
def get_all_genres():
    return get_models_with_filters(Genre, request.args)

# Added from 10 Builing an API
@bp.post("/<genre_id>/books")
def create_book_with_genre(genre_id):
    genre = validate_model(Genre, genre_id)

    request_body = request.get_json()
    request_body["genres"] = [genre]
    return create_model(Book, request_body)


# Added from 10 Builing an API
### GET /genres/<genre_id>/books
# Finally, let's create a route to get all books by a specific genre.
@bp.get("/<genre_id>/books")
def get_books_by_genre(genre_id):
    genre = validate_model(Genre, genre_id)
    response = [book.to_dict() for book in genre.books]
    return response

# Manual Testing in Postman
# Now that we have established a relationship between the Genre and Book models, we can test our changes using Postman.
    # View the genres in the database and the books in the database with a GET request to /genres and a GET to /books.
    # Create a book of a specific genre with a POST request to /genres/<genre_id>/books.
    # Verify the genres have been added to the book with a GET request to /books/<book_id>.
    # View all books of a specific genre with a GET request to /genres/<genre_id/books.

# 1
# Many-to-Many: Nested Routes
# We have routes to create a new Book record with a specific Genre, but we don’t have a route that supports updating an existing book to add a Genre.
# Which of the options below:
# follows Python and Flask best practices?
# follows patterns we’ve established in the hello-books-api project?
# enables us to update an existing Book record with a Genre?
# Select one option.

# 1
# Many-to-Many: Nested Routes
# Submitted on today at 10:24 PM
# We have routes to create a new Book record with a specific Genre, but we don’t have a route that supports updating an existing book to add a Genre.
# Which of the options below:
# follows Python and Flask best practices?
# follows patterns we’ve established in the hello-books-api project?
# enables us to update an existing Book record with a Genre?

# Create an update_book instance method in the Book class that takes in a dictionary and updates the book’s attributes for valid keys.

# Create a PUT nested route at the path /genres/<genre_id>/books/<book_id>. This route:

# Confirms if the genre and book passed in the path exists.
# If they both exist, the genre with genre_id is added to the list of genres held by the book instance.
# Commits any changes to the database.
