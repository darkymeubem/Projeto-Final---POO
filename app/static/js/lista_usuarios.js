// app/static/js/lista_usuarios.js
const editButtons = document.querySelectorAll(".edit-btn");
const deleteButtons = document.querySelectorAll(".delete-btn");

function animateButton(button) {
  button.addEventListener("mouseenter", () => {
    button.style.transform = "scale(1.1)";
    button.style.boxShadow = "0 4px 8px rgba(0, 0, 0, 0.3)";
  });

  button.addEventListener("mouseleave", () => {
    button.style.transform = "scale(1)";
    button.style.boxShadow = "0 2px 4px rgba(0, 0, 0, 0.2)";
  });
}

editButtons.forEach((button) => {
  animateButton(button);
});

deleteButtons.forEach((button) => {
  animateButton(button);
});
