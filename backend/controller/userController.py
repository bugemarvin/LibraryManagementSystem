from flask import request, jsonify
from datetime import datetime
from models.user import User

class UserController:
        def count():
                count = User.query.count()
                return count

        def getUserByStatus():
                pass

        def getUserByRole():
                pass

        def getUser():
                pass

        def getConfirmUser():
                pass

        def registerUser():
                pass

        def loginUser():
                pass

        def verifyUser():
                pass

        def countVerified():
                user = User.query.filter(User.confirmed == True).count()
                return user

        def countUnverified():
                user = User.query.filter(User.confirmed == False).count()
                return user