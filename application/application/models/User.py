from sqlalchemy import Column, Integer, String
from application.database import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True)
    email = Column(String(120), unique=True)

    def __repr__(self):
        return '<User %r>' % (self.name)