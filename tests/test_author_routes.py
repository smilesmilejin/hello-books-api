##################### Added from 08 Building an API one-to-many Part 1
# Self
from app.models.author import Author
import pytest

def test_create_one_book(client):
    author_data = {"name": "David"}

    response = client.post("/authors", json=author_data)
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "David"

    }

def test_create_one_book_no_name_empty_request_body(client):
    # Arrange
    author_data = {}

    response = client.post("authors", json=author_data)
    response_body = response.get_json()

    assert response.status_code == 400
    assert response_body == {"message": f"Invalid request: missing name"}

# the third case should still create a Author successfully, ignoring the extra keys.
def test_create_one_author_with_extra_keys(client):
    author_data = {
        "name": "David",
        "age": 22
    }

    response = client.post("/authors", json=author_data)
    response_body = response.get_json()

    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "name": "David"
    }

def test_get_all_authors_empty_database(client):
    response = client.get("/authors")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_all_authors_with_name_query_matching_none(client, two_saved_authors):
    # Act
    data = {"name": "Emma"}
    response = client.get("/authors", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_all_authors_with_name_query_matching_one(client, two_saved_authors):

    data = {"name": "Frank"}
    response = client.get("/authors", query_string = data)
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == [
        {
            "id": 2,
            "name": "Frank"
        }
    ]