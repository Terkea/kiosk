from sqlalchemy import Column, Integer, String, ForeignKey
from application.database import Base

class Booking(Base):
    __tablename__ = 'booking'
    id = Column(Integer, primary_key=True)
    event_id = Column(Integer, ForeignKey('event.id'), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    datetime = Column(String(255), unique=True, nullable=False)

    def __repr__(self):
        return str(self.__dict__)