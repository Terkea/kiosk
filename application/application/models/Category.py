from sqlalchemy import Column, Integer, String
from application.database import Base

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)

    def __repr__(self):
        return str(self.__dict__)