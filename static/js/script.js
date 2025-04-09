document.addEventListener("DOMContentLoaded", () => {
  const sidebar = document.getElementById("sidebar");
  const toggleButtons = document.querySelectorAll("#toggleSidebar");

  toggleButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      sidebar.classList.toggle("active");
    });
  });
});

// JavaScript code to handle file selection
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("scanForm");
  const imageInput = document.getElementById("imageInput");

  form.addEventListener("submit", function (e) {
    if (!imageInput.files.length) {
      e.preventDefault(); // Stop form submission
      alert("Please upload an image before submitting.");
    }
  });
});

document
  .getElementById("imageInput")
  .addEventListener("change", function (event) {
    var file = event.target.files[0];
    var reader = new FileReader();

    reader.onload = function (e) {
      var imageContainer = document.getElementById("imageContainer");
      imageContainer.style.backgroundImage = "url(" + e.target.result + ")";
    };

    reader.readAsDataURL(file);
  });

setTimeout(function () {
  const alert = document.getElementById("temp-alert");
  if (alert) {
    alert.style.transition = "opacity 0.5s ease-out";
    alert.style.opacity = 0;
    setTimeout(() => alert.remove(), 500); // Remove from DOM
  }
}, 4000);
