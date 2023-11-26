from flask import jsonify, request
from controller.bookController import BookController
from controller.userController import UserController

class Routes:
        '''
        The initial route for the application to test if the application is running
        '''
        def index():
                # Return a welcome message to the user when they visit the root route
                return jsonify({"success": True, "status": 200, "message": 'Welcome to the books library system' }), 200

        def status():
                # Return a status message to the user when they visit the status route confirming that the application is running
                return jsonify({"success": True, "status": 200, "mesage": [{'request': True, 'response': True}, dict(request.headers)] }), 200

        def stats():
                bookCount = BookController.count()
                bookCategoryCount = BookController.countCategory()
                bookCategory = BookController.bookCategory()
                userCount = UserController.count()
                verifiedUserCount = UserController.countVerified()
                unverifiedUserCount = UserController.countUnverified()
                # Return a status message to the user when they visit the status route confirming that the application is running
                return jsonify({ "success": True, "status": 200, "message":\
                        [{'book': [{"total": bookCount, "countByCategories": bookCategoryCount, 'categories': bookCategory}]},\
                        {'user':[{"total": userCount, "verified": verifiedUserCount, "unverified": unverifiedUserCount}]}]\
                                }), 200
