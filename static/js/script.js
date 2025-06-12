console.log("script.js loaded!");

// This function is called when the user clicks the "Delete Profile" button.
function confirmDelete() {
    return confirm("Are you sure you want to delete your profile? This action cannot be undone.");
}

// Contact modal
function openContactModal() {
    document.getElementById("contactModal").style.display = "block";
}
function closeContactModal() {
    document.getElementById("contactModal").style.display = "none";
}

// This function is called when the user clicks on a contact type button (fan, artist, venue).
function showSelectedForm() {
    const type = document.getElementById("user_type")?.value;
    const forms = document.querySelectorAll(".contact-form");

    forms.forEach(f => f.style.display = "none");

    if (type === "fan") {
        document.getElementById("fanForm").style.display = "block";
    } else if (type === "artist") {
        document.getElementById("artistForm").style.display = "block";
    } else if (type === "venue") {
        document.getElementById("venueForm").style.display = "block";
    }
}

document.addEventListener("DOMContentLoaded", function () {
    const dropdown = document.getElementById("user_type");

    if (dropdown) {
        dropdown.addEventListener("change", showSelectedForm);
    }
});

// This script toggles the visibility of the close icon in the navbar when the collapse state changes.
document.addEventListener("DOMContentLoaded", function () {
    const toggler = document.getElementById("navToggler");
    const collapse = document.getElementById("navbarSupportedContent");
    const icon = toggler.querySelector(".navbar-toggler-icon");
    const closeIcon = toggler.querySelector(".navbar-close-icon");

    collapse.addEventListener("show.bs.collapse", () => {
      icon.classList.add("d-none");
      closeIcon.classList.remove("d-none");
    });

    collapse.addEventListener("hide.bs.collapse", () => {
      icon.classList.remove("d-none");
      closeIcon.classList.add("d-none");
    });
  });