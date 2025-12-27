
// Movie list with images
const movies = [
    { name: "Pushpa", image: "images/pushpa.jpg" },
    { name: "RRR", image: "images/rrr.jpg" },
    { name: "Bahubali", image: "images/bahubali.jpg" },
    { name: "Salaar", image: "images/salaar.jpg" },
    { name: "KGF", image: "images/kgf.jpg" },
    { name: "Avatar", image: "images/avatar.jpg" },
    { name: "Inception", image: "images/inception.jpg" },
    { name: "Interstellar", image: "images/interstellar.jpg" }
];

// Elements
const searchInput = document.querySelector(".search-box input");
const searchResults = document.getElementById("searchResults");

// Search functionality
searchInput.addEventListener("input", () => {
    const query = searchInput.value.toLowerCase();
    searchResults.innerHTML = "";

    if (query === "") {
        searchResults.style.display = "none";
        return;
    }

    const filteredMovies = movies.filter(movie =>
        movie.name.toLowerCase().includes(query)
    );

    if (filteredMovies.length === 0) {
        searchResults.innerHTML = `<div class="result-item">
            <span>No results found</span>
        </div>`;
    } else {
        filteredMovies.forEach(movie => {
            const div = document.createElement("div");
            div.className = "result-item";

            div.innerHTML = `
                <img src="${movie.image}" alt="${movie.name}">
                <span>${movie.name}</span>
            `;

            div.onclick = () => {
                alert(`You selected: ${movie.name}`);
            };

            searchResults.appendChild(div);
        });
    }

    searchResults.style.display = "block";
});

// Multiple images list
const slides = [
    {
        img: "images/image2.webp",
        title: "Most Popular Indian Directors of 2025"
    },
    {
        img: "images/image4.jpg",
        title: "Top Trending South Indian Directors"
    },
    {
        img: "images/image3.jpg",
        title: "Bollywood Directors Making a Comeback"
    },
    {
        img: "OIP.webp",
        title: "New Age Directors Changing Indian Cinema"
    },
    {
        img: "image1.webp",
        title: "New Age Directors Changing Indian Cinema"
    }
    // Add more here...
];

let current = 0;

// Update slide
function showSlide() {
    document.getElementById("heroImage").src = slides[current].img;
    document.getElementById("heroTitle").innerText = slides[current].title;
}

// Next & Prev
function nextSlide() {
    current = (current + 1) % slides.length;
    showSlide();
}

function prevSlide() {
    current = (current - 1 + slides.length) % slides.length;
    showSlide();
}

// Load first image
showSlide();

// Optio
// ----------------------------------------------
document.querySelectorAll(".play-btn-small").forEach(btn => {
    btn.onclick = () => alert("Playing trailer...");
});
// UNLIMITED IMAGES ARRAY
const sliderImages = [
    {
        img: "images/image8.jpg",
        title: "Top 10 Indian Stars",
        link: "#"
    },
    {
        img: "images/image15.jpg",
        title: "Best Movies 2025",
        link: "#"
    },
    {
        img: "images/image7.jpeg",
        title: "Thunderbolts Trailer",
        link: "#"
    },
    {
        img: "images/image19.jpg",
        title: "Upcoming Releases",
        link: "#"
    },
    {
        img: "images/image20.jpeg",
        title: "Top Web Series",
        link: "#"
    },
    {
        img: "images/image12.jpg",
        title: "Action Trailers",
        link: "#"
    },
    {
        img: "images/image21.jpg",
        title: "Most Watched",
        link: "#"
    },

    // ⭐ ADD MORE IMAGES HERE ⭐
];


// IMAGE LIST (Add as many as you want)
const images = [
    "images/image11.jpg",
    "images/image13.webp",
    "images/image8.jpg",
    "images/image15.jpg",
    "images/image16.jpg",
    "images/image17.jpg",
    "images/image7.jpg",
    "images/image13.webp"
];

// SELECT ELEMENTS
const slider = document.getElementById("slider");
const nextBtn = document.querySelector(".next");
const prevBtn = document.querySelector(".prev");

// LOAD IMAGES INSIDE SLIDER
function loadImages() {
    images.forEach(img => {
        const div = document.createElement("div");
        div.classList.add("slide-item");

        div.innerHTML = `
            <img src="${img}" alt="movie">
        `;
        slider.appendChild(div);
    });
}

loadImages();

// SCROLL SETTINGS
let scrollAmount = 0;
const scrollStep = 350; // Scroll size

// NEXT BUTTON
nextBtn.addEventListener("click", () => {
    slider.scrollBy({
        left: scrollStep,
        behavior: "smooth"
    });
});

// PREVIOUS BUTTON
prevBtn.addEventListener("click", () => {
    slider.scrollBy({
        left: -scrollStep,
        behavior: "smooth"
    });
});
// BEST OF 2025 ANIMATION
const bestSection = document.querySelector(".second-line");

