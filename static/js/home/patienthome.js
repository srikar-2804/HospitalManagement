document.addEventListener("DOMContentLoaded", () => {
    console.log("Patient Home Page Loaded!");

    // Navbar link hover animation
    const navItems = document.querySelectorAll(".nav-links a");
    navItems.forEach(item => {
        item.addEventListener("mouseover", () => {
            item.style.transform = "scale(1.1)";
            item.style.transition = "transform 0.3s ease, color 0.3s ease";
        });
        item.addEventListener("mouseout", () => {
            item.style.transform = "scale(1)";
        });
    });

    // Button hover animation
    const buttons = document.querySelectorAll(".btn");
    buttons.forEach(button => {
        button.addEventListener("mouseover", () => {
            button.style.transform = "translateY(-3px)";
            button.style.boxShadow = "0 8px 15px rgba(0, 0, 0, 0.2)";
        });
        button.addEventListener("mouseout", () => {
            button.style.transform = "translateY(0)";
            button.style.boxShadow = "0 4px 6px rgba(0, 0, 0, 0.1)";
        });
    });
});
