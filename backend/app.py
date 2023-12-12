from flask import Flask, jsonify
from flask_cors import CORS
from routes.bookRoutes import BookRoutes
from routes.route import Routes
from routes.userRoutes import UserRoutes
from models.user import db
from flask_migrate import Migrate
from dotenv import load_dotenv
from flask_jwt_extended import JWTManager, jwt_required
import os

# initialize the flask app
app = Flask(__name__)
CORS(app)

# Load environment variables
load_dotenv()

# Get environment variables
userName = os.getenv('DATABASE_USER')
userPassword = os.getenv('DATABASE_PASSWORD')
host = os.getenv('DATABASE_HOST')
dataBaseName = os.getenv('DATABASE_NAME')
routeDefault = os.getenv('ROUTE_DEFAULT')
secretKey = os.getenv('SECRET_KEY')

# Configure your MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(
    userName, userPassword, host, dataBaseName)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)
app.config['JWT_SECRET_KEY'] = secretKey
jwt = JWTManager(app)

with app.app_context():
    db.create_all()

# Defining the main routes
defaultRoute = routeDefault

@app.route(defaultRoute + '/', methods=['GET'], strict_slashes=False)
def home():
    """
    This function handles the home route of the application.
    It returns the result of the index() function from the Routes module.
    """
    return Routes.index()


@app.route(defaultRoute + '/status', methods=['GET'], strict_slashes=False)
def status():
    """
    Returns the status of the application.
    """
    return Routes.status()


@app.route(defaultRoute + '/stats', methods=['GET'], strict_slashes=False)
def stats():
    """
    Returns the statistics for the library management system.

    :return: The statistics data.
    """
    return Routes.stats()


@app.route(defaultRoute + '/insert', methods=['POST'], strict_slashes=False)
@jwt_required()
def add():
    """
    Add a book to the library.

    Returns:
        The result of inserting the book.
    """
    return BookRoutes.insert_book()


@app.route(defaultRoute + '/delete', methods=['DELETE'], strict_slashes=False)
@jwt_required()
def delete():
    """
    Deletes a book from the library.

    Returns:
        The result of the delete operation.
    """
    return BookRoutes.delete()


@app.route(defaultRoute + '/search', methods=['GET'], strict_slashes=False)
def search():
    """
    This function handles the search endpoint of the Library Management System API.
    It calls the searchBooks() function from the BookRoutes module to perform the search.
    """
    return BookRoutes.searchBooks()


@app.route(defaultRoute + '/search/update', methods=['GET'], strict_slashes=False)
def searchupdate():
    """
    This function handles the search update route.
    It calls the searchAll() function from the BookRoutes module.
    """
    return BookRoutes.searchAll()


@app.route(defaultRoute + '/list', methods=['GET'], strict_slashes=False)
def list_books():
    """
    Retrieves a list of books from the database.

    Returns:
        A list of books.
    """
    return BookRoutes.get_book_list()


@app.route(defaultRoute + '/list/category', methods=['GET'], strict_slashes=False)
def list_books_by_category():
    """
    Retrieve a list of books by category.

    Returns:
        A list of books filtered by category.
    """
    return BookRoutes.listAllBycategory()


@app.route(defaultRoute + '/update', methods=['PUT'], strict_slashes=False)
@jwt_required()
def update():
    """
    Update a book in the library.
    
    Returns:
        The updated book information.
    """
    return BookRoutes.updateBook()


# User routes
@app.route(defaultRoute + '/login', methods=['POST'], strict_slashes=False)
def login():
    """
    Login a user.

    Returns:
        The result of the login.
    """
    return UserRoutes.loginUser()

@app.route(defaultRoute + '/register', methods=['POST'], strict_slashes=False)
def register():
    """
    Register a user.

    Returns:
        The result of the registration.
    """
    return UserRoutes.registerUser()

@app.route(defaultRoute + "/user", methods=["GET"])
@jwt_required()
def getuser():
    return UserRoutes.getUser()

@app.route(defaultRoute + "/logout", methods=["GET"])
@jwt_required()
def logout():
    return UserRoutes.logoutUser()

'''
@app.route(defaultRoute + '/role', methods=['GET'])
@jwt_required
def role():
    return UserRoutes.roles()
'''

@app.errorhandler(404)
def not_found(error):
    """
    Error handler for 404 status code.

    Args:
        error: The error object.

    Returns:
        A JSON response with the error details.
    """
    return jsonify({"success": False, "error": 404, "message": "Resource Not Found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
