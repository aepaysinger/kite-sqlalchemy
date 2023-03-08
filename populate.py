from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Book, Base

engine = create_engine('sqlite:///books-collection.db')

Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)

session = DBSession()

bookOne = Book(title="The Bell Jar", author="Sylvia Plath", genre="roman a clef")
session.add(bookOne)
session.commit()