##################### Added from 08 Building an API one-to-many Part 1
# Self
from app.models.author import Author
import pytest

# Self
def test_from_dict_return_author():
    author_data = {"name": "David"}
    new_author = Author.from_dict(author_data)

    assert new_author.name == "David"

def test_from_dict_with_no_name():
    author_data= {}

    with pytest.raises(KeyError, match = 'name'):
        new_author = Author.from_dict(author_data)

def test_from_dict_with_extra_keys():
    # Arrange
    author_data = {
        "name": "Emma",
        "age": 22
    }

    # Act
    new_book = Author.from_dict(author_data)

    # Assert
    assert new_book.name == "Emma"

def test_to_dict_no_missing_data():
    new_book_instance = Author(id=1, name="Emily")
    
    result = new_book_instance.to_dict()

    # Assert
    assert len(result) == 2
    assert result["name"] == "Emily"
    assert result== {
        "id":1,
        "name": "Emily"
    }


def test_to_dict_missing_id():
    new_book_instance = Author(name="Emily")
    
    result = new_book_instance.to_dict()

    # Assert
    assert len(result) == 2
    assert result["id"] is None
    assert result["name"] == "Emily"
    assert result== {
        "id":None,
        "name": "Emily"
    }

def test_to_dict_missing_name():
    
    new_book_instance = Author(id=1)
    
    result = new_book_instance.to_dict()

    # Assert
    assert len(result) == 2
    assert result["id"] == 1
    assert result["name"] is None
    assert result== {
        "id":1,
        "name": None
    }