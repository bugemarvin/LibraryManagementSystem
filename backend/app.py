from flask import Flask, jsonify
from flask_cors import CORS
from routes.bookRoutes import BookRoutes
from routes.route import Routes
from models.user import db
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

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

# Configure your MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://{}:{}@{}/{}'.format(userName, userPassword, host, dataBaseName)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()

# Defining the main routes
defaultRoute = routeDefault

# Define main routes
@app.route(defaultRoute + '/', methods=['GET'], strict_slashes=False)
def home():
    return Routes.index()

@app.route(defaultRoute + '/status', methods=['GET'], strict_slashes=False)
def status():
    return Routes.status()

@app.route(defaultRoute + '/stats', methods=['GET'], strict_slashes=False)
def stats():
    return Routes.stats()

# Define routes to interact with books
@app.route(defaultRoute + '/insert', methods=['POST'], strict_slashes=False)
def add():
    return BookRoutes.insert_book()

@app.route(defaultRoute + '/delete', methods=['DELETE'], strict_slashes=False)
def delete():
    return BookRoutes.delete()

@app.route(defaultRoute + '/search', methods=['GET'], strict_slashes=False)
def search():
    return BookRoutes.searchBooks()

@app.route(defaultRoute + '/search/update', methods=['GET'], strict_slashes=False)
def searchupdate():
    return BookRoutes.searchAll()

@app.route(defaultRoute + '/list', methods=['GET'], strict_slashes=False)
def list_books():
    return BookRoutes.get_book_list()

@app.route(defaultRoute + '/list/category', methods=['GET'], strict_slashes=False)
def list_books_by_category():
    return BookRoutes.listAllBycategory()

@app.route(defaultRoute + '/update', methods=['PUT'], strict_slashes=False)
def update():
    return BookRoutes.updateBook()

# error handler
@app.errorhandler(404)
def not_found(error):
    return jsonify({"success": False, "error": 404, "message": "Resource Not Found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
