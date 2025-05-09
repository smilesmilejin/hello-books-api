
################## 03 Building an API: comment the following
# from flask import Blueprint, abort, make_response
# from app.models.book import books

# books_bp = Blueprint("books_bp", __name__, url_prefix="/books")




# # Use the books_bp blueprint with a decorator to define a GET request endpoint
# @books_bp.get("")
# # @books_bp.get("", strict_slashes=False)
# def get_all_books():
#     books_response = []
#     for book in books:
#         books_response.append(
#             {
#                 "id": book.id,
#                 "title": book.title,
#                 "description": book.description
#             }
#         )
#     return books_response

# @books_bp.get("/<book_id>")
# def get_one_book(book_id):
#     book = validate_book(book_id)

#     return {
#         "id": book.id,
#         "title": book.title,
#         "description": book.description,
#     }


# def validate_book(book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         # When book_id is not a number
#         response = {"message": f"book {book_id} invalid"}
#         abort(make_response(response, 400))

#     for book in books:
#         if book.id == book_id:
#             return book

#     # When book_id does not exist in books
#     response = {"message": f"book {book_id} not found"}
#     abort(make_response(response, 404))

################## END 03 Building an API: comment the following


################## 03 Building an API:Create

from flask import Blueprint, abort, make_response, request, Response
from app.models.book import Book
from ..db import db
from .route_utilities import validate_model, create_model, get_models_with_filters

# Added 07 Building an API -Refactoring Part 3
# changes books_bp to bp
# renamed the variable to bp where it is declared
bp = Blueprint("books_bp", __name__, url_prefix="/books")

# books_bp = Blueprint("books_bp", __name__, url_prefix="/books")

# End 07 Building an API -Refactoring Part 3

# @books_bp.post("")
# def create_book():
#     request_body = request.get_json() # use request to accesss to incoming request data
#     title = request_body["title"]
#     description = request_body["description"]

#     new_book = Book(title=title, description=description)
    
#     # db.session is the database's way of collecting changes that need to be made.
#     db.session.add(new_book) # Add new_book to the database
#     db.session.commit() # database commit the changes

#     response = {
#         "id": new_book.id,
#         "title": new_book.title,
#         "description": new_book.description,
#     }
#     return response, 201

# # Added from 07 Building an API -Refactoring
# @books_bp.post("")
# def create_book():
#     request_body = request.get_json()

#     try:
#         title = request_body["title"]
#         description = request_body["description"]

#         new_book = Book(title=title, description=description)

#     except KeyError as error:
#         response = {"message": f"Invalid request: missing {error.args[0]}"}
#         abort(make_response(response, 400))

#     db.session.add(new_book)
#     db.session.commit()

#     response = {
#         "id": new_book.id,
#         "title": new_book.title,
#         "description": new_book.description,
#     }
#     return response, 201
# # End from 07 Building an API -Refactoring

# # Added from 07 Building an API -Refactoring
# # Updated create_book function example
# @books_bp.post("")
# def create_book():
#     request_body = request.get_json()
#     # Question what is request_body is empty?
#     try:
#         new_book = Book.from_dict(request_body)

#     except KeyError as error:
#         # print(error) # 'title'
#         # print(error.args) # ('title',)
#         response = {"message": f"Invalid request: missing {error.args[0]}"}
#         abort(make_response(response, 400))

#     db.session.add(new_book)
#     db.session.commit()

#     response = {
#         "id": new_book.id,
#         "title": new_book.title,
#         "description": new_book.description,
#     }
#     return response, 201
# # End from 07 Building an API -Refactoring

# Added from 07 Building an API -Refactoring Part 2
# Updated create_book function
# @bp.post("")
# def create_book():
#     request_body = request.get_json()

#     try:
#         new_book = Book.from_dict(request_body)

#     except KeyError as error:
#         response = {"message": f"Invalid request: missing {error.args[0]}"}
#         abort(make_response(response, 400))

#     db.session.add(new_book)
#     db.session.commit()

#     return new_book.to_dict(), 201
# End from 07 Building an API -Refactoring Part 2

# 05 Building an API - Testing 
# This will cause the test to fail due to incorrect 
# @books_bp.get("")
# def get_all_books():
#     return make_response("I'm a teapot!", 418)

# @bp.get("")
# def get_all_books():
#     # 05 Building an API - More Flask Queries

#     # Method 1
#     # # check for title in the query params. 
#     # # If it's not present, the get() call will return None, a falsy value.
#     # title_param = request.args.get("title")
#     # if title_param:
#     #     # query = db.select(Book).where(Book.title == title_param).order_by(Book.id) # code that builds a query to filter by title
#     #     # But if we try to send a request looking for apple in the title, GET /books?title=apple, we won't get any results. This is 
#     #     # because the == operator is looking for an exact match, and none of our titles are exactly apple. 
#     #     # QLAlchemy filter by partial string and see what we find. Among the results, 
#     #     # we might learn that we can use the like() method to filter by a partial string.
#     #     # We might also encounter results describing the contains() method, 
#     #     # SELECT * FROM book WHERE title LIKE '%apple%' ORDER BY id;
#     #     # %: matches any characters,
#     #     # == will not work
#     #     # like(). contain() is case sensative
#     #     # Fortunately, PostgreSQL provides the ILIKE operator, which is case-insensitive
#     #     # query = db.select(Book).where(Book.title == title_param).order_by(Book.id) # code that builds a query to filter by title
#     #     # query = db.select(Book).where(Book.title.like(f"%{title_param}%")).order_by(Book.id)
#     #     query = db.select(Book).where(Book.title.ilike(f"%{title_param}%")).order_by(Book.id)

