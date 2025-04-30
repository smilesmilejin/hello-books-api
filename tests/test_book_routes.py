from app.models.book import Book
import pytest
# # Added from 06 Building an API testing
# # Continuing our best pytest practices, this test should start with the name test_, and it should describe the nature of this test. The name is shortened here for formatting purposes.
# # We pass in the client fixture here, which we registered in conftest.py. pytest automatically tries to match each test parameter to a fixture with the same name.
# def test_get_all_books_with_no_records(client):
#     # Act
#     # This sends an HTTP request to /books. It returns an HTTP response object, which we store in our local variable response
#     response = client.get("/books")
#     # We can get the JSON response body with response.get_json()
#     response_body = response.get_json()

#     # Assert
#     # Every response object will have a status_code. 
#     # We can read that status code and check it against the expected status code.
#     assert response.status_code == 200
#     # We can check all of the parts of the response body that we need to verify. We can check its contents, size, values, etc!
#     assert response_body == []

# # To actually use this fixture in a test, we need to request it by name.
# def test_get_one_book(client, two_saved_books):
#     # Act
#     response = client.get("/books/1")
#     response_body = response.get_json()

#     # Assert
#     assert response.status_code == 200
#     assert response_body == {
#         "id": 1,
#         "title": "Ocean Book",
#         "description": "watr 4evr"
#     }

# # We'll wrap up our foray into API unit testing with a test for our POST route create_book()
#             # tests/test_book_routes.py.
# def test_create_one_book(client):
#     # Act
#     # Sends a POST request to /books, 
#     # with the dict to be used as the JSON request body passed in using the json keyword argument
#     response = client.post("/books", json={
#         "title": "New Book",
#         "description": "The Best!"
#     })
#     # Gets the JSON response body as a Python value. 
#     # Since the create logic returns a dict, we should anticipate response_body to receive a dict result here.
#     response_body = response.get_json()

#     # Assert

#     assert response.status_code == 201 # Checks for the expected status code
#     # {...}}	Checks for the expected key/value pairs in the response body
#     assert response_body == {
#         "id": 1,
#         "title": "New Book",
#         "description": "The Best!"
#     }
# # End from 06 Building an API testing


# Added from 07 Building an API -Refactoring
# edge cases:
# The first two cases should fail to create a Book,
# the request body is missing the title keys. 

# # Method 1 for missing title or description keys
# def test_create_one_book_no_title(client):
#     # Arrange
#     test_data = {"description": "The Best!"}

#     # Act & Assert
#     with pytest.raises(KeyError, match='title'):
#         response = client.post("/books", json=test_data)

# # the request body is missing description keys. 
# def test_create_one_book_no_description(client):
#     # Arrange
#     test_data = {"title": "New Book"}

#     # Act & Assert
#     with pytest.raises(KeyError, match = 'description'):
#         response = client.post("/books", json=test_data)

################# Method 2 Updated test cases for create_book that check for a 400 Bad Response

def test_create_one_book_no_title(client):
    # Arrange
    test_data = {"description": "The Best!"}

    # Act
    response = client.post("/books", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {'message': 'Invalid request: missing title'}

def test_create_one_book_no_description(client):
    # Arrange
    test_data = {"title": "New Book"}

    # Act
    response = client.post("/books", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {'message': 'Invalid request: missing description'}


# the third case should still create a Book successfully, ignoring the extra keys.
def test_create_one_book_with_extra_keys(client):
    # Arrange
    test_data = {
        "extra": "some stuff",
        "title": "New Book",
        "description": "The Best!",
        "another": "last value"
    }

    # Act
    response = client.post("/books", json=test_data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "title": "New Book",
        "description": "The Best!"
    }

# End from 07 Building an API -Refactoring

# Added from 07 Building an API -Refactoring Part 2
# When we have records and a `title` query in the request arguments, `get_all_books` returns a list containing only the `Book`s that match the query
def test_get_all_books_with_title_query_matching_none(client, two_saved_books):
    # Act
    data = {'title': 'Desert Book'}
    response = client.get("/books", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

# When we have records and a `title` query in the request arguments, `get_all_books` returns a list containing only the `Book`s that match the query
def test_get_all_books_with_title_query_matching_one(client, two_saved_books):
    # Act
    data = {'title': 'Ocean Book'}
    response = client.get("/books", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert len(response_body) == 1
    assert response_body[0] == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }

# When we call `get_one_book` with a numeric ID that doesn't have a record, we get the expected error message
def test_get_one_book_missing_record(client, two_saved_books):
    # Act
    response = client.get("/books/3")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {"message": "Book 3 not found"}

# When we call `get_one_book` with a non-numeric ID, we get the expected error message
def test_get_one_book_invalid_id(client, two_saved_books):
    # Act
    response = client.get("/books/cat")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 400
    assert response_body == {"message": "Book cat invalid"}

# End # Added from 07 Building an API -Refactoring Part 2