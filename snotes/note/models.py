
from snotes.database import db
from sqlalchemy import Column

class Note(db.Model):
    id=Column(db.Integer, primary_key=True)

