document.addEventListener("DOMContentLoaded", () => {

    const slides = document.querySelectorAll(".slide");
    const next = document.querySelector(".next");
    const prev = document.querySelector(".prev");

    let current = 0;

    function showSlide(index) {
        slides.forEach(slide => slide.classList.remove("active"));
        current = (index + slides.length) % slides.length;
        slides[current].classList.add("active");
    }

    next.addEventListener("click", () => showSlide(current + 1));
    prev.addEventListener("click", () => showSlide(current - 1));

    setInterval(() => {
        showSlide(current + 1);
    }, 5000);

});

/* ==========================
   Sticky Header
========================== */

const header = document.querySelector("#encabezado");

let lastScroll = 0;

window.addEventListener("scroll", () => {

    const currentScroll = window.pageYOffset;

    // Background

    if(currentScroll > 20){

        header.classList.add("scrolled");

    }else{

        header.classList.remove("scrolled");

    }

    // Hide while scrolling down

    if(currentScroll > lastScroll && currentScroll > 150){

        header.classList.add("hide");

    }else{

        header.classList.remove("hide");

    }

    lastScroll = currentScroll;

})

/* ==========================
   Fade Sections
========================== */

const observer = new IntersectionObserver(entries => {

    entries.forEach(entry => {

        if(entry.isIntersecting){

            entry.target.classList.add("show");

        }

    });

});

const hiddenElements = document.querySelectorAll(".hidden");

hiddenElements.forEach(el => observer.observe(el));