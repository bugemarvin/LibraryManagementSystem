from flask import jsonify, request
from controller.bookController import BookController
from controller.userController import UserController


class Routes:
    '''
    The initial route for the application to test if the application is running
    '''
    @staticmethod
    def index():
        """
        Returns a JSON response with a welcome message for the books library system.

        :return: JSON response with success status, HTTP status code, and welcome message.
        """
        return jsonify({"success": True, "status": 200, "message": 'Welcome to the books library system'}), 200

    @staticmethod
    def status():
        """
        Return a status message to the user when they visit the status route confirming that the application is running.

        Returns:
                A JSON response containing a success message, status code, and request headers.
        """
        return jsonify({"success": True, "status": 200, "mesage": [{'request': True, 'response': True}, dict(request.headers)]}), 200

    @staticmethod
    def stats():
        """
        Returns the statistics of the library management system.

        Returns:
                A JSON response containing the following information:
                - Total number of books in the library
                - Number of books categorized by category
                - List of book categories
                - Total number of users in the system
                - Number of verified users
                - Number of unverified users
        """
        bookCount = BookController.count()
        bookCategoryCount = BookController.countCategory()
        bookCategory = BookController.bookCategory()
        userCount = UserController.count()
        verifiedUserCount = UserController.countVerified()
        unverifiedUserCount = UserController.countUnverified()
        # Return a status message to the user when they visit the status route confirming that the application is running
        return jsonify({
            "success": True,
            "status": 200,
            "message": [
                {
                    'book': [
                        {
                            "total": bookCount,
                            "countByCategories": bookCategoryCount,
                            'categories': bookCategory
                        }
                    ]
                },
                {
                    'user': [
                        {
                            "total": userCount,
                            "verified": verifiedUserCount,
                            "unverified": unverifiedUserCount
                        }
                    ]
                }
            ]
        }), 200
