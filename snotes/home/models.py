
from enum import Enum, unique

from sqlalchemy import Column, Enum as SqlEnum
from flask.ext.login import UserMixin

from snotes.database import db
from snotes.models import RoleEnum, ColumnEnum

class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = Column(db.Integer, primary_key=True)
    username = Column(db.String(20), nullable=False, unique=True)
    password = Column(db.String(32), nullable=False)
    role = Column(ColumnEnum(RoleEnum)) 
    atime = Column(db.Integer, nullable=False)
    mtime = Column(db.Integer, nullable=False)

