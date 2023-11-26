from models.user import db
from flask import jsonify

# Define the Book model
class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    author = db.Column(db.String(255), nullable=False)
    genre = db.Column(db.String(255), nullable=False)
    isbn = db.Column(db.String(20), unique=True, nullable=False)
    year = db.Column(db.Integer)
    synopsis = db.Column(db.Text)
    copiesAvailable = db.Column(db.Integer)
    dateAdded = db.Column(db.DateTime)
    dateModified = db.Column(db.DateTime)

    def __init__(self, title, author, genre, isbn, year, synopsis, copiesAvailable, dateAdded, dateModified):
        self.title = title
        self.author = author
        self.genre = genre
        self.isbn = isbn
        self.year = year
        self.synopsis = synopsis
        self.copiesAvailable = copiesAvailable
        self.dateAdded = dateAdded
        self.dateModified = dateModified

    def to_json(self):
        return jsonify({
            'title': self.title,
            'author': self.author,
            'genre': self.genre,
            'isbn': self.isbn,
            'year': self.year,
            'synopsis': self.synopsis,
            'copiesAvailable': self.copiesAvailable,
            'dateAdded': self.dateAdded,
        })

    def insert(book):
        db.session.add(book)
        db.session.commit()

    def update():
        db.session.commit()

    def delete(book):
        db.session.delete(book)
        db.session.commit()

    def bookList():
        books = db.paginate()
        return books
