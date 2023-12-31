# Library Management System API

This Flask application serves as a backend for a Library Management System API. It provides endpoints to manage books in the library, including adding, deleting, searching, and updating book details. Additionally, the API offers routes to retrieve statistics about the library, such as the total number of books, categories, and user counts.

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
ROUTE_DEFAULT=/api/v1
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

## Book Endpoints

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

## Error Endpoints

### Error Handling
* **Description**: *404 Not Found*
```json
{
  "success": false,
  "status": 404,
  "message": "Resource Not Found"
}
```

## User Endpoints

### Add user
* **Route**: `/api/v1/register`
* **Method**: `POST`
* **Description**: *Adds a user to the database.*
#### Example Request:
```json
{
		"confirmed": false,
		"confirmedOn": "Tue, 12 Dec 2023 14:22:36 GMT",
		"dateCreated": "Sun, 10 Dec 2023 10:53:06 GMT",
		"dateModified": "Tue, 12 Dec 2023 14:22:36 GMT",
		"emailAddress": "xxxx@xxx.com",
		"firstName": "Jhon",
		"id": "692d0248fe3f40dda061e34f45e41b04",
		"lastName": "Doe",
		"location": "",
		"middleName": "B",
		"phoneNumber": "000-0XX-XXX-XXX",
		"photos": null,
		"role": "user",
		"status": "inactive",
		"token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDI0NzczNTgsImlhdCI6MTcwMjM5MDk1OCwic3ViIjoiYnVnZW1hcnZpbkBvdXRsb29rLmNvbSJ9.mJp0HLS-u66s672qDGZmxjZmkiV92Ld-nRPoxZomnis"
	}
```
#### Example Response:
```json

    {
      "success": true,
      "status": 201,
      "message": "User created successfully"
    }
```

### Login user
* **Route**: `/api/v1/login`
* **Method**: `GET`
* **Description**: *Login a user*
```http
Authorization: Bearer <token>
```
#### Example Request:
```json
{
  "username": "emailAddress | phoneNumber",
  "password": "password"
}
```

### Example Response
```json
{
  "sucess": true,
  "status": 200,
  "message": "User logged in successfully",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDI0NzczNTgsImlhdCI6MTcwMjM5MDk1OCwic3ViIjoiYnVnZW1hcnZpbkBvdXRsb29rLmNvbSJ9.mJp0HLS-u66s672qDGZmxjZmkiV92Ld-nRPoxZomnis"
}
```

### Logout user
* **Route**: `/api/v1/logout`
* **Method**: `GET`
* **Description**: *Login a user*

### Example Response
```json
{
  "sucess": true,
  "status": 200,
  "message": "User logged out successfully",
}
```
