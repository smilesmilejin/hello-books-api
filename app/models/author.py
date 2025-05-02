
##################### Added from 08 Building an API one-to-many Part 1
# To show relationship of models
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db


class Author(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    books: Mapped[list["Book"]] = relationship(back_populates="author")

    def to_dict(self):
        author_as_dict = {
            "id": self.id,
            "name": self.name
        }
        
        return author_as_dict
    
    @classmethod
    def from_dict(cls, author_data):
        new_author = cls(name=author_data["name"])
        return new_author
    
##################### End from 08 Building an API one-to-many Part 1
