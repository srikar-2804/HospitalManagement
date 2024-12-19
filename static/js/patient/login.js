document.addEventListener('DOMContentLoaded', () => {
    const messages = document.querySelectorAll('.message');
    setTimeout(() => {
        messages.forEach(message => {
            message.style.opacity = '0';
            setTimeout(() => message.remove(), 500); // Fully remove message after fading
        });
    }, 3000); // Messages will fade out after 3 seconds
});
