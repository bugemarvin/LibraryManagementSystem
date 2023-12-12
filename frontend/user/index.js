const token = localStorage.getItem('token');
if (!token) {
  window.location.href = 'login.html';
}

/**
 * Generates a form input element with pre-filled values based on the provided data.
 * @param {Object} data - The data object containing the values for the form input fields.
 * @returns {HTMLElement} - The generated form input element.
 */
const formInputs = (user) => {
  return `<div>
          <h1>Role:</h1>${user.role}<br/>
          <p>First Name:</p>${user.firstName}<br/>
          <p>Middle Name:</p>${user.middleName}<br/>
          <p>last Name:</p>${user.lastName}<br/>
          <p>phone Number:</p>${user.phoneNumber}<br/>
          <p>Photos:</p>${user.photos}<br/>
          <p>Status:</p>${user.status}<br/>
                        </div>`;
};

/**
 * Displays a list of books in the specified container element.
 * @param {string} id - The ID of the container element.
 * @param {Array} books - An array of book objects.
 */
const displayUser = (books) => {
//   const inputs = document.createDocumentFragment();
  const container = document.getElementById('users');
  container.innerHTML = formInputs(books);
};

fetch('http://127.0.0.1:1245/api/v1/user', {
  method: 'GET',
  headers: {
    Authorization: `Bearer ${token}`
  }
})
  .then(async (res) => res.json()).then((data) => {
    displayUser(data.user);
  })
  .catch((error) => {
    console.error('Error:', error);
  });
