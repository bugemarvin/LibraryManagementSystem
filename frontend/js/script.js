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
  const url = `http://127.0.0.1:1245/api/v1/${path}`;

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
  if (document.getElementById(id).hasChildNodes()) {
    document.getElementById(id).innerHTML = '';
  }
  const listItem = document.createElement('li');
  listItem.textContent = data;
  li.appendChild(listItem);
  const info = document.getElementById(id).appendChild(li);
  return info;
};

const displaySuccess = (id, message) => {
  const success = document.getElementById(id);
  success.classList.add('list-group', 'alert', 'alert-success');
  success.innerHTML = '';
  success.innerHTML = message;
  success.style.textAlign = 'center';
  success.style.padding = '10px';
  success.style.color = 'white'
  success.style.fontWeight = 'bold';
  success.style.width = '50%';
  success.style.margin = 'auto';
};

const displayFormInput = (id) => {
  const forms = document.getElementById(id);
  const inputs = forms.getElementsByTagName('input');
  for (let i = 0; inputs.length; i++) {
    inputs[i].style.border = '1px solid red';
  }
}

const displayFormInputSuccess = (id) => {
  const forms = document.getElementById(id);
  const inputs = forms.getElementsByTagName('input');
  for (let i = 0; inputs.length; i++) {
    inputs[i].style.border = '1px solid green';
  }
}

const displayError = (id, message) => {
  const error = document.getElementById(id);
  error.classList.add('list-group', 'alert', 'alert-danger');
  error.innerHTML = '';
  error.innerHTML = message;
  error.style.textAlign = 'center';
  error.style.padding = '10px';
  error.style.color = 'white';
  error.style.fontWeight = 'bold';
  error.style.width = '50%';
  error.style.margin = 'auto';
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
  li.innerHTML = `<strong>${data.title}</strong><br><b>Author:</b> ${data.author}<br><b>Genre:</b> ${data.genre}<br><b>ISBN:</b> ${data.isbn}<br><b>Year:</b> ${data.year}<br><b>Copies Available:</b> ${data.copiesAvailable}<br><b>Synopsis:</b> ${data.synopsis}<br><br>`;
  return li;
};

/**
 * Displays a list of books in the specified container element.
 * @param {string} id - The ID of the container element.
 * @param {Array} books - An array of book objects.
 */
const displayBooky = (id, books) => {
  const container = document.getElementById(id);

  container.innerHTML = '';
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
  fetchRequest(`list/category?genre=${encodeURIComponent(category)}`, 'GET')
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
  const isbns = document.getElementById('isbn').value;
  const year = document.getElementById('year').value;
  const synopsis = document.getElementById('synopsis').value;
  const copiesAvailable = document.getElementById('copiesAvailable').value;
  const isbn = encodeURIComponent(isbns);

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
window.addEventListener('load', () => {
  const listBooks = document.getElementById('all-books');
  if (listBooks) listAllBooks('all-books');
});

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
  li.innerHTML = `<div class="form-group">
                    <label for="Data">Title:</label>
                    <input type="text" id="titleUpdate" class="form-control" value="${data.title}">
                    <br>
                    <lable for="Data">Author:</label>
                    <input type="text" id="authorUpdate" class="form-control" value="${data.author}">
                    <br>
                    <lable for="Data">Genre:</label>
                    <input type="text" id="genreUpdate" class="form-control" value="${data.genre}">
                    <br>
                    <lable for="Data">ISBN:</label>
                    <input type="text" id="isbnUpdate" class="form-control" value="${data.isbn}">
                    <br>
                    <lable for="Data">Year:</label>
                    <input type="text" id="yearUpdate" class="form-control" value="${data.year}">
                    <br>
                    <lable for="Data">Synopsis:</label>
                    <input type="text" id="synopsisUpdate" class="form-control" value="${data.synopsis}">
                    <br>
                    <lable for="Data">Copies Available:</label>
                    <input type="text" id="copiesAvailableUpdate" class="form-control" value="${data.copiesAvailable}">
                    <br>
                    <button type="button" class="btn btn-primary" onclick="updateBook()">Update Book</button>
                  </div>`;
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

const register = async () => {
  const fname = document.getElementById('fname').value;
  const mname = document.getElementById('mname').value;
  const lname = document.getElementById('lname').value;
  const email = document.getElementById('email').value;
  const phone = document.getElementById('phone').value;
  const password = document.getElementById('password').value;
  const repassword = document.getElementById('repassword').value;

  if (!fname || !lname || !email || !password || !repassword) {
    alert('Please enter all the user details.');
  }
  const jsonData = {
    fname,
    mname,
    lname,
    email,
    phone,
    password,
    repassword
  };
  fetchRequest('register', 'POST', jsonData)
    .then((response) => {
      if (response.status === 201) {
        displaySuccess('register', response.message);
        displayFormInputSuccess('registration');
        console.log(response.message);
      }
      if (response.status === 409) {
        displayError('register', response.message);
        displayFormInput('registration');
        console.log('Error: ' + response.message);
      }
      setTimeout(() => {
        window.location.href = '/frontend/register.html';
      }, 500);
      return response;
    })
    .catch((error) => {
      console.error('Error:', error);
    });
};

const Details = (id, message) => {
  const info = document.getElementById(id);
  info.innerHTML = message
}


const login = async () => {
  const username = document.getElementById('username').value;
  const password = document.getElementById('password').value;

  if (!username) {
    alert('Please Enter Username.');
  }

  if (!password) {
    alert('Please Enter Password.');
  }

  const jsonData = {
    username,
    password
  };
  await fetchRequest('login', 'POST', jsonData)
    .then((response) => {
      if (response.status === 200) {
        localStorage.setItem('token', response.token);
        window.location.href = '/user';
      }
    })
    .catch((error) => {
      createLi('danger', error.message)
      console.error('Error:', error);
    });
};

const logout = async () => {
  await fetchRequest('logout', 'GET')
    .then((response) => {
      if (response) {
        window.location.href = 'http://127.0.0.1:5500/frontend/login.html';
      }
      return response;
    }
    )
    .catch((error) => {
      console.error('Error:', error);
    });
};
