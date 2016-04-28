
from flask import Blueprint

from .models import Note

note = Blueprint('note', __name__)

@note.route('/')
def list():
    return "note/list"