window.addEventListener("scroll", () => {
    const sectionTop = bestSection.getBoundingClientRect().top;
    const trigger = window.innerHeight - 150;

    if (sectionTop < trigger) {
        bestSection.classList.add("show");
    }
});
// ------------------------------
// 3 page
window.onload = () => {
    let slider = document.querySelector(".celeb-slider");
    let nextBtn = document.querySelector(".next-btn");

    nextBtn.addEventListener("click", () => {
        slider.scrollBy({
            left: 300,
            behavior: "smooth"
        });
    });
};

// -------------------------------
// 4page
// Optional interaction
document.querySelectorAll(".card").forEach(card => {
    card.addEventListener("click", () => {
        alert("Movie clicked!");
    });
});

// -------------------------------------
// 5
document.addEventListener("DOMContentLoaded", function () {
    const slider = document.getElementById("movieSlider");
    const nextBtn = document.querySelector(".next");
    const prevBtn = document.querySelector(".prev");

    nextBtn.addEventListener("click", function () {
        slider.scrollLeft += 300;
    });

    prevBtn.addEventListener("click", function () {
        slider.scrollLeft -= 300;
    });
});
// ----------------------------------------
// 6
document.addEventListener("DOMContentLoaded", () => {

    /* ======================
       TRAILER ON / OFF
    ====================== */
    const trailerButtons = document.querySelectorAll(".btn.outline");

    trailerButtons.forEach(button => {
        button.addEventListener("click", () => {

            const card = button.closest(".movie-card");
            let video = card.querySelector("video");

            if (!video) {
                // ON → Create & Play video
                video = document.createElement("video");
                video.src = "sample.mp4"; // replace with real video
                video.controls = true;
                video.autoplay = true;
                video.muted = true;
                video.style.width = "100%";
                video.style.marginTop = "10px";

                card.appendChild(video);
                button.textContent = "⏸ Stop Trailer";
            } else {
                // OFF → Stop & Remove video
                video.pause();
                video.remove();
                button.textContent = "▶ Trailer";
            }
        });
    });

    /* ======================
       WATCH OPTIONS ON / OFF
    ====================== */
    const watchButtons = document.querySelectorAll(".btn:not(.outline)");

    watchButtons.forEach(button => {
        button.addEventListener("click", () => {

            const card = button.closest(".movie-card");
            let options = card.querySelector(".watch-options");

            if (!options) {
                // ON → Create options
                options = document.createElement("div");
                options.className = "watch-options";
                options.innerHTML = `
                    <p>Available on:</p>
                    <ul>
                        <li>▶ Amazon Prime</li>
                        <li>▶ Netflix</li>
                        <li>▶ Disney+</li>
                    </ul>
                `;

                card.appendChild(options);
                button.textContent = "Hide options";
            } else {
                // OFF → Remove options
                options.remove();
                button.textContent = "Watch options";
            }
        });
    });

});



// ---------------------------
// 7
document.addEventListener("DOMContentLoaded", () => {

    const slider = document.querySelector(".slider");
    const leftBtn = document.querySelector(".arrow.left");
    const rightBtn = document.querySelector(".arrow.right");

    const scrollAmount = 300; // width of one card

    // Scroll Right
    rightBtn.addEventListener("click", () => {
        slider.scrollBy({
            left: scrollAmount,
            behavior: "smooth"
        });
    });

    // Scroll Left
    leftBtn.addEventListener("click", () => {
        slider.scrollBy({
            left: -scrollAmount,
            behavior: "smooth"
        });
    });

    // Hide/Show arrows
    function updateButtons() {
        leftBtn.style.display = slider.scrollLeft <= 0 ? "none" : "block";

        rightBtn.style.display =
            slider.scrollLeft + slider.clientWidth >= slider.scrollWidth
                ? "none"
                : "block";
    }

    slider.addEventListener("scroll", updateButtons);
    updateButtons();
});
document.addEventListener("DOMContentLoaded", () => {

    const cards = document.querySelectorAll(".card");
    const detailsView = document.getElementById("detailsView");

    const detailsImg = document.getElementById("detailsImg");
    const detailsTitle = document.getElementById("detailsTitle");
    const detailsDesc = document.getElementById("detailsDesc");
    const backBtn = document.getElementById("backBtn");

    cards.forEach(card => {
        card.addEventListener("click", () => {
            detailsImg.src = card.dataset.img;
            detailsTitle.textContent = card.dataset.title;
            detailsDesc.textContent = card.dataset.desc;

            detailsView.classList.add("active");
        });
    });

    backBtn.addEventListener("click", () => {
        detailsView.classList.remove("active");
    });

});
// ------------------------------------------
