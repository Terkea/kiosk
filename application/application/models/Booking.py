import datetime

from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, DateTime
from application.database import Base

class Booking(Base):
    __tablename__ = 'booking'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    event_id = Column(Integer, ForeignKey('event.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    datetime = Column(DateTime, default=datetime.datetime.utcnow)

    autoload = True
    
    def __repr__(self):
        return str(self.__dict__)