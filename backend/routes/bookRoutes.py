from controller.bookController import BookController
from flask import jsonify

class BookRoutes:
    '''
    Defining routes to interact with books
    '''

    @staticmethod
    def listAllBycategory():
        '''
        Query all books by category and return the list as a JSON response.
        '''
        books = BookController.listAllCategory()
        return books

    @staticmethod
    def get_book_list():
        '''
        Query all books and return the list as a JSON response.
        '''
        books = BookController.listAll()
        return books

    @staticmethod
    def insert_book():
        '''
        Insert a book into the database and return a response.
        '''
        insertBook = BookController.insert()
        return insertBook

    @staticmethod
    def delete():
        '''
        Query the book by the title or isbn and return a response.
        '''
        book = BookController.delete()
        return book

    @staticmethod
    def searchBooks():
        '''
        Query the book by the title, author, or genre and return the book.
        '''
        search = BookController.search()
        return search

    @staticmethod
    def updateBook():
        '''
        Update a book in the database and return a response.
        '''
        return BookController.updates()

    @staticmethod
    def searchAll():
        '''
        Query the book by the title, author, or genre and return the book.
        '''
        search = BookController.searchAll()
        return search