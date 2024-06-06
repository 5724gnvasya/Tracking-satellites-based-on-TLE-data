const addButton = document.querySelector(".add");
const submitButton  = document.querySelector(".submit");

function createForm() {
  const form = document.createElement("form");
  form.className = "satellite-form";
  const inputField1 = document.createElement("input");
  inputField1.type = "number";
  inputField1.placeholder = "Enter satellite's ID";
  // inputField1.style.placeholder = "font-family: 'Lato', sans-serif; color: #ccc; font-weight: bold; text-decoration: none; text-transform: uppercase;";
  // inputField1.setAttribute("placeholder", "Enter satellite's ID");
  // inputField1.setAttribute("style", "placeholder: font-family: 'Lato', sans-serif; color: #ccc;");

  form.appendChild(inputField1);

  const inputField2 = document.createElement("input");
  inputField2.type = "number";
  inputField2.placeholder = "Enter step";
  // inputField2.style.placeholder = "font-family: 'Lato', sans-serif; color: #ccc; font-weight: bold; text-decoration: none; text-transform: uppercase;";
  
  form.appendChild(inputField2);

  const inputField3 = document.createElement("input");
  inputField3.type = "date";
  inputField3.placeholder = "Enter date";
  // inputField3.style.placeholder = "font-family: 'Lato', sans-serif; color: #ccc; font-weight: bold; text-decoration: none; text-transform: uppercase;";
  
  form.appendChild(inputField3);

  const deleteButton = document.createElement("button");
  deleteButton.type = "button";
  deleteButton.textContent = "Delete satellite";
  deleteButton.className = "delete";
  form.appendChild(deleteButton);

  
  deleteButton.addEventListener("click", function() {
    form.remove();
  });

  document.querySelector('.satellites_info').appendChild(form);

}

// document.addEventListener("DOMContentLoaded", function() {
//   createForm();
// });
addButton.addEventListener("click", createForm);


// document.addEventListener("DOMContentLoaded", function() {
//   const deleteButton = document.querySelector(".delete");

//   deleteButton.addEventListener("click", function() {
//     const forms = document.querySelectorAll("form");
//     if (forms.length > 0) {
//       forms[forms.length - 1].remove();
//     }
//   });
// });



const imageBlock = document.getElementById('image-block');


submitButton.addEventListener('click', function() {
  const imageBlock = document.getElementById('image-block');
  const existingImage = imageBlock.querySelector('img');

  if (!existingImage) {
  //   // If an image already exists, do nothing or replace it with a new one
  //   existingImage.src = '../static/icons/example1.jpg';
  // } else {
    const img = document.createElement('img');
    img.src = '../static/icons/example1.jpg';

    img.onload = function() {
      console.log('Image loaded!');
      imageBlock.appendChild(img);
    }
  }
}
);




// отправка данных на бэк, пока не работает
// submitButton.addEventListener("click", function() {
//   const forms = document.querySelectorAll("form");
//   const lastForm = forms[forms.length - 1];
//   const formData = new FormData(lastForm);

//   fetch('/api/satellites', {
//     method: 'POST',
//     body: formData
//   })
//   .then(response => response.json())
//   .then(data => console.log(data))
//   .catch(error => console.error(error));
// });



