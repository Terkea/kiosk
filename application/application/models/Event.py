from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, Text, Boolean
from sqlalchemy.orm import relationship
from application.database import Base

class Event(Base):
    __tablename__ = 'event'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)
    name = Column(String(255), nullable=False)
    venue = Column(String(255), nullable=False)
    datetime = Column(String(255), nullable=False)
    entry_price = Column(String(255), nullable=False)
    description = Column(Text(), nullable=False)
    event_type = Column(String(255), nullable=False)
    slots_available = Column(String(255), nullable=False)
    picture = Column(String(255))
    is_visible = Column(Boolean(), default=True)

    # add the foreign keys
    booking = relationship("Booking", backref="event")

    autoload = True
    
    def __repr__(self):
        return str(self.__dict__)