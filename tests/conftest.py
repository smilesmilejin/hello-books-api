import pytest
from app import create_app # We should import create_app in order to set up our test configuration for running the tests
from app.db import db
from flask.signals import request_finished # We use the @request_finished decorator to create a new database session after a request as described below.
from dotenv import load_dotenv # We'll use load_dotenv to manually load the contents of our .env into our environment variables.
import os # As we did in the root __init__.py file, we'll use os to read our environment variables.

load_dotenv() # Before we can use our environment variables, we need to invoke the load_dotenv function that we imported.

@pytest.fixture # We'll create and use a pytest fixture named app, which will be used in our client fixture (defined later)
def app():
    # We're creating a dictionary holding the configuration for our testing environment to pass to create_app.
    # We're creating a key TESTING with a value of True which will be added to the app.config in our __init__.py's create_app function.
    # In our test configuration, we're creating a key SQLALCHEMY_DATABASE_URI with a value of os.environ.get('SQLALCHEMY_TEST_DATABASE_URI'). '
    # 'This will be used to overwrite the default value of SQLALCHEMY_DATABASE_URI in our __init__.py's create_app function to ensure that our tests run against the test database we created hello_books_test.
    test_config = {
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": os.environ.get('SQLALCHEMY_TEST_DATABASE_URI')
    }
    # We're passing in our test configuration object test_config when creating our test instance of our application. The settings in test_config will be merged into the default configuration app.config inside the create_app function.
    app = create_app(test_config)

    # This decorator indicates that the function defined below, expire_session, will be invoked after any request is completed
    @request_finished.connect_via(app)
    def expire_session(sender, response, **extra):
        # Without this line, when we test that an update was made to a record following a put request, the test will only look at the in-memory copy of the updated record. By adding db.session.remove(), we make sure the test checks that the update was persisted in the database.
        db.session.remove()

    # This syntax designates that the following code should have an application context. This lets various functionality in Flask determine what the current running app is. 
    # This is particularly important when accessing the database associated with the app.
    with app.app_context():
        # At the start of each test, this code recreates the tables needed for our models.
        db.create_all()
        # This fixture suspends here, returning the app for use in tests or other fixtures. The lines after this yield statement will run after the test using the app has been completed.
        yield app

    with app.app_context():
        # After the test runs, this code specifies that we should drop all of the tables, deleting any data that was created during the test.
        db.drop_all()

# Set up a second test fixture
@pytest.fixture
# This fixture is named client. It will request the existing app fixture to run, first.
def client(app):
    # The responsibility of this fixture is to make a test client, which is an object able to simulate a client making HTTP requests.
    return app.test_client()
