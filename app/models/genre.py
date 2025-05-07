# Added from 10 Building an API Many to Many Relationships

# For migration, we need to import this model in another file __init__.p[y], to let it detect. 
    # app/models/genre.py
    # from .models import book, genre
# app/models/genre.py
from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Genre(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]

    def to_dict(self):
        genre_as_dict = {}
        genre_as_dict["id"] = self.id
        genre_as_dict["name"] = self.name

        return genre_as_dict

    @classmethod
    def from_dict(cls, genre_data):
        new_genre = cls(name=genre_data["name"])
        return new_genre