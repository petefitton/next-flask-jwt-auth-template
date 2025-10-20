from . import db
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    
    id: int = db.Column(db.Integer, primary_key=True)
    username: str = db.Column(db.String, nullable=False)
    pw_hash: str = db.Column(db.String, nullable=False)
