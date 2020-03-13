from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Sequence
from sqlalchemy.orm import relationship
from application.database import Base

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    mobile = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)
    city = Column(String(255), nullable=False)
    postcode = Column(String(255), nullable=False)
    course = Column(String(255), nullable=False)
    is_guest = Column(Boolean(), nullable=False)
    is_admin = Column(Boolean(), nullable=False)

    # add the foreign keys
    event = relationship("Event")
    booking = relationship("Booking")

    autoload=True

    def __repr__(self):
        return str(self.__dict__)