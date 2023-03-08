import sys

from sqlalchemy import Column, ForeignKey, Integer, String

from sqlalchemy.orm import declarative_base

from sqlalchemy import create_engine

Base = declarative_base()


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    author = Column(String(250), nullable=False)
    genre = Column(String(250))


engine = create_engine("sqlite:///books-collection.db")

Base.metadata.create_all(engine)
