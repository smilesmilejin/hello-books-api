# app/models/book_genre.py
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from ..db import db

class BookGenre(db.Model):
    #   Specifying the Table Name
    # we can specify a different name for the table, using the __tablename__ property. 
  __tablename__ = "book_genre"

  book_id: Mapped[int] = mapped_column(ForeignKey("book.id"), primary_key=True)
  genre_id: Mapped[int] = mapped_column(ForeignKey("genre.id"), primary_key=True)