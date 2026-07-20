document.addEventListener("DOMContentLoaded", () => {

    // Hero Elements
    const leftImage = document.querySelector(".order-2 .placement-hero-img");
    const centerContent = document.querySelector(".col-lg-6");
    const rightImage = document.querySelector(".order-3 .placement-hero-img");

    // Initial State
    if (leftImage) {
        leftImage.style.opacity = "0";
        leftImage.style.transform = "translateX(-200px)";
    }

    if (centerContent) {
        centerContent.style.opacity = "0";
        centerContent.style.transform = "translateY(60px)";
    }

    if (rightImage) {
        rightImage.style.opacity = "0";
        rightImage.style.transform = "translateX(200px)";
    }

    // Animate after page load
    setTimeout(() => {

        if (leftImage) {
            leftImage.style.transition = "all 1s ease";
            leftImage.style.opacity = "1";
            leftImage.style.transform = "translateX(0)";
        }

        setTimeout(() => {

            if (centerContent) {
                centerContent.style.transition = "all 0.8s ease";
                centerContent.style.opacity = "1";
                centerContent.style.transform = "translateY(0)";
            }

        }, 200);

        setTimeout(() => {

            if (rightImage) {
                rightImage.style.transition = "all 1s ease";
                rightImage.style.opacity = "1";
                rightImage.style.transform = "translateX(0)";
            }

        }, 400);

    }, 200);


    // Journey Steps Animation (Scroll)
    const steps = document.querySelectorAll(".placement-step");
    const track = document.querySelector(".placement-journey-track");

    if (track) {

        const observer = new IntersectionObserver((entries) => {

            entries.forEach(entry => {

                if (entry.isIntersecting) {

                    steps.forEach((step, index) => {

                        setTimeout(() => {
                            step.classList.add("show");
                        }, index * 180);

                    });

                    observer.disconnect();

                }

            });

        }, {
            threshold: 0.3
        });

        observer.observe(track);
    }

});


// cards
document.addEventListener("DOMContentLoaded", function () {

    const cards = document.querySelectorAll(".placement-card");

    const observer = new IntersectionObserver(function (entries) {

        entries.forEach(function (entry) {

            if (entry.isIntersecting) {

                cards.forEach(function (card, index) {

                    setTimeout(function () {
                        card.classList.add("show");
                    }, index * 180); 

                });

                observer.unobserve(entry.target);

            }

        });

    }, {
        threshold: 0.2
    });

    observer.observe(document.querySelector(".placement-services-section"));

});
