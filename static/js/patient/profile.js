document.addEventListener('DOMContentLoaded', () => {
    const form = document.querySelector('.profile-form');
    form.addEventListener('submit', (event) => {
        const inputs = form.querySelectorAll('input, textarea');
        let isValid = true;
        inputs.forEach(input => {
            if (!input.value.trim()) {
                isValid = false;
                input.style.border = '1px solid red';
            } else {
                input.style.border = '';
            }
        });
        if (!isValid) {
            event.preventDefault();
            alert('Please fill out all fields before submitting.');
        }
    });
});
