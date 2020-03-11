from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('oracle+cx_oracle://terkea:test@127.0.0.1:1521/?service_name=ORCLCDB.LOCALDOMAIN',
 convert_unicode=True, max_identifier_length=128)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    # import all modules here that might define models so that
    # they will be registered properly on the metadata.  Otherwise
    # you will have to import them first before calling init_db()
    from application.models import User
    from application.models import Category
    from application.models import Event
    from application.models import Booking
    Base.metadata.create_all(bind=engine)