#     # else:
#     #     query = db.select(Book).order_by(Book.id)

#     # remaining code as before


#     # Method 2 # Reorganize
#     query = db.select(Book)

#     title_param = request.args.get("title")
#     if title_param:
#         query = query.where(Book.title.ilike(f"%{title_param}%"))

#     description_param = request.args.get("description")
#     if description_param:
#         query = query.where(Book.description.ilike(f"%{description_param}%"))

#     query = query.order_by(Book.id)

#     # END 05 Building an API - More Flask Queries

#     # query = db.select(Book).order_by(Book.id)
#     # we used the db.session object and called its scalars method to get a list of models. 
#     books = db.session.scalars(query)
#     # We could also write the line above as:
#     # books = db.session.execute(query).scalars()

#     books_response = []
#     for book in books:
#         # books_response.append(
#         #     {
#         #         "id": book.id,
#         #         "title": book.title,
#         #         "description": book.description
#         #     }
#         # )

#         ## Added from 07 Building an API - Refactoring Part 2
#         books_response.append(book.to_dict())
#         ## End from 07 Building an API - Refactoring Part 2
#     return books_response

################## 04 Building an API Read One Book
@bp.get("/<book_id>")
def get_one_book(book_id):
    # Added from 07 Building an API - Refactoring Part 3
    # book = validate_book(book_id)
    book = validate_model(Book, book_id)
    # End from 07 Building an API - Refactoring Part 3

    # Added from 07 Building an API - Refactoring Part 2
    return book.to_dict()
    # End from 07 Building an API - Refactoring Part 2
    
    # return {
    #     "id": book.id,
    #     "title": book.title,
    #     "description": book.description,
    # }

# # Added from 07 Building an API -Refactoring Part 3
# def validate_book(cls, book_id):
# # End from 07 Building an API -Refactoring Part 3
# # def validate_book(book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         # When book_id is not a number
#         response = {"message": f"Book {book_id} invalid"}
#         abort(make_response(response , 400))

#     # The query variable above receives a Select object representing the query for the data we are going to retrieve.
#     # Added from 07 Building an API -Refactoring Part 3
#     # query = db.select(Book).where(Book.id == book_id)
#     query = db.select(cls).where(cls.id == model_id)
#     # End from 07 Building an API -Refactoring Part 3

#     # scalar method: only one result
#     # db.session has another method we can use, scalar, which will only return one result rather than a list.
#     book = db.session.scalar(query)
    
#     # when we execute a query which selects no book records db.session.scalar(query) returns None! 
#     # When book_id does not exist in books
#     if not book:
#         response = {"message": f"Book {book_id} not found"}
#         abort(make_response(response, 404))

#     return book

# ################## END 04 Building an API Read One Book

###################  Added from 07 Building an API -Refactoring Part 3
# def validate_book(cls, book_id):
#     try:
#         book_id = int(book_id)
#     except:
#         response = {"message": f"{cls.__name__} {book_id} invalid"}
#         abort(make_response(response , 400))

#     query = db.select(cls).where(cls.id == book_id)
#     book = db.session.scalar(query)

#     if not book:
#         response = {"message": f"{cls.__name__} {book_id} not found"}
#         abort(make_response(response, 404))

#     return book

################### End from 07 Building an API -Refactoring Part 3

################## 04 Building an API Update

# HTTP method: PUT, endpoint: /<book_id>
@bp.put("/<book_id>")
def update_book(book_id):
    # Added from 07 Building an API - Refactoring Part 3
    # book = validate_book(book_id)
    book = validate_model(Book, book_id)
    # End from 07 Building an API - Refactoring Part 3

    # This endpoint relies on reading the HTTP request body. 
    # We'll use request.get_json() to parse the JSON body into a Python dictionary.
    request_body = request.get_json()

    book.title = request_body["title"]
    book.description = request_body["description"]
    # commit the change to the database, we'll execute db.session.commit().
    db.session.commit()

    # By using the Response constructor, we can manually create a Response object when we need detailed control over the contents and attributes of the endpoint's response.
    # use the keyword argument status to set a status code of 204 for our endpoint's response.
    # Since we construct our own response object we need to set the mimetype for our response to "application/json". 
    return Response(status=204, mimetype="application/json")

################## END 04 Building an API Update


################## 04 Building an API Delete

@bp.delete("/<book_id>")
def delete_book(book_id):
    # Added from 07 Building an API - Refactoring Part 3
    # book = validate_book(book_id)
    book = validate_model(Book, book_id)
    # End from 07 Building an API - Refactoring Part 3

    db.session.delete(book)
    db.session.commit()

    return Response(status=204, mimetype="application/json")

################## END 04 Building an API Delete


##################### Added 08 Building an API one-to-many Part 3

@bp.post("")
def create_book():
    request_body = request.get_json()
    return create_model(Book, request_body)

@bp.get("")
def get_all_books():
    return get_models_with_filters(Book, request.args)
##################### End 08 Building an API one-to-many Part 3