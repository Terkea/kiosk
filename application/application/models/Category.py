from sqlalchemy import Column, Integer, String, Sequence
from application.database import Base

class Category(Base):
    __tablename__ = 'category'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    name = Column(String(255), nullable=False)

    autoload = True
    
    def __repr__(self):
        return str(self.__dict__)