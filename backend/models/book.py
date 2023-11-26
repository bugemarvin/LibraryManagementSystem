from models.user import db
from flask import jsonify


class Book(db.Model):
    """
    Represents a book in the library management system.
    """

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
        """
        Initializes a new instance of the Book class.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            genre (str): The genre of the book.
            isbn (str): The ISBN of the book.
            year (int): The year the book was published.
            synopsis (str): The synopsis of the book.
            copiesAvailable (int): The number of copies available.
            dateAdded (datetime): The date the book was added to the system.
            dateModified (datetime): The date the book was last modified.
        """
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
        """
        Converts the Book object to a JSON representation.

        Returns:
            dict: A dictionary representing the Book object.
        """
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
        """
        Inserts a book into the database.

        Args:
            book (Book): The book to be inserted.
        """
        db.session.add(book)
        db.session.commit()

    def update():
        """
        Updates the book in the database.
        """
        db.session.commit()

    def delete(book):
        """
        Deletes a book from the database.

        Args:
            book (Book): The book to be deleted.
        """
        db.session.delete(book)
        db.session.commit()

    def bookList():
        """
        Retrieves a list of books from the database.

        Returns:
            list: A list of books.
        """
        books = db.paginate()
        return books
