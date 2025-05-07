# Added from 10 Building an API Many to Many Relationships

# For migration, we need to import this model in another file __init__.p[y], to let it detect. 
    # app/models/genre.py
    # from .models import book, genre
# app/models/genre.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db

class Genre(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    # genre.books returns a list of Book instances associated with the Genre instance named genre.
    # book_genre is the linking table
    books: Mapped[list["Book"]] = relationship(secondary="book_genre", back_populates="genres") 

    def to_dict(self):
        genre_as_dict = {}
        genre_as_dict["id"] = self.id
        genre_as_dict["name"] = self.name

        return genre_as_dict

    @classmethod
    def from_dict(cls, genre_data):
        new_genre = cls(name=genre_data["name"])
        return new_genre
    

