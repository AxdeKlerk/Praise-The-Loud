const toggler = document.getElementById("navToggler");
const collapse = document.getElementById("navbarSupportedContent");
const userTypeSelect = document.getElementById("user_type");
const fanForm = document.getElementById("fanForm");
const artistForm = document.getElementById("artistForm");
const venueForm = document.getElementById("venueForm");

//----------------------------------------------//
// 1. Confirm Delete For Profile Page
//----------------------------------------------//

  // This function is called when the user clicks the "Delete Profile" button
  function confirmDelete() {
    return confirm("Are you sure you want to delete? This action cannot be undone.");
}

//----------------------------------------------//
// 2. Toggle Navbar Icons
//----------------------------------------------//

  // Switches between hamburger (☰) and close (×) icon when navbar is opened or closed
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

//----------------------------------------------//
// 3. Contact Forms Based on User Type
//----------------------------------------------//

  // Helper function: shows or hides a form and enables/disables its fields
  function setFormState(formElement, show) {
    if (!formElement) return;

    // Show or hide the form visually
    formElement.style.display = show ? "block" : "none";

    // Enable or disable all form fields
    const inputs = formElement.querySelectorAll("input, textarea, select");
    inputs.forEach(input => input.disabled = !show);
  }

  // Hides all three contact forms
  function hideAllForms() {
    setFormState(fanForm, false);
    setFormState(artistForm, false);
    setFormState(venueForm, false);
}

  // Watch for changes on dropdown and show the correct form
  if (userTypeSelect) {
    userTypeSelect.addEventListener("change", function () {
      hideAllForms();
      const selected = this.value;
      // Show only the selected form
      if (selected === "fan") setFormState(fanForm, true);
      else if (selected === "artist") setFormState(artistForm, true);
      else if (selected === "venue") setFormState(venueForm, true);
    });

    // Restore form if user had already selected something
    const preselected = userTypeSelect.getAttribute("data-selected");
    if (preselected) {
      userTypeSelect.value = preselected;
      // Triggers the change event manually
      userTypeSelect.dispatchEvent(new Event("change"));
    }
  }

//----------------------------------------------//
// 4. Review Management Forms
//----------------------------------------------//

// Handles the toggling of the review management form
// It allows users to manage their reviews by showing or hiding the form
  document.querySelectorAll("[data-toggle-manage]").forEach(function (button) {
    button.addEventListener("click", function () {

      const reviewId = this.dataset.toggleManage;
      const form = document.getElementById(`manage-form-${reviewId}`);
      if (form) {
        form.classList.toggle("d-none");
      }
    });
  });

  // Hides the review management form if the user clicks a cancel button
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
      if (!confirmDelete()) {
        event.preventDefault();
      }
    });
  });



