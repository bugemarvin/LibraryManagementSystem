/* global fetch */
/* global alert */
/* eslint-disable semi */
/* eslint-disable no-unused-vars */
/* eslint-disable array-callback-return */
/* eslint-enable array-callback-return */

/**
 * Makes a fetch request to the specified path with the given request type and JSON data.
 * @method PUT, POST, GET, DELETE, etc
 * @param {string} path - The path for the API endpoint.
 * @param {string} ReqType - The request type (e.g., GET, POST, PUT, DELETE).
 * @param {Object} jsonData - The JSON data to be sent with the request.
 * @returns {Promise} A promise that resolves with the response data or rejects with an error.
 */
const fetchRequest = (path, ReqType, jsonData) => {
  const url = `http://127.0.0.1:5000/api/v1/${path}`;

  return new Promise((resolve, reject) => {
    fetch(url, {
      method: ReqType,
      headers: {
        'Content-Type': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: ReqType === 'GET' ? null : JSON.stringify(jsonData)
    })
      .then((response) => response.json())
      .then(resolve)
      .catch(reject);
  });
};

/**
 * Creates a list item and appends it to the specified element.
 * @param {string} id - The id of the element to append the list item to.
 * @param {string} data - The text content of the list item.
 * @returns {Node} - The appended list item element.
 */
const createLi = (id, data) => {
  const li = document.createDocumentFragment();
  const listItem = document.createElement('li');
  listItem.textContent = data;
  li.appendChild(listItem);
  const info = document.getElementById(id).appendChild(li);
  return info;
};

/**
 * Creates an HTML li element with information about a book.
 * @param {Object} data - The data object containing book information.
 * @param {string} data.title - The title of the book.
 * @param {string} data.author - The author of the book.
 * @param {string} data.genre - The genre of the book.
 * @param {string} data.isbn - The ISBN of the book.
 * @param {number} data.year - The year the book was published.
 * @param {number} data.copiesAvailable - The number of copies available for the book.
 * @param {string} data.synopsis - The synopsis of the book.
 * @returns {HTMLLIElement} - The created li element.
 */
const createLis = (data) => {
  const li = document.createElement('li');
  li.innerHTML = `<strong>${data.title}</strong><br>Author: ${data.author}<br>Genre: ${data.genre}<br>ISBN: ${data.isbn}<br>Year: ${data.year}<br>Copies Available: ${data.copiesAvailable}<br>Synopsis: ${data.synopsis}<br><br>`;
  return li;
};

/**
 * Displays a list of books in the specified container element.
 * @param {string} id - The ID of the container element.
 * @param {Array} books - An array of book objects.
 */
const displayBooky = (id, books) => {
  const container = document.getElementById(id);
  books.forEach((book) => {
    const listItem = createLis(book);
    container.appendChild(listItem);
  });
};

/**
 * Fetches and displays all books.
 * @method GET
 * @param {HTMLElement} all - The container element to display the books.
 * @returns {Promise} - A promise that resolves with the response from the server.
 */
const listAllBooks = (all) => {
  fetchRequest('list', 'GET')
    .then((response) => {
      if (response.success) {
        displayBooky(all, response.message);
      } else if (response.status === 204) {
        createLi(all, response.message);
      } else {
        // createLi(all, response.message);
        alert('Error: ' + response.statusText);
      }
      return response;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
};

/**
 * Fetches and displays books by category.
 * @method GET
 * @param {string} category - The category of books to fetch.
 * @param {string} id - The ID of the element to display the books in.
 * @returns {Promise} - A promise that resolves with the response from the server.
 */
const listBooksByCategory = (category, id) => {
  fetchRequest(`list/category?genre=${category}`, 'GET')
    .then((response) => {
      if (response.success) {
        displayBooky(id, response.message);
      } else {
        createLi(id, response.message);
      }
      return response;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
};

/**
 * Inserts a book into the library management system.
 * @method POST
 * @param {Object} book - The book object to insert in the database table books json
 * @param {string} book.title - The title of the book.
 * @param {string} book.author - The author of the book.
 * @param {string} book.genre - The genre of the book.
 * @param {string} book.isbn - The ISBN of the book.
 * @param {number} book.year - The year the book was published.
 * @param {number} book.copiesAvailable - The number of copies available for the book.
 * @param {string} book.synopsis - The synopsis of the book.
 * @returns {Promise} - A promise that resolves with the response from the server in json format.
 */
const insertBook = () => {
  // Get form data
  const title = document.getElementById('title').value;
  const author = document.getElementById('author').value;
  const genre = document.getElementById('genre').value;
  const isbn = document.getElementById('isbn').value;
  const year = document.getElementById('year').value;
  const synopsis = document.getElementById('synopsis').value;
  const copiesAvailable = document.getElementById('copiesAvailable').value;

  // Validate form data
  if (!title || !author || !genre || !isbn || !year || !synopsis || !copiesAvailable) {
    alert('Please enter all the book details.');
  }
  const jsonData = {
    title,
    author,
    genre,
    isbn,
    year,
    synopsis,
    copiesAvailable
  };

  // fetching data from the Flask server
  fetchRequest('insert', 'POST', jsonData)
    .then((response) => {
      if (response.success) {
        // alert('Message: ' + response.message);
        createLi('insert-book', response.message);
        console.log(response.message);
      } else {
        createLi('insert-book', response.message);
        console.log('Error: ' + response.message);
      }
      return response;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
};

/**
 * Deletes a book from the library management system.
 * @method DELETE
 * @param {string} isbn_or_title - The ISBN or title of the book to delete.
 * @returns {Promise} - A promise that resolves with the response from the server.
 */
const deleteBook = () => {
  const isbnOrTitle = document.getElementById('isbn_or_title').value;

  if (!isbnOrTitle) {
    alert('Please enter ISBN or title to delete.');
    return;
  }
  const info = {
    isbnOrTitle
  };

  fetchRequest('delete', 'DELETE', info)
    .then((response) => {
      if (response.success) {
        // alert('Message: ' + response.message);
        createLi('delete-book', response.message + ' ' + isbnOrTitle);
      } else {
        createLi('delete-book', response.message);
      }
      return response
    })
    .catch((error) => {
      console.error('Error:', error);
    });
};

/**
 * Updates a book in the library management system.
 * @method PUT
 * @param {Object} book - The book object to update in the database table books json format.
 * @param {string} book.title - The title of the book.
 * @param {string} book.author - The author of the book.
 * @param {string} book.genre - The genre of the book.
 * @param {string} book.isbn - The ISBN of the book.
 * @param {number} book.year - The year the book was published.
 * @param {number} book.copiesAvailable - The number of copies available for the book.
 * @param {string} book.synopsis - The synopsis of the book.
 * @returns {Promise} - A promise that resolves with the response from the server.
 */
const updateBook = () => {
  const title = document.getElementById('titleUpdate').value;
  const author = document.getElementById('authorUpdate').value;
  const genre = document.getElementById('genreUpdate').value;
  const isbn = document.getElementById('isbnUpdate').value;
  const year = document.getElementById('yearUpdate').value;
  const synopsis = document.getElementById('synopsisUpdate').value;
  const copiesAvailable = document.getElementById('copiesAvailableUpdate').value;
  const jsonData = { title, author, genre, isbn, year, synopsis, copiesAvailable };
  fetchRequest('update', 'PUT', jsonData)
    .then((response) => {
      if (response.success) {
        // alert('Message: ' + response.message);
        createLi('update-book', response.message);
        console.log(response.message);
      } else {
        createLi('update-book', response.message);
        console.log('Error: ' + response.message);
      }
      return response;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
};

/**
 * Performs a search for books based on the provided search query.
 * @method GET
 * @param {string} searchQuery - The search query.
 * @returns {Promise} - A promise that resolves with the response from the server.
 */
const searchBooks = () => {
  const searchQuery = document.getElementById('searchQuery').value;

  // Send a request to the Flask server
  fetchRequest(`search?query=${searchQuery}`, 'GET')
    .then((response) => {
      if (response.success) {
        displayBooky('search-book', response.message);
      } else {
        createLi('search-book', response.message);
      }
      return response;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
};

// Getting all the books from the database
listAllBooks('all-books');

/**
 * Lists books by the selected category.
 * @method GET
 * @param {string} category - The category of books to fetch.
 * @returns {Promise} - A promise that resolves with the response from the server.
 */
const listBooksBySelectedCategory = () => {
  const category = document.getElementById('category').value;
  listBooksByCategory(category, 'category-books');
};

/**
 * Generates a form input element with pre-filled values based on the provided data.
 * @param {Object} data - The data object containing the values for the form input fields.
 * @returns {HTMLElement} - The generated form input element.
 */
const formInput = (data) => {
  const li = document.getElementById('updateDetails');
  li.innerHTML = `<div class="form-group"><label for="Data">Title:</label><input type="text" id="titleUpdate" class="form-control" value="${data.title}"><br><lable for="Data">Author:</label><input type="text" id="authorUpdate" class="form-control" value="${data.author}"><br><lable for="Data">Genre:</label><input type="text" id="genreUpdate" class="form-control" value="${data.genre}"><br><lable for="Data">ISBN:</label><input type="text" id="isbnUpdate" class="form-control" value="${data.isbn}"><br><lable for="Data">Year:</label><input type="text" id="yearUpdate" class="form-control" value="${data.year}"><br><lable for="Data">Synopsis:</label><input type="text" id="synopsisUpdate" class="form-control" value="${data.synopsis}"><br><lable for="Data">Copies Available:</label><input type="text" id="copiesAvailableUpdate" class="form-control" value="${data.copiesAvailable}"><br><button type="button" class="btn btn-primary" onclick="updateBook()">Update Book</button></div>`;
  return li;
};

/**
 * Displays a list of books in the specified container element.
 * @param {string} id - The ID of the container element.
 * @param {Array} books - An array of book objects.
 */
const displayBooks = (id, books) => {
  const inputs = document.createDocumentFragment();
  const container = document.getElementById(id);
  container.innerHTML = '';
  books.forEach((book) => {
    const listItem = formInput(book);
    inputs.appendChild(document.createElement(listItem));
  });
  container.appendChild(inputs);
};

/**
 * Updates the search results based on the provided search query.
 * @method GET
 * @param {string} searchQuery - The search query.
 * @returns {Promise} - A promise that resolves with the response from the server.
 */
const updatesearch = () => {
  const searchQuery = document.getElementById('searchupdate').value;
  fetchRequest(`search/update?query=${searchQuery}`, 'GET')
    .then((response) => {
      if (response.success) {
        displayBooks('updateDetails', response.message);
        console.log(response.message);
      } else {
        createLi('searchUpdate-book', response.message);
        console.log('Error: ' + response.message);
      }
      return response;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
};
