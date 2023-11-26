# Library Management System

This is a web application that serves as a library management system. It allows users to add, delete, search, and update books in the library. Additionally, the application offers routes to retrieve statistics about the library, such as the total number of books, categories, and user counts.

## Table of Contents

- [Library Management System API](#library-management-system-api)
  - [Table of Contents](#table-of-contents)
  - [About the Project](#about-the-project)
    - [Built With](#built-with)
  - [Setup](#setup)
    - [Requirements](#requirements)
    - [Activate the virtual environment](#activate-the-virtual-environment)
    - [Database Configuration](#database-configuration)
    - [Running the Application](#running-the-application)
  - [API Endpoints](#api-endpoints)
    - [Welcome](#welcome)
    - [Status](#status)
    - [Statistics](#statistics)
    - [Add a Book](#add-a-book)
    - [Delete a Book](#delete-a-book)
    - [Search Books](#search-books)
    - [List All Books](#list-all-books)
    - [List Books by Category](#list-books-by-category)
    - [Update a Book](#update-a-book)
    - [Error Handling](#error-handling)
- [Frontend Documentation](#frontend-documentation)
  - [fetchRequest Function](#fetchrequest-function)
  - [createLi Function](#createli-function)
  - [createLis Function](#createlis-function)
  - [displayBooky Function](#displaybooky-function)
  - [listAllBooks Function](#listallbooks-function)
  - [listBooksByCategory Function](#listbooksbycategory-function)
  - [insertBook Function](#insertbook-function)
    - [deleteBook Function](#deletebook-function)
  - [updateBook Function](#updatebook-function)
  - [searchBooks Function](#searchbooks-function)
  - [listBooksBySelectedCategory Function](#listbooksbyselectedcategory-function)
  - [formInput Function](#forminput-function)
  - [displayBooks Function](#displaybooks-function)
  - [updatesearch Function](#updatesearch-function)
  - [Usage](#usage)

## About the Project

This is a Flask application serves as a Library Management System API. It endpoints to manage books in the library, including adding, deleting, searching, and updating book details. Additionally, the API offers routes to retrieve statistics about the library, such as the total number of books, categories, and user counts.

### Built With

* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/en/2.0.x/)
* [MySQL](https://www.mysql.com/)
* [Bootstrap](https://getbootstrap.com/)
* [fetch API](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API)
* [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
* [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
* [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)

## Setup

### Requirements

Make sure you have Python installed on your system. Then, create and activate a virtual environment.

# Create a virtual environment
```bash
python -m venv venv
```

### Activate the virtual environment
#### On Windows
```bash
venv\Scripts\activate
```
#### On macOS/Linux
```bash
source venv/bin/activate
```

Install the required Python packages using the provided `requirements.txt` file:

```bash
pip install -r requirements.txt
```

### Database Configuration 
Set up your MySQL database by configuring the environment variables in a `.env` file.\
Specify the database `user`, `password`, `host`, `name`, and the `default route`.

```env
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=your_database_host
DATABASE_NAME=your_database_name
ROUTE_DEFAULT=/api
```

### Running the Application

Run the Flask application using the following command:

```bash
python app.py or flask run
```

The application will be accessible at http://127.0.0.1:5000/ by default.

# API Endpoints

### Welcome
* **Route**: `/api/v1`
* **Method**: `GET`
* **Description**: *Welcome message for the books library system.*
#### Example Response:
```json
{
    "success": true,
    "status": 200,
    "message": "Welcome to the books library system"
}
```

### Status
* **Route**: `/api/v1/status`
* **Method**: `GET`
* **Description**: *Returns a status message confirming that the application is running.*
#### Example Response:
```json
{
  "success": true,
  "status": 200,
  "message": [
    {"request": true, "response": true},
    {"Header1": "Value1", "Header2": "Value2"}
  ]
}
```

### Statistics
* **Route**: `/api/v1/stats`
* **Method**: `GET`
* **Description**: *Returns statistics of the library management system.*
#### Example Response:
```json
{
  "success": true,
  "status": 200,
  "message": [
    {
      "book": [
        {
          "total": 50,
          "countByCategories": 5,
          "categories": ["Fiction", "Non-Fiction"]
        }
      ]
    },
    {
      "user": [
        {
          "total": 100,
          "verified": 80,
          "unverified": 20
        }
      ]
    }
  ]
}
```

### Add a Book
* **Route**: `/api/v1/insert`
* **Method**: `POST`
* **Description**: *Adds a book to the library.*
#### Example Request:
```json
{
  "title": "Sample Book",
  "author": "John Doe",
  "genre": "Fiction",
  "isbn": "1234567890",
  "year": 2022,
  "synopsis": "A sample book synopsis.",
  "copiesAvailable": 10
}
```
#### Example Response:
```json

    {
      "success": true,
      "status": 201,
      "message": "The book has been added to the Library"
    }
```
### Delete a Book
* **Route**: `/api/v1/delete`
* **Method**: `DELETE`
* **Description**: *Deletes a book from the library.*
* Example Request:
```json

{
  "isbnOrTitle": "1234567890"
}
```
#### Example Response:
```json

    {
      "success": true,
      "status": 201,
      "message": "The book has been deleted"
    }
```

### Search Books
* **Route**: `/api/v1/search`
* **Method**: `GET`
* **Description**: *Searches for books in the library based on a query.*
* **Query Parameters**:
        *query*=`Search term`
### Example Response:
```json

    {
      "success": true,
      "status": 200,
      "message": [
        {
          "id": 1,
          "title": "Sample Book",
          "author": "John Doe",
          "genre": "Fiction",
          "isbn": "1234567890",
          "year": "2022",
          "synopsis": "A sample book synopsis.",
          "copiesAvailable": 10,
          "dateAdded": "2022-01-01T12:00:00",
          "dateModified": "2022-01-01T12:00:00"
        }
      ],
      "count": 1
    }
```

### List All Books
* **Route**: `/api/v1/list`
* **Method**: `GET`
* **Description**: *Retrieves a list of all books from the library.*
### Example Response:
```json

    {
      "success": true,
      "status": 200,
      "message": [
        {
          "id": 1,
          "title": "Sample Book",
          "author": "John Doe",
          "genre": "Fiction",
          "isbn": "1234567890",
          "year": "2022",
          "synopsis": "A sample book synopsis.",
          "copiesAvailable": 10,
          "dateAdded": "2022-01-01T12:00:00",
          "dateModified": "2022-01-01T12:00:00"
        }
      ],
      "count": 1
    }
```

### List Books by Category
* **Route**: `/api/v1/list/category`
* **Method**: `GET`
* **Description**: *Retrieves a list of books based on a specific genre.*
* **Query Parameters**:
        *genre*=`Book category`
#### Example Response:
```json

    {
      "success": true,
      "status": 200,
      "message": [
        {
          "id": 1,
          "title": "Sample Book",
          "author": "John Doe",
          "genre": "Fiction",
          "isbn": "1234567890",
          "year": "2022",
          "synopsis": "A sample book synopsis.",
          "copiesAvailable": 10,
          "dateAdded": "2022-01-01T12:00:00",
          "dateModified": "2022-01-01T12:00:00"
        }
      ],
      "count": 1
    }
```
### Update a Book
* **Route**: `/api/v1/update`
* **Method**: `PUT`
* **Description**: *Updates the details of a book in the library.*
#### Example Request:
```json

{
  "title": "Updated Sample Book",
  "author": "John Doe",
  "genre": "Fiction",
  "isbn": "1234567890",
  "year": 2023,
  "synopsis": "An updated sample book synopsis.",
  "copiesAvailable": 5
}
```
#### Example Response:
```json

{
      "success": true,
      "status": 201,
      "message": "The book has been updated in the Library"
}
```

### Error Handling
* **Description**: *404 Not Found*
```json
{
  "success": false,
  "status": 404,
  "message": "Resource Not Found"
}
```
# Frontend Documentation

This document provides an overview of the frontend code for a library management system.
The code includes functions for making fetch requests, creating and displaying list items, managing books, and interacting with a Flask server.

## fetchRequest Function

This function makes a fetch request to the specified API endpoint with the given request type and JSON data.
```javascript
      Parameters:
        path (string): The path for the API endpoint.
        ReqType (string): The request type (e.g., GET, POST, PUT, DELETE).
        jsonData (Object): The JSON data to be sent with the request.

      Returns:
        A Promise that resolves with the response data or rejects with an error.
```
## createLi Function

This function creates a list item and appends it to the specified element.
```javascript
    Parameters:
        id (string): The id of the element to append the list item to.
        data (string): The text content of the list item.

    Returns:
        The appended list item element.
```
## createLis Function

This function creates an HTML li element with information about a book.
```javascript
    Parameters:
        data (Object): The data object containing book information.

    Returns:
        The created li element.
```
## displayBooky Function

This function displays a list of books in the specified container element.
```javascript
    Parameters:
        id (string): The ID of the container element.
        books (Array): An array of book objects.
```
## listAllBooks Function

This function fetches and displays all books.
```javascript
    Parameters:
        all (HTMLElement): The container element to display the books.

    Returns:
        A Promise that resolves with the response from the server.
```
## listBooksByCategory Function

This function fetches and displays books by category.
```javascript
    Parameters:
        category (string): The category of books to fetch.
        id (string): The ID of the element to display the books in.

    Returns:
        A Promise that resolves with the response from the server.
```
## insertBook Function

This function inserts a book into the library management system.
```javascript
    Returns:
        A Promise that resolves with the response from the server in JSON format.
```
### deleteBook Function

This function deletes a book from the library management system.
```javascript
    Returns:
        A Promise that resolves with the response from the server.
```
## updateBook Function

This function updates a book in the library management system.
```javascript
    Returns:
        A Promise that resolves with the response from the server.
```
## searchBooks Function

This function performs a search for books based on the provided search query.
```javascript
    Returns:
        A Promise that resolves with the response from the server.
```
## listBooksBySelectedCategory Function

This function lists books by the selected category.
```javascript
    Returns:
        A Promise that resolves with the response from the server.
```
## formInput Function

This function generates a form input element with pre-filled values based on the provided data.
```javascript
    Parameters:
        data (Object): The data object containing the values for the form input fields.

    Returns:
        The generated form input element.
```
## displayBooks Function

This function displays a list of books in the specified container element.
```javascript
    Parameters:
        id (string): The ID of the container element.
        books (Array): An array of book objects.
```
## updatesearch Function

This function updates the search results based on the provided search query.
```javascript
    Returns:
        A Promise that resolves with the response from the server.
```
## Usage
* Call listAllBooks('all-books') to display all books on page load.
* Use other functions like listBooksByCategory, insertBook, deleteBook, updateBook, searchBooks, and listBooksBySelectedCategory to interact with the library management system.