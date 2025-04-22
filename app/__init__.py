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
from .db import db, migrate
from .models import book # Newly added import
from .routes.book_routes import books_bp


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:postgres@localhost:5432/hello_books_development'

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    app.register_blueprint(books_bp)

    return app