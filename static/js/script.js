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
