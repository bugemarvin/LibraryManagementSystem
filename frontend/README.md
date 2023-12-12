# Frontend Documentation

This document provides an overview of the frontend code for a library management system for testing purposes.
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
* Call `listAllBooks('all-books')` to display all books on page load.
* Use other functions like `listBooksByCategory`, `insertBook`, `deleteBook`, `updateBook`, `searchBooks`, and `listBooksBySelectedCategory` to interact with the library management system.
