document.addEventListener("DOMContentLoaded", () => {
  const sidebar = document.getElementById("sidebar");
  const toggleButtons = document.querySelectorAll("#toggleSidebar");

  toggleButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      sidebar.classList.toggle("active");
    });
  });
});
