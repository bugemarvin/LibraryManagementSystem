from flask_sqlalchemy import SQLAlchemy
import uuid
from datetime import datetime

# initialize the database
db = SQLAlchemy()


class User(db.Model):
    """
    Represents a user in the library management system.

    Attributes:
            id (int): The unique identifier for the user.
            firstName (str): The first name of the user.
            middleName (str): The middle name of the user.
            lastName (str): The last name of the user.
            emailAddress (str): The email address of the user.
            phoneNumber (str): The phone number of the user.
            password (str): The password of the user.
            role (str): The role of the user.
            dateCreated (datetime): The date and time when the user was created.
            dateModified (datetime): The date and time when the user was last modified.
            location (str): The location of the user.
            status (str): The status of the user.
            confirmed (bool): Indicates if the user is confirmed.
            confirmedOn (datetime): The date and time when the user was confirmed.
            token (str): The token associated with the user.
            photos (str): The photos of the user.
    """

    __tablename__ = 'user'
    id = db.Column(db.String(255), primary_key=True, default=uuid.uuid4().hex, unique=True)
    firstName = db.Column(db.String(255), nullable=False)
    middleName = db.Column(db.String(255))
    lastName = db.Column(db.String(255), nullable=False)
    emailAddress = db.Column(db.String(255), nullable=False, unique=True)
    phoneNumber = db.Column(db.String(35), unique=True)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), nullable=False, server_default='user', default='user')
    dateCreated = db.Column(db.DateTime)
    dateModified = db.Column(db.DateTime, nullable=False, default=0, onupdate=datetime.utcnow())
    location = db.Column(db.String(255), nullable=False, default=0)
    status = db.Column(db.String(255), nullable=False, server_default='inactive', default='inactive')
    confirmed = db.Column(db.Boolean, nullable=False, default=0)
    confirmedOn = db.Column(db.DateTime, nullable=False, default=0, onupdate=datetime.utcnow())
    token = db.Column(db.String(255), nullable=False)
    photos = db.Column(db.String(255))

    def __init__(self, firstName, middleName, lastName, emailAddress, phoneNumber, password, role, dateCreated, dateModified, location, status, confirmed, confirmedOn, token, photos):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber
        self.password = password
        self.role = role
        self.dateCreated = dateCreated
        self.dateModified = dateModified
        self.location = location
        self.status = status
        self.confirmed = confirmed
        self.confirmedOn = confirmedOn
        self.token = token
        self.photos = photos

    def deleteUser(user):
        db.session.delete(user)

    def addUser(user):
        db.session.add(user)
        db.session.commit()

    def update():
        db.session.commit()

