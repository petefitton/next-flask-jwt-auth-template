from . import db
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from flask_sqlalchemy.model import Model
else:
    Model = db.Model

class User(Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    pw_hash = db.Column(db.String, nullable=False)