# from flask import Flask
# from .routes.book_routes import books_bp
# #from .routes.hello_world_routes import hello_world_bp
# # from app.routes.hello_world_routes import hello_world_bp



# # def create_app():
# #     app = Flask(__name__)

# #     # Register Blueprints here
# #     app.register_blueprint(hello_world_bp)

# #     return app

# def create_app():
#     app = Flask(__name__)

#     # Register Blueprints here
#     app.register_blueprint(books_bp)

#     return app

# # 03 Building an API
# from flask import Flask
# from .db import db, migrate # Imports the db and migrate objects we created previously
# from .models import book # Newly added import
# from .routes.book_routes import books_bp
# # Added from 06 Building an API -testing
# import os # This built-in module provides a way to read environment variables.
# # END Added from 06 Building an API -testing

# def create_app():
#     app = Flask(__name__)

#     # Configures the app to include two new SQLAlchemy settings
#     # We set app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] to False to hide a warning about a feature in SQLAlchemy that we won't be using.
#         # Disable track modifications to save system resources
#     # We set app.config['SQLALCHEMY_DATABASE_URI'] to the connection string for our database, hello_books_development
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#     # app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'
    
#     #### Added from 06 Building an API - Testing
#     app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')

#     if config:
#         # Merge `config` into the app's configuration
#         # to override the app's default settings
#         app.config.update(config)


#     #### End 06 Building an API - Testing

#     # Connects db and migrate to our Flask app, using the package's recommended syntax. 
#     # The app.config values must be set before this step, 
#     # since SQLAlchemy is going to look for those keys during this step.

#     # Initialize the SQLAlchemy extension with the Flask app
#     db.init_app(app)
#     # Initialize Flask-Migrate for handling database migrations
#     migrate.init_app(app, db)

#     # Register Blueprints here
#     app.register_blueprint(books_bp)

#     # Return the configured Flask application instance
#     return app

# # Added from 06 Building an API -testing
from flask import Flask
from .db import db, migrate
##################### Added from 10 Building an API many-to-many
from .models import book, author, genre, book_genre

# Added from 07 Building an API -Refactoring Part 3
# Using Alias
from .routes.book_routes import bp as books_bp

##################### Added from 08 Building an API one-to-many Part 1
from .routes.author_routes import bp as authors_bp

##################### Added from 10 Building an API many-to-many
from .routes.genre_routes import bp as genres_bp


# Method 2
# from .routes import book_routes
# End from 07 Building an API -Refactoring Part 3

import os

# We have called the new parameter config which should receive a dictionary of configuration settings. 
# It has a default value of None, making the parameter optional.
def create_app(config=None):
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # This syntax gets an environment variable by the name passed in to the get(...) method.
    # SQLALCHEMY_DATABASE_URI': This is the exact name of the development database environment variable we defined in .env. 
    # By default, app.config['SQLALCHEMY_DATABASE_URI'] will be set to the value we gave this variable in the .env file.
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI') 


    # if config is truthy (is not None or empty), 
    # that means we want to merge the passed configuration config with our default settings in app.config. 
    # We do this to overwrite defaults-like the database connection string-to set up our app for different environments.
    if config:
        # Merge `config` into the app's configuration
        # to override the app's default settings

        # Use the contents of the dictionary passed to update(...) to add or overwrite key/value pairs in the app settings dictionary app.config
        app.config.update(config)

    db.init_app(app)
    migrate.init_app(app, db)

    ##################### Added from 07 Building an API -Refactoring Part 3
    # Register Blueprints here
    app.register_blueprint(books_bp)

    ##################### Added from 08 Building an API one-to-many Part 1
    app.register_blueprint(authors_bp)
    ##################### End from 08 Building an API one-to-many Part 1
    # Method 2
    # <module_name>.<symbol_name> to access a specific symbol from the module. 
    # Register Blueprints here
    # app.register_blueprint(book_routes.bp)
    ####################### End from 07 Building an API -Refactoring Part 3
    

    ##################### Added from 10 Building an API many-to-many
    app.register_blueprint(genres_bp)


    return app
# # END Added from 06 Building an API -testing