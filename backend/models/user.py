from flask_sqlalchemy import SQLAlchemy

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
            phoneNumber (int): The phone number of the user.
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
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    firstName = db.Column(db.String(255), nullable=False)
    middleName = db.Column(db.String(255))
    lastName = db.Column(db.String(255), nullable=False)
    emailAddress = db.Column(db.String(255), nullable=False)
    phoneNumber = db.Column(db.Integer(), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(255), nullable=False, default='user')
    dateCreated = db.Column(db.DateTime, nullable=False)
    dateModified = db.Column(db.DateTime, nullable=True)
    location = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(255), nullable=False, default='pending')
    confirmed = db.Column(db.Boolean, nullable=False, default=False)
    confirmedOn = db.Column(db.DateTime, nullable=True)
    token = db.Column(db.String(255), nullable=True)
    photos = db.Column(db.String(255), nullable=True)

    def __init__(self, firstName, middleName, lastName, emailAddress, phoneNumber, password, role, location, status, confirmed, confirmedOn, token, tokenExpiration, photos):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.emailAddress = emailAddress
        self.phoneNumber = phoneNumber
        self.password = password
        self.role = role
        self.location = location
        self.status = status
        self.confirmed = confirmed
        self.confirmedOn = confirmedOn
        self.token = token
        self.tokenExpiration = tokenExpiration
        self.photos = photos

    def updateUser(user):
        db.session.update(user)
        db.session.commit()

    def deleteUser(user):
        db.session.delete(user)

    def addUser(user):
        db.session.add(user)
        db.session.commit()

    def update():
        db.session.commit()
        """_summary_
                """
