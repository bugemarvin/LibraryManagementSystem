from flask import request, jsonify
from models.user import User
from utils.token import Token
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_jwt_extended import get_jwt_identity, JWTManager

jwt = JWTManager()

class UserController:
        def count():
                count = User.query.count()
                return count

        def register():
                data = request.get_json()
                firstName = data['fname']
                middleName = data['mname']
                lastName = data['lname']
                emailAddress = data['email']
                phoneNumber = data['phone']
                passwords = data['password']
                role = User.role
                dateCreated = datetime.utcnow()
                dateModified = User.dateModified
                location = User.location
                status = User.status
                confirmed = User.confirmed
                confirmedOn = User.confirmedOn
                getToken = emailAddress if emailAddress else phoneNumber
                token = Token.generateToken(getToken)
                photos = User.photos
                password = generate_password_hash(passwords)
                if not firstName:
                        return jsonify({'sucess': True, 'status': 400, 'message': 'First name is required'}), 400
                if not lastName:
                        return jsonify({'sucess': True, 'status': 400, 'message': 'Last name is required'}), 400
                if not emailAddress:
                        return jsonify({'sucess': True, 'status': 400, 'message': 'Email address is required'}), 400
                if not password:
                        return jsonify({'sucess': True, 'status': 400, 'message': 'Password is required'}), 400

                user = User(
                        firstName=firstName,
                        middleName=middleName,
                        lastName=lastName,
                        emailAddress=emailAddress,
                        phoneNumber=phoneNumber,
                        password=password,
                        role=role,
                        dateCreated=dateCreated,
                        dateModified=dateModified,
                        location=location,
                        status=status,
                        confirmed=confirmed,
                        confirmedOn=confirmedOn,
                        token=token,
                        photos=photos
                )

                if user is None:
                        return jsonify({'sucess': True, 'status': 404, 'message': 'User details cannot be blank'}), 404

                if User.query.filter_by(emailAddress=emailAddress).all() or User.query.filter_by(phoneNumber=phoneNumber).all():
                        return jsonify({'sucess': True, 'status': 409, 'message': 'User already exists'}), 409

                User.addUser(user)
                return jsonify({'sucess': True, 'status': 201, 'message': 'User created successfully'}), 201

        def login():
                data = request.get_json()
                username = data['username']
                passwords = data['password']
                user = User.query.filter_by(emailAddress=username).first() or User.query.filter_by(phoneNumber=username).first()
                dbpasswort = user.password
                password = check_password_hash(dbpasswort, passwords)
                if not user or not password:
                        return jsonify({'sucess': True, 'status': 404, 'message': 'User does not exist'}), 404
                getToken = user.emailAddress if user.emailAddress else user.phoneNumber
                token = Token.generateToken(getToken)
                user.token = token
                User.update()
                return jsonify({'sucess': True, 'status': 200, 'message': 'User logged in successfully', 'token': token}), 200

        def countVerified():
                user = User.query.filter_by(confirmed=True).count()
                return user

        def countUnverified():
                user = User.query.filter_by(confirmed=False).count()
                return user

        def token():
                token = get_jwt_identity()
                if not token:
                        return jsonify({'sucess': False, 'status': 401, 'message': 'Unauthorized'}), 401
                return token

        def getUsers():
                token = UserController.token()
                user = User.query.filter_by(emailAddress=token).first() or User.query.filter_by(phoneNumber=token).first()
                user_json = {
                                'id': user.id,
                                'firstName': user.firstName,
                                'middleName': user.middleName,
                                'lastName': user.lastName,
                                'emailAddress': user.emailAddress,
                                'phoneNumber': user.phoneNumber,
                                'role': user.role,
                                'dateCreated': user.dateCreated,
                                'dateModified': user.dateModified,
                                'location': user.location,
                                'status': user.status,
                                'confirmed': user.confirmed,
                                'confirmedOn': user.confirmedOn,
                                'token': user.token,
                                'photos': user.photos
                                }
                return jsonify({'sucess': True, 'status': 200, 'user': user_json}), 200

        def logout():
                token = UserController.token()
                return jsonify({'sucess': True, 'status': 200, 'message': 'User logged out successfully', 'user': users}), 200