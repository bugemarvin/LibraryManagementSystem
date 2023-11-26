from controller.bookController import BookController
from flask import jsonify

class BookRoutes:
    '''
    Defining routes to interact with books
    '''
    def listAllBycategory():
        # Query all books by category
        books = BookController.listAllCategory()
        # Return the list as a JSON response
        return books

    def get_book_list():
        # Query all books
        books = BookController.listAll()
        # Return the list as a JSON response
        return books

    def insert_book():
        # Insert a book into the database
        insertBook = BookController.insert()
        # return a response
        return insertBook

    def delete():
        # Query the book by the title or isbn
        book = BookController.delete()
        # Return a response
        return book

    def searchBooks():
        # Query the book by the title, author or genre and return the book
        search = BookController.search()
        # Return a response
        return search

    def updateBook():
        return BookController.updates()
    
    def searchAll():
        # Query the book by the title, author or genre and return the book
        search = BookController.searchAll()
        # Return a response
        return search