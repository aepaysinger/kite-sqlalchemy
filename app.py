from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Book


engine = create_engine("sqlite:///books-collection.db")
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()


# operate on the Read Operation
@app.route("/")
@app.route("/books")
def showBooks():
    books = session.query(Book).all()
    return render_template("books.html", books=books)


# Create new book and save it in database
@app.route("/books/new/", methods=["GET", "POST"])
def newBook():
    if request.method == "POST":
        newBook = Book(
            title=request.form["name"],
            author=request.form["author"],
            genre=request.form["genre"],
        )
        session.add(newBook)
        session.commit()
        return redirect(url_for("showBooks"))
    else:
        return render_template("newBook.html")


# update books and save in database
@app.route("/books/<int:book_id>/edit/", methods=["GET", "POST"])
def editBook(book_id):
    editedBook = session.query(Book).filter_by(id=book_id).one()
    if request.method == "POST":
        if request.form["name"]:
            editedBook.title = request.form["name"]
            return redirect(url_for("showBooks"))
    else:
        return render_template("editBook.html", book=editedBook)


# delete book
@app.route("/books/<int:book_id>/delete", methods=["GET"])
def deleteBook(book_id):
    bookToDelete = session.query(Book).filter_by(id=book_id).one()
    session.delete(bookToDelete)
    session.commit()
    return redirect(url_for("showBooks", book_id=book_id))


if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=4996)
