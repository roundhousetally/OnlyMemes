from sqlalchemy.ext.declarative import declarative_base
from classes.storage import Storage

Base = declarative_base()
storage = Storage()

storage.load()
