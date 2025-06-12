console.log("script.js loaded!");

// This function is called when the user clicks the "Delete Profile" button.
function confirmDelete() {
    return confirm("Are you sure you want to delete your profile? This action cannot be undone.");
}

// This script handles the toggling of the mobile navigation menu.
// It changes the icon from a hamburger to a close icon when the menu is open.
document.addEventListener("DOMContentLoaded", function () {
  const toggler = document.getElementById("navToggler");
  const collapse = document.getElementById("navbarSupportedContent");

  if (toggler && collapse) {
    const icon = toggler.querySelector(".navbar-toggler-icon");
    const closeIcon = toggler.querySelector(".navbar-close-icon");

    collapse.addEventListener("show.bs.collapse", () => {
      if (icon) icon.classList.add("d-none");
      if (closeIcon) closeIcon.classList.remove("d-none");
    });

    collapse.addEventListener("hide.bs.collapse", () => {
      if (icon) icon.classList.remove("d-none");
      if (closeIcon) closeIcon.classList.add("d-none");
    });
  }
});


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

// This script initializes the contact form based on the selected user type.
// It listens for changes on the user type dropdown and shows the corresponding form.
document.addEventListener("DOMContentLoaded", function () {
  const userTypeSelect = document.getElementById("user_type");
  const fanForm = document.getElementById("fanForm");
  const artistForm = document.getElementById("artistForm");
  const venueForm = document.getElementById("venueForm");

  function hideAllForms() {
    if (fanForm) fanForm.style.display = "none";
    if (artistForm) artistForm.style.display = "none";
    if (venueForm) venueForm.style.display = "none";
  }

  if (userTypeSelect) {
    userTypeSelect.addEventListener("change", function () {
      hideAllForms();
      const selected = this.value;
      if (selected === "fan" && fanForm) fanForm.style.display = "block";
      else if (selected === "artist" && artistForm) artistForm.style.display = "block";
      else if (selected === "venue" && venueForm) venueForm.style.display = "block";
    });

    // Restore selected form on reload
    const preselected = userTypeSelect.getAttribute("data-selected");
    if (preselected) {
      userTypeSelect.value = preselected;
      userTypeSelect.dispatchEvent(new Event("change"));
    }
  }
});

