# Import the SQLAlchemy parts
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create a database URL for SQLAlchemy
#mydb is the name of the db file
SQLALCHEMY_DATABASE_URL = "sqlite:///./mydb.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# Create the SQLAlchemy engine
engine = create_engine(
    # "check_same_thread" this argument is needed because we are using SQLite
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()