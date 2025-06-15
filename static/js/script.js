console.log("script.js loaded!");

const toggler = document.getElementById("navToggler");
const collapse = document.getElementById("navbarSupportedContent");
const userTypeSelect = document.getElementById("user_type");
const fanForm = document.getElementById("fanForm");
const artistForm = document.getElementById("artistForm");
const venueForm = document.getElementById("venueForm");

// This function is called when the user clicks the "Delete Profile" button
  function confirmDelete() {
    return confirm("Are you sure you want to delete your profile? This action cannot be undone.");
}

// This script handles the toggling of the navigation menu
// It changes the icon from a hamburger to a close icon when the menu is open
// It also ensures the close icon is hidden when the menu is closed
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


// This function is called when the user clicks on a contact type button (fan, artist, venue)
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

// This script initializes the contact form based on the selected user type
// It listens for changes on the user type dropdown and shows the corresponding form
  function setFormState(formElement, show) {
    if (!formElement) return;

    // Show or hide the form visually
    formElement.style.display = show ? "block" : "none";

    // Enable or disable all form fields
    const inputs = formElement.querySelectorAll("input, textarea, select");
    inputs.forEach(input => input.disabled = !show);
  }

  function hideAllForms() {
    setFormState(fanForm, false);
    setFormState(artistForm, false);
    setFormState(venueForm, false);
}

  if (userTypeSelect) {
    userTypeSelect.addEventListener("change", function () {
      hideAllForms();
      const selected = this.value;
      if (selected === "fan") setFormState(fanForm, true);
      else if (selected === "artist") setFormState(artistForm, true);
      else if (selected === "venue") setFormState(venueForm, true);
    });

    // Restore form if user had already selected something
    const preselected = userTypeSelect.getAttribute("data-selected");
    if (preselected) {
      userTypeSelect.value = preselected;
      userTypeSelect.dispatchEvent(new Event("change"));
    }
  }

// This script handles the toggling of the review management form
// It allows users to manage their reviews by showing or hiding the form
  document.querySelectorAll("[data-toggle-manage]").forEach(function (button) {
    button.addEventListener("click", function () {

      const reviewId = this.dataset.toggleManage;
      const form = document.getElementById(`manage-form-${reviewId}`);
      if (form) {
        form.classList.toggle("d-none");
      }
      console.log("Button clicked:", reviewId);
    });
  });

  // Cancel
  document.querySelectorAll("[data-cancel-manage]").forEach(function (button) {
    button.addEventListener("click", function () {
      const reviewId = this.dataset.cancelManage;
      const form = document.getElementById(`manage-form-${reviewId}`);
      if (form) {
        form.classList.add("d-none");
      }
    });
  });

  // Confirm before delete
  document.querySelectorAll("[data-delete-button]").forEach(function (btn) {
    btn.addEventListener("click", function (event) {
      const confirmDelete = confirm("Are you sure you want to delete this review?");
      if (!confirmDelete) {
        event.preventDefault();
      }
    });
  });



