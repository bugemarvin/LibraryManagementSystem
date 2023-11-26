/* global fetch */
/* eslint-disable array-callback-return */
/* eslint-enable array-callback-return */

// Function to fetch data from the Flask server
const fetchRequest = (path, ReqType, jsonData) => {
  const url = `http://127.0.0.1:5000/api/v1/${path}`;

  return new Promise((resolve, reject) => {
    fetch(url, {
      method: ReqType,
      headers: {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Access-Control-Allow-Origin': '*'
      },
      body: ReqType === 'GET' ? null : JSON.stringify(jsonData)
    })
      .then((response) => response.json())
      .then(resolve)
      .catch(reject);
  });
};

// Function to create a list of books
const createLi = (id, data) => {
  const li = document.createDocumentFragment();
  const listItem = document.createElement('li');
  listItem.textContent = data;
  li.appendChild(listItem);
  const info = document.getElementById(id).appendChild(li);
  return info;
};

// Function to create a list item for a book
const createLis = (data) => {
  const li = document.createElement('li');
  li.innerHTML = `<strong>${data.title}</strong><br>Author: ${data.author}<br>Genre: ${data.genre}<br>ISBN: ${data.isbn}<br>Year: ${data.year}<br>Copies Available: ${data.copiesAvailable}<br>Synopsis: ${data.synopsis}<br><br>`;
  return li;
};

// Function to display books
const displayBooky = (id, books) => {
  const container = document.getElementById(id);
  books.forEach((book) => {
    const listItem = createLis(book);
    container.appendChild(listItem);
  });
};

// Function to list all books
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

// Function to list books by category
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

// Function to insert a new book
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

// Function to delete a book
const deleteBook = () => {
  const isbn_or_title = document.getElementById('isbn_or_title').value;

  if (!isbn_or_title) {
    alert('Please enter ISBN or title to delete.');
    return;
  }
  const info = {
    isbn_or_title: isbn_or_title
  };

  fetchRequest('delete', 'DELETE', info)
    .then((response) => {
      if (response.success) {
        // alert('Message: ' + response.message);
        createLi('delete-book', response.message + ' ' + isbn_or_title);
      } else {
        alert('Error: ' + response.statusText);
      }
      return response
    })
    .then((request) => {
      if (request.success) {
        console.log(request.message);
      }
      else {
        alert('Error: ' + request.message);
      }
      return request
    })
    .catch((error) => {
      console.error('Error:', error);
    });
};

// Function to update a book
const updateBook = () => {
  const title = document.getElementById('titleUpdate').value;
  const author = document.getElementById('authorUpdate').value;
  const genre = document.getElementById('genreUpdate').value;
  const isbn = document.getElementById('isbnUpdate').value;
  const year = document.getElementById('yearUpdate').value;
  const synopsis = document.getElementById('synopsisUpdate').value;
  const copiesAvailable = document.getElementById('copiesAvailableUpdate').value;
  const jsonData = {title, author, genre, isbn, year, synopsis, copiesAvailable};
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

// Function to search books
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

// calls for buttons

// Getting all the books from the database
listAllBooks('all-books');

// Function call to list books by the selected category
const listBooksBySelectedCategory = () => {
  const category = document.getElementById('category').value;
  listBooksByCategory(category, 'category-books');
};

// Function to create a form for updating book details
const formInput = (data) => {
  const li = document.getElementById('updateDetails');
  li.innerHTML = `<div class="form-group"><label for="Data">Title:</label><input type="text" id="titleUpdate" class="form-control" value="${data.title}"><br><lable for="Data">Author:</label><input type="text" id="authorUpdate" class="form-control" value="${data.author}"><br><lable for="Data">Genre:</label><input type="text" id="genreUpdate" class="form-control" value="${data.genre}"><br><lable for="Data">ISBN:</label><input type="text" id="isbnUpdate" class="form-control" value="${data.isbn}"><br><lable for="Data">Year:</label><input type="text" id="yearUpdate" class="form-control" value="${data.year}"><br><lable for="Data">Synopsis:</label><input type="text" id="synopsisUpdate" class="form-control" value="${data.synopsis}"><br><lable for="Data">Copies Available:</label><input type="text" id="copiesAvailableUpdate" class="form-control" value="${data.copiesAvailable}"><br><button type="button" class="btn btn-primary" onclick="updateBook()">Update Book</button></div>`;
  return li;
};

// Function to display books to update details using the form
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

// Function to search a book to update
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
