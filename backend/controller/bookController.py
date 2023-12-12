from models.book import Book
from flask import jsonify, request
from datetime import datetime
# from controller.userController import UserController

# Define the Book model controller
class BookController():
    def count():
        """
        Counts the total number of books in the library.

        Returns:
            int: The total number of books.
        """
        count = Book.query.count()
        return count

    def insert():
        """
        Inserts a new book into the library.

        Returns:
            tuple: A tuple containing the success status, HTTP status code, and a message.
        """

        # get form data in json format
        data = request.get_json()
        title = data['title']
        author = data['author']
        genre = data['genre']
        isbn = data['isbn']
        years = data['year']
        synopsis = data['synopsis']
        copiesAvailable = data['copiesAvailable']
        dateAdded = datetime.utcnow()
        dateModified = datetime.utcnow()
        # createdByUser = UserController.user
        # createdByUserRole = UserController.role
        # converting the date from a string to a date object
        year = int(years)
        copiesAvailable = int(copiesAvailable)

        if title is None:
            return jsonify({"success": False, "status": 400, "message": "Title is required"}), 400
        if author is None:
            return jsonify({"success": False, "status": 400, "message": "Author is required"}), 400
        if genre is None:
            return jsonify({"success": False, "status": 400, "message": "Genre is required"}), 400
        if isbn is None:
            return jsonify({"success": False, "status": 400, "message": "Isbn is required"}), 400
        if year is None:
            return jsonify({"success": False, "status": 400, "message": "Year is required"}), 400
        if synopsis is None:
            return jsonify({"success": False, "status": 400, "message": "Synopsis is required"}), 400
        if copiesAvailable is None:
            return jsonify({"success": False, "status": 400, "message": "Copies is required"}), 400

        # checking if the book is in the database
        if Book.query.filter(Book.title == title).all() or Book.query.filter(Book.isbn == isbn).all():
            return jsonify({"success": False, "status": 409, "message": "The book is already in the Library"}), 409
        else:
            # adding book to the database
            book = Book(
                title=title,
                author=author,
                genre=genre,
                isbn=isbn,
                year=year,
                synopsis=synopsis,
                copiesAvailable=copiesAvailable,
                dateAdded=dateAdded,
                dateModified=dateModified,
                # createdByUser=createdByUser,
                # createdByUserRole=createdByUserRole
            )
            Book.insert(book)
            return jsonify({"success": True, "status": 201, "message": "The book has been added to the Library"}), 201

    def delete():
        """
        Deletes a book from the library.

        Returns:
            tuple: A tuple containing the success status, HTTP status code, and a message.
        """

        # get the title or isbn from the request body
        data = request.get_json()
        info = data['isbnOrTitle']
        try:
            data = Book.query.filter_by(title=info).first(
            ) or Book.query.filter_by(isbn=info).first()
            Book.delete(data)
            return jsonify({"success": True, "status": 201, "message": "The book has been deleted"}), 201
        except:
            count = BookController.count()
            if count == 0:
                return jsonify({"success": True, "status": 204, "message": "There are no books in the library's database by the requested title or Isbn"}), 404
            return jsonify({"success": False, "status": 404, "message": "The book is not in the Library by the title or isbn of {}".format(info)}), 404

    def searchAll():
        """
        Searches for books in the library based on a query.

        Returns:
            tuple: A tuple containing the success status, HTTP status code, a list of books, and the count of books.
        """

        # Get response in json
        info = request.args.get('query')
        # Query the book by the title, author, or genre
        books = Book.query.filter(Book.title.ilike(f'%{info}%') | Book.author.ilike(
            f'%{info}%') | Book.isbn.ilike(f'%{info}%') | Book.year.ilike(f'%{info}%')).all()
        # checking the requested book is in the database
        if not books:
            count = BookController.count()
            if count == 0:
                return jsonify({"success": False, "status": 204, "message": "There are no books found in the library's database"}), 404
            return jsonify({"success": False, "status": 404, "message": "There are no books in the library by the requested search term {}".format(info)}), 404
        books_json = [{"id": book.id, "title": book.title, "author": book.author, "genre": book.genre, "isbn": book.isbn,
                       "year": str(book.year), "synopsis": book.synopsis, "copiesAvailable": book.copiesAvailable, "dateAdded": book.dateAdded, "dateModifide": book.dateModified} for book in books]
        return jsonify({"success": True, "status": 200, "message": books_json, 'count': len(books_json)}), 200

    def search():
        """
        Searches for books in the library based on a query.

        Returns:
            tuple: A tuple containing the success status, HTTP status code, a list of books, and the count of books.
        """

        if request.args.get(''):
            return jsonify({"success": False, "status": 400, "message": "Please provide a search term"}), 400
        data = request.args.get('query')
        books = Book.query.filter(Book.title.ilike(f'%{data}%') | Book.author.ilike(
            f'%{data}%') | Book.genre.ilike(f'%{data}%')).all()
        if not books:
            count = BookController.count()
            if count == 0:
                return jsonify({"success": False, "status": 204, "message": "There are no books found in the library's database"}), 404
            return jsonify({"success": False, "status": 404, "message": "There are no books in the library by the requested search term {}".format(data)}), 404
        books_json = [{"id": book.id, "title": book.title, "author": book.author, "genre": book.genre, "isbn": book.isbn,
                       "year": str(book.year), "synopsis": book.synopsis, "copiesAvailable": book.copiesAvailable, "dateAdded": book.dateAdded, "dateModifide": book.dateModified} for book in books]
        return jsonify({"success": True, "status": 200, "message": books_json, 'count': len(books_json)}), 200

    def listAll():
        """
        Lists all the books in the library.

        Returns:
            tuple: A tuple containing the success status, HTTP status code, a list of books, and the count of books.
        """

        # Query all books
        books = Book.query.all()
        # check if there are no books
        if not books:
            count = BookController.count()
            if count == 0:
                return jsonify({"success": False, "status": 204, "message": "There are no books found in the library's database"}), 204
            return jsonify({"success": False, "status": 404, "message": "Books not found"}), 404
        # Convert the list of books to a JSON format
        books_json = [{"id": book.id, "title": book.title, "author": book.author, "genre": book.genre, "isbn": book.isbn,
                       "year": str(book.year), "synopsis": book.synopsis, "copiesAvailable": book.copiesAvailable, "dateAdded": book.dateAdded, "dateModifide": book.dateModified} for book in books]
        # Return the list as a JSON response
        return jsonify({"success": True, "status": 200, 'message': books_json, 'count': len(books_json)}), 200

    def listAllCategory():
        """
        Lists all the books in the library based on a specific genre.

        Returns:
            tuple: A tuple containing the success status, HTTP status code, a list of books, and the count of books.
        """

        # Get response in json
        genres = request.args.get('genre')
        # Query the book by the genre
        books = Book.query.filter(Book.genre.ilike(f'{genres}')).all()
        # checking the requested category is in the database
        if not books:
            count = BookController.count()
            if count == 0:
                return jsonify({"success": False, "status": 204, "message": "There are no books found in the library's database"}), 404
            return jsonify({"success": False, "status": 404, "message": "There are no books in the library for the requested category of {}".format(genres)}), 404
        # Convert the list of books to a JSON format
        books_json = [{"id": book.id, "title": book.title, "author": book.author, "genre": book.genre, "isbn": book.isbn,
                       "year": str(book.year), "synopsis": book.synopsis, "copiesAvailable": book.copiesAvailable, "dateAdded": book.dateAdded, "dateModifide": book.dateModified} for book in books]
        if len(books_json) == 0:
            return jsonify({"success": False, "status": 404, "message": "There are no books in the library for the requested category of {}".format(genres)}), 404
        else:
            # Return the list as a JSON response
            return jsonify({"success": True, "status": 200, "message": books_json, 'count': len(books_json)}), 200

    def countCategory():
        """
        Counts the number of unique book categories in the library.

        Returns:
            int: The number of unique book categories.
        """
        bookCategories = set()
        books = Book.query.all()
        for book in books:
            bookCategories.add(book.genre)
        return len(bookCategories)

    def bookCategory():
        """
        Retrieves a list of all the book categories in the library.

        Returns:
            list: A list of book categories.
        """
        bookCategories = set()
        books = Book.query.all()
        for book in books:
            bookCategories.add(book.genre)
        return list(bookCategories)

    def updates():
        """
        Updates the details of a book in the library.

        Returns:
            tuple: A tuple containing the success status, HTTP status code, and a message.
        """
        data = request.get_json()
        title = data['title']
        author = data['author']
        genre = data['genre']
        isbn = data['isbn']
        years = data['year']
        synopsis = data['synopsis']
        copiesAvailable = data['copiesAvailable']
        dateModified = datetime.utcnow()
        # modifiedBy = UserController.user
        # modifiedByUserRole = UserController.role
        # converting the date from a string to a date object
        year = int(years)
        copiesAvailable = int(copiesAvailable)
        # checking if the book is in the database
        book = Book.query.filter_by(title=title).first()
        bookCreatedDate = book.dateAdded

        if book:
            book.title = title
            book.author = author
            book.genre = genre
            book.isbn = isbn
            book.year = year
            book.synopsis = synopsis
            book.copiesAvailable = copiesAvailable
            book.dateAdded = bookCreatedDate
            book.dateModified = dateModified
            # book.modifiedBy = modifiedBy
            # book.modifiedByUserRole = modifiedByUserRole
            Book.update()
            return jsonify({"success": True, "status": 201, "message": "The book has been updated in the Library"}), 201
        else:
            return jsonify({"success": False, "status": 404, "message": "The book is not in the Library by the title of {}".format(book)}), 404
