from app.models.book import Book

# Continuing our best pytest practices, this test should start with the name test_, and it should describe the nature of this test. The name is shortened here for formatting purposes.
# We pass in the client fixture here, which we registered in conftest.py. pytest automatically tries to match each test parameter to a fixture with the same name.
def test_get_all_books_with_no_records(client):
    # Act
    # This sends an HTTP request to /books. It returns an HTTP response object, which we store in our local variable response
    response = client.get("/books")
    # We can get the JSON response body with response.get_json()
    response_body = response.get_json()

    # Assert
    # Every response object will have a status_code. 
    # We can read that status code and check it against the expected status code.
    assert response.status_code == 200
    # We can check all of the parts of the response body that we need to verify. We can check its contents, size, values, etc!
    assert response_body == []

# To actually use this fixture in a test, we need to request it by name.
def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Ocean Book",
        "description": "watr 4evr"
    }
