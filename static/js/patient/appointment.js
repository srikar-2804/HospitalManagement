// JS for Schedule Appointment Page
// Displays success message and clears form fields upon submission

document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.appointment-form');
    const messageBox = document.querySelector('.message');

    form.addEventListener('submit', (event) => {
        event.preventDefault(); // Prevent form from refreshing the page

        // Simulate successful form submission
        messageBox.textContent = "Appointment scheduled successfully!";

        // Clear form fields
        form.reset();
    });
});
