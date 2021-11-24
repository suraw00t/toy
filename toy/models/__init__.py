from flask_mongoengine import MongoEngine
from .users import User
from .stocks import Item, Stock, Status

__all__ = ["User"]

db = MongoEngine()


def init_db(app):
    db.init_app(app)
