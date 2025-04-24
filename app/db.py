# 03 Building an API
# First we import SQLAlchemy, Migrate, and our newly created Base class
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models.base import Base

# , we create an instance of SQLAlchemy, 
# which we will call db, and pass it our Base class as the constructor argument. 
db = SQLAlchemy(model_class=Base)
# we make an instance of Migrate. We will not directly interact with this object much, 
# but this object will be used by the application to update our database tables when we make changes to our model class's attributes.
migrate = Migrate()