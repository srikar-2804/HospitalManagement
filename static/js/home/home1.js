document.addEventListener("DOMContentLoaded", () => {
    console.log("Website is fully loaded!");

    // Smooth scroll for anchor links
    const links = document.querySelectorAll(".nav-links a");
    links.forEach(link => {
        link.addEventListener("click", function (e) {
            if (this.getAttribute("href").startsWith("#")) {
                e.preventDefault();
                const target = document.querySelector(this.getAttribute("href"));
                target.scrollIntoView({ behavior: "smooth" });
            }
        });
    });

    // Navbar hover effect with scale animation
    const navItems = document.querySelectorAll(".nav-links li a");
    navItems.forEach(item => {
        item.addEventListener("mouseover", () => {
            item.style.transform = "scale(1.2)";
            item.style.transition = "transform 0.3s ease, background 0.3s ease";
        });
        item.addEventListener("mouseout", () => {
            item.style.transform = "scale(1)";
        });
    });

    // Button hover animation in hero section
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
