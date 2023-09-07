
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



#define sqlite connection url
SQLALCHEMY_DATABASE_URL = "sqlite:///./my_database.db"

# create new engine instance 
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# create sessionmaker 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
#create the database tables on app startup or reload
Base.metadata.create_all(bind=engine)


def get_db(self):
    self.db = self.SessionLocal()
    try:
        yield self.db
    finally:
        self.db.close()
            