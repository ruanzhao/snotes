
from sqlalchemy import Column
from flask.ext.login import UserMixin

from snotes.database import db


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(db.Integer, primary_key=True)
    username = Column(db.String(20), nullable=False, unique=True)
