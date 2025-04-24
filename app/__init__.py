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

# 03 Building an API
from flask import Flask
from .db import db, migrate # Imports the db and migrate objects we created previously
from .models import book # Newly added import
from .routes.book_routes import books_bp


def create_app():
    app = Flask(__name__)

    # Configures the app to include two new SQLAlchemy settings
    # We set app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] to False to hide a warning about a feature in SQLAlchemy that we won't be using.
        # Disable track modifications to save system resources
    # We set app.config['SQLALCHEMY_DATABASE_URI'] to the connection string for our database, hello_books_development
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

    # Connects db and migrate to our Flask app, using the package's recommended syntax. 
    # The app.config values must be set before this step, 
    # since SQLAlchemy is going to look for those keys during this step.

    # Initialize the SQLAlchemy extension with the Flask app
    db.init_app(app)
    # Initialize Flask-Migrate for handling database migrations
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(books_bp)

    # Return the configured Flask application instance
    return app