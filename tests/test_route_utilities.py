# Added from 07 Building an API -Refactoring Part 3
# New test cases for update_book, delete_book, and validate_book
from werkzeug.exceptions import HTTPException
# from app.routes import validate_book # This one does NOT work!
# from app.routes.book_routes import validate_book # After move validate_book to validate_model, delete this
import pytest
from app.models.book import Book
# from app.routes import validate_model # This given does NOT work!
from app.routes.route_utilities import validate_model

def test_validate_book(two_saved_books):
    # Act
    # Add `Book` argument to `validate_book` invocation
    result_book = validate_model(Book, 1)

    # Assert
    assert result_book.id == 1
    assert result_book.title == "Ocean Book"
    assert result_book.description == "watr 4evr"

# def test_validate_book(two_saved_books):
#     # Act
#     result_book = validate_book(1)

#     # Assert
#     assert result_book.id == 1
#     assert result_book.title == "Ocean Book"
#     assert result_book.description == "watr 4evr"

def test_validate_book_missing_record(two_saved_books):
    # Act & Assert
    # Calling `validate_book` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        # result_book = validate_book("3")
        # Add `Book` argument to `validate_book` invocation  - 07 Part 3
        result_book = validate_model(Book, "3")
    
def test_validate_book_invalid_id(two_saved_books):
    # Act & Assert
    # Calling `validate_book` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        # result_book = validate_book("cat")
        # Add `Book` argument to `validate_book` invocation  - 07 Part 3
        result_book = validate_model(Book, "3")




def test_validate_model(two_saved_books):
    # Act
    result_book = validate_model(Book, 1)

    # Assert
    assert result_book.id == 1
    assert result_book.title == "Ocean Book"
    assert result_book.description == "watr 4evr"

def test_validate_model_missing_record(two_saved_books):
    # Act & Assert
    # Calling `validate_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        result_book = validate_model(Book, "3")
    
def test_validate_model_invalid_id(two_saved_books):
    # Act & Assert
    # Calling `validate_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException):
        result_book = validate_model(Book, "cat")

# End from 07 Building an API -Refactoring Part 3

# Added from 08 Building an API one to many relatipnshiop Part 3
# test_route_utilities.py
from app.routes.route_utilities import validate_model, create_model
from werkzeug.exceptions import HTTPException
from app.models.book import Book
from app.models.author import Author
import pytest

# We use the `client` fixture because we need an
# application context to work with the database session
def test_create_model_book(client):
    # Arrange
    test_data = {
        "title": "New Book",
        "description": "The Best!"
    }

    # Act
    result = create_model(Book, test_data)

    # Assert
    assert isinstance(result, tuple)
    assert result[0]["id"] == 1
    assert result[0]["title"] == "New Book"
    assert result[0]["description"] == "The Best!"
    assert result[1] == 201


def test_create_model_book_missing_data(client):
    # Arrange
    test_data = {
        "description": "The Best!"
    }

    # Act & Assert
    # Calling `create_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException) as error:
        result_book = create_model(Book, test_data)

    response = error.value.response
    assert response.status == "400 BAD REQUEST"

# We use the `client` fixture because we need an   
# application context to work with the database session
def test_create_model_author(client):
    # Arrange
    test_data = {
        "name": "New Author"
    }

    # Act
    result = create_model(Author, test_data)

    # Assert
    assert isinstance(result, tuple)
    assert result[0]["id"] == 1
    assert result[0]["name"] == "New Author"
    assert result[1] == 201

from app.routes.route_utilities import validate_model, create_model, get_models_with_filters

def test_get_models_with_filters_one_matching_book(two_saved_books):
    # Act
    result = get_models_with_filters(Book, {"title": "ocean"})

    # Assert
    assert result == [{
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }]