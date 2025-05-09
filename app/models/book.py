# ################## 03 Building an API: Comment the hardcoded books data 
# # class Book:
# #     def __init__(self, id, title, description):
# #         self.id = id
# #         self.title = title
# #         self.description = description

# # books = [
# #     Book(1, "Fictional Book", "A fantasy novel set in an imaginary world."),
# #     Book(2, "Wheel of Time", "A fantasy novel set in an imaginary world."),
# #     Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
# # ]

#  ############## End 03 Building an API: Comment the hardcoded books data 

# ################## Added from 03 Building an API
# # from sqlalchemy.orm import Mapped, mapped_column # This file needs access to SQLAlchemy's tools for defining table columns in a model
# # from ..db import db
# ##################### Added from 08 Building an API one-to-many Part 1
# from sqlalchemy.orm import Mapped, mapped_column, relationship
# from sqlalchemy import ForeignKey
# from typing import Optional
# from ..db import db
# ##################### End from 08 Building an API one-to-many Part 1

# # By default, SQLAlchemy will use the lowercase version of this class name as the name of the table it will create.
# class Book(db.Model):

#     # Added from 07 Building an API - Refactoring
#     # Complete from_dict function example
#     # indented under the Book class definition
#     @classmethod
#     def from_dict(cls, book_data):
#         new_book = Book(title=book_data["title"],
#                         description=book_data["description"])
#         return new_book
#     # End from 07 Building an API - Refactoring

#     # Instances of Book will have an attribute id, which maps to a database column of type int. 
#     # Notice that this attribute goes outside of any instance method and doesn't reference self.
#     id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
#     # Creates a required title attribute, which maps to a string column, title
#     title: Mapped[str]
    
#     # Creates a required description attribute, which maps to a string column, description
#     # To mark a text column as nullable, we would need to add Optional to the type hint, written as Mapped[Optional[str]].
#     description: Mapped[str]

#     ##################### Added from 08 Building an API one-to-many Part 1
#     # For example, while Mapped[Optional[int]] declares a nullable integer column, 
#     # Mapped[int] declares an integer column that disallows NULL values, just as Mapped[str] declares a required string column.
#     # Defining Relationships as Optional or Required
#     author_id: Mapped[Optional[int]] = mapped_column(ForeignKey("author.id"))
#     author: Mapped[Optional["Author"]] = relationship(back_populates="books")

#     ##################### End from 08 Building an API one-to-many Part 1

# # If deleting rows with id 1, the next insert will be 2, run the folloiwng query to reset autoincrement in 1 
#     # SELECT pg_get_serial_sequence('book', 'id');
#     # ALTER SEQUENCE public.book_id_seq RESTART WITH 1;

#     # Added from 07 Building an API - Refactoring Part 2
#     def to_dict(self):
#         book_as_dict = {}
#         book_as_dict["id"] = self.id
#         book_as_dict["title"] = self.title
#         book_as_dict["description"] = self.description

#         return book_as_dict
#     # End from 07 Building an API - Refactoring Part 2


##################### Added from 08 Building an API one-to-many Part 2
# app/models/book.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db

class Book(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]
    author_id: Mapped[Optional[int]] = mapped_column(ForeignKey("author.id"))
    author: Mapped[Optional["Author"]] = relationship(back_populates="books")
    # Added from 10 Building an API
    # book.genres returns a list of Genre instances associated with the Book instance named book.
    genres: Mapped[list["Genre"]] = relationship(secondary="book_genre", back_populates="books") 

    # Added from 10 Building an API many to many 
    def to_dict(self):
        book_as_dict = {}
        book_as_dict["id"] = self.id
        book_as_dict["title"] = self.title
        book_as_dict["description"] = self.description

        if self.author:
            book_as_dict["author"] = self.author.name

        if self.genres:
            book_as_dict["genres"] = [genre.name for genre in self.genres]

        return book_as_dict

    # Added from 10 Building an API many to many 
    @classmethod
    def from_dict(cls, book_data):
        # Use get() to fetch values that could be undefined to avoid raising an error
        author_id = book_data.get("author_id")
        genres = book_data.get("genres", [])

        new_book = cls(
            title=book_data["title"],
            description=book_data["description"],
            author_id=author_id,
            genres=genres
        )

        return new_book
    
##################### End from 08 Building an API one-to-many Part 2