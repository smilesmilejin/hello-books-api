################## 03 Building an API: Comment the hardcoded books data 
# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Fictional Book", "A fantasy novel set in an imaginary world."),
#     Book(2, "Wheel of Time", "A fantasy novel set in an imaginary world."),
#     Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world.")
# ]

 ############## End 03 Building an API: Comment the hardcoded books data 

################## Added from 03 Building an API
from sqlalchemy.orm import Mapped, mapped_column # This file needs access to SQLAlchemy's tools for defining table columns in a model
from ..db import db

# By default, SQLAlchemy will use the lowercase version of this class name as the name of the table it will create.
class Book(db.Model):
    # Instances of Book will have an attribute id, which maps to a database column of type int. 
    # Notice that this attribute goes outside of any instance method and doesn't reference self.
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    
    # Creates a required title attribute, which maps to a string column, title
    title: Mapped[str]
    
    # Creates a required description attribute, which maps to a string column, description
    # To mark a text column as nullable, we would need to add Optional to the type hint, written as Mapped[Optional[str]].
    description: Mapped[str]

# If deleting rows with id 1, the next insert will be 2, run the folloiwng query to reset autoincrement in 1 
    # SELECT pg_get_serial_sequence('book', 'id');
    # ALTER SEQUENCE public.book_id_seq RESTART WITH 1;