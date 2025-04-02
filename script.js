document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('button').addEventListener('click', function () {
        document.querySelector('.fingerprint').classList.toggle('scanning');
    });
});

// function openNav() {
//   document.getElementById("mySidebar").style.width = "250px";
//   document.getElementById("mySidebar").style.transition = "0.5s";
//   document.getElementsByClassName("content")[0].style.marginLeft = "250px";
// }

// function closeNav() {
//   document.getElementById("mySidebar").style.width = "0";
//   document.getElementsByClassName("content")[0].style.marginLeft = "0";
// }

function openNav() {
  document.getElementById("mySidebar").style.width = "250px";
  document.getElementById("mySidebar").style.transition = "0.5s";
}

function closeNav() {
  document.getElementById("mySidebar").style.width = "0";
}

// Your existing script.js file - modify the openNav function
function openNav() {
  var sidebar = document.getElementById("mySidebar");
  sidebar.style.display = (sidebar.style.display === "block") ? "none" : "block";
}


// mail
document.addEventListener("DOMContentLoaded", function () {
  // Function to create mailto link with relevant content from the result div
  function createMailtoLink() {
      // Get the content from the result div
      var disease = document.querySelector(".result .prediction p").textContent.trim();
      var solutions = document.querySelector(".result .suggestions p").textContent.trim();

      // Combine disease and solutions into a formatted message with line breaks
      var mailtoMessage = "Disease: " + disease + "%0A%0A" + "Solutions: " + solutions;

      // Create the mailto link
      var mailtoLink = "mailto:?subject=Plant%20Project%20Result&body=" + encodeURIComponent(mailtoMessage);

      // Redirect to the mailto link
      window.location.href = mailtoLink;
  }

  // Attach the function to the Gmail icon click event
  var gmailIcon = document.getElementById("gmailIcon");
  if (gmailIcon) {
      gmailIcon.addEventListener("click", function (event) {
          event.preventDefault(); // Prevent the default link behavior
          createMailtoLink();
      });
  }
});

//pdf

    document.addEventListener("DOMContentLoaded", function () {
        // Function to generate PDF with relevant content from the result div
        function generatePDF() {
            // Get the content from the result div
            var disease = document.querySelector(".result .prediction p").textContent.trim();
            var solutions = document.querySelector(".result .suggestions p").textContent.trim();

            // Combine disease and solutions into a formatted message with line breaks
            var pdfContent = "Disease: " + disease + "\n\nSolutions: " + solutions;

            // Create a new HTML element to hold the PDF content
            var pdfContainer = document.createElement("div");
            pdfContainer.textContent = pdfContent;

            // Use html2pdf library to generate the PDF
            html2pdf(pdfContainer, {
                margin: 10,
                filename: 'Plant_Project_Result.pdf',
                image: { type: 'jpeg', quality: 0.98 },
                html2canvas: { scale: 2 },
                jsPDF: { unit: 'mm', format: 'a4', orientation: 'portrait' }
            });
        }

        // Attach the function to the PDF icon click event
        var pdfIcon = document.getElementById("pdfIcon");
        if (pdfIcon) {
            pdfIcon.addEventListener("click", function (event) {
                event.preventDefault(); // Prevent the default link behavior
                generatePDF();
            });
        }
    });




