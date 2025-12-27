document.addEventListener("DOMContentLoaded", () => {
    // ===== HERO IMAGE SLIDER =====
    const images = [
        "images copy/image2.webp",
        "images copy/image1.webp",
        "images copy/image4.jpg",
        "images copy/image3.jpg",
        "images copy/image14.jpg",
        "images copy/image15.jpg",
        "images copy/image19.jpg",
        "images copy/image21.jpg",
        "images copy/image22.jpg",
        "images copy/OIP.webp"

    ];

    let currentIndex = 0;
    const heroImg = document.querySelector(".hero-img");
    const leftArrow = document.querySelector(".arrow.left");
    const rightArrow = document.querySelector(".arrow.right");

    rightArrow.addEventListener("click", () => {
        currentIndex = (currentIndex + 1) % images.length;
        heroImg.src = images[currentIndex];
    });

    leftArrow.addEventListener("click", () => {
        currentIndex = (currentIndex - 1 + images.length) % images.length;
        heroImg.src = images[currentIndex];
    });

});

document.querySelectorAll(".up-item").forEach(item => {
    item.addEventListener("click", () => {
        alert("Play trailer (demo)");
    });
});
document.addEventListener("DOMContentLoaded", () => {

    const heroLeft = document.querySelector(".hero-left");
    const heroImg = document.querySelector(".hero-img");
    const playBtn = document.querySelector(".play-btn");

    // CREATE VIDEO ELEMENT
    const heroVideo = document.createElement("video");
    heroVideo.src = "videos/video1.mp4"; // path to your video
    heroVideo.className = "hero-video";
    heroVideo.muted = true;
    heroVideo.loop = true;

    // ADD VIDEO TO HERO
    heroLeft.insertBefore(heroVideo, heroLeft.firstChild);

    // INITIAL STATE
    heroVideo.style.display = "none"; // hide video initially

    // PLAY / PAUSE BUTTON
    playBtn.addEventListener("click", () => {
        if (!heroVideo.paused) {
            heroVideo.pause();
            heroVideo.style.display = "none"; // hide video
            heroImg.style.display = "block";   // show image
            playBtn.textContent = "▶";         // change button to play
        } else {
            heroImg.style.display = "none";    // hide image
            heroVideo.style.display = "block"; // show video
            heroVideo.play();
            playBtn.textContent = "⏸";         // change button to pause
        }
    });

});


// ----------------------------------------------------------------------
// second page //
const slider = document.getElementById("slider");

/* ===== IMAGE DATA ===== */
const cardsData = [
  {
    img: "images copy/image8.jpg",
    title: "The Top 10 Most Popular Indian Stars of 2025",
    link: "See the gallery"
  },
  {
    img: "images copy/image13.webp",
    title: "The Most Popular Movies of 2025",
    link: "See the list"
  },
  {
    img: "images copy/image16.jpg",
    title: "Sinners (2025)",
    link: "View details"
  },
  {
    img: "images copy/image18.jpg",
    title: "Thunderbolts*",
    link: "Coming soon"
  },
  {
    img: "images copy/image16.jpg",
    title: "Sinners (2025)",
    link: "View details"
  },
  {
    img: "images copy/image13.webp",
    title: "The Most Popular Movies of 2025",
    link: "See the list"
  },
   {
    img: "images copy/image8.jpg",
    title: "The Top 10 Most Popular Indian Stars of 2025",
    link: "See the gallery"
  },
];

/* ===== CREATE CARDS ===== */
cardsData.forEach(item => {
  const card = document.createElement("div");
  card.className = "card";

  card.innerHTML = `
    <img src="${item.img}">
    <p>${item.title}</p>
    <span>${item.link}</span>
  `;

  slider.appendChild(card);
});

/* ===== SLIDER BUTTONS ===== */
function slideLeft() {
  slider.scrollBy({
    left: -260,
    behavior: "smooth"
  });
}

function slideRight() {
  slider.scrollBy({
    left: 260,
    behavior: "smooth"
  });
}
// --------------------------------------
// page3
document.querySelectorAll(".play-btn-small").forEach(btn => {
    btn.onclick = () => alert("Playing trailer...");
});
// UNLIMITED IMAGES ARRAY
const sliderImages = [
    {
        img: "images copy/image13.webp",
        title: "Top 10 Indian Stars",
        link: "#"
    },
    {
        img: "images copy/image13.webp",
        title: "Best Movies 2025",
        link: "#"
    },
    {
        img: "images copy/image13.webp",
        title: "Thunderbolts Trailer",
        link: "#"
    },
    {
        img: "images copy/image13.webp",
        title: "Upcoming Releases",
        link: "#"
    },
    {
        img: "images copy/image13.webp",
        title: "Top Web Series",
        link: "#"
    },
    {
        img: "images copy/image13.webp",
        title: "Action Trailers",
        link: "#"
    },
    {
        img: "images copy/image13.webp",
        title: "Most Watched",
        link: "#"
    },

];

// --------------------------------------------------
// page4
// ⭐ Movie Posters Array
const movies = [
  { img: "images copy/image16.jpg", title: "Stranger Things 5", video: "videos/video1.mp4" },
  { img: "images copy/image16.jpg", title: "Pluribus", video: "videos/video1.mp4" },
   { img: "images copy/image16.jpg", title: "Stranger Things 5", video: "videos/video1.mp4" },
  { img: "images copy/image16.jpg", title: "Pluribus", video: "videos/video1.mp4" },
   { img: "images copy/image16.jpg", title: "Stranger Things 5", video: "videos/video1.mp4" },
  { img: "images copy/image16.jpg", title: "Pluribus", video: "videos/video1.mp4" },
  // add more...
];


// ⭐ Display Movie Cards
movies.forEach(movie => {
  movieList.innerHTML += `
    <div class="card">
      <img src="${movie.img}" alt="${movie.title}">
      <h3 class="title">${movie.title}</h3>
      <button class="play-btn" data-video="${movie.video}">▶ Trailer</button>
    </div>
  `;
});

// ⭐ Modal & Video Elements
const modal = document.getElementById("videoModal");
const trailerVideo = document.getElementById("trailerVideo");

// 🎬 PLAY / STOP TOGGLE BUTTON
document.addEventListener("click", (e) => {
  if (e.target.classList.contains("play-btn")) {

    const videoFile = e.target.getAttribute("data-video");

    // If video is closed → open & play
    if (modal.style.display !== "flex") {
      trailerVideo.src = videoFile;
      modal.style.display = "flex";
      trailerVideo.play();
      e.target.textContent = "⏸ Stop Trailer"; // button text change
    }
    // If video is open → close & stop
    else {
      trailerVideo.pause();
      trailerVideo.currentTime = 0;
      modal.style.display = "none";
      e.target.textContent = "▶ Trailer"; // back to play text
    }
  }
});


modal.addEventListener("click", (event) => {
  if (event.target === modal) {
    trailerVideo.pause();
    trailerVideo.currentTime = 0;
    modal.style.display = "none";
  }
});

// ------------------
const movies3= [
  { img: "images/avatar.jpg", title: "Avatar: Fire and Ash", year: 2025, rating: "⭐7.5" },
  { img: "images/wake.jpg", title: "Wake Up Dead Man", year: 2025, rating: "⭐7.4" },
  { img: "images/stranger.jpg", title: "Stranger Things", year: "2016-2025", rating: "⭐8.6" },
  { img: "images/pluribus.jpg", title: "Pluribus", year: 2025, rating: "⭐7.3" },
  { img: "images/it.jpg", title: "IT: Welcome to Derry", year: 2025, rating: "⭐8.2" },
  { img: "images/fallout.jpg", title: "Fallout", year: 2024, rating: "⭐8.4" },
  { img: "images/battle.jpg", title: "One Battle After Another", year: 2025, rating: "⭐7.1" },
  { img: "images/dhurandhar.jpg", title: "Dhurandhar", year: 2025, rating: "⭐7.0" },
  { img: "images/heated.jpg", title: "Heated Rivalry", year: 2025, rating: "⭐6.9" },
  { img: "images/housemaid.jpg", title: "The Housemaid", year: 2025, rating: "⭐7.0" }
];

const container = document.getElementById("movieContainer");

movies.forEach(movie3 => {
  container.innerHTML += `
    <div class="card">
      <img src="${movie3.img}" alt="${movie3.title}">
      <h3>${movie3.title}</h3>
      <p>${movie3.year} • ${movie3.rating}</p>
    </div>
  `;
});
// ------------------------------------------------------
// page4
// Movie Data
const moviesInTheaters = [
  { img: "images copy/image23.jpg", title: "Stranger Things 5", video: "videos/video1.mp4", rate: "⭐7.5" },
  { img: "images copy/image23.jpg", title: "Akhanda 2 - Thaandavam", video: "videos/video1.mp4", rate: "⭐7.0" },
  { img: "images copy/image23.jpg", title: "Dhurandhar", video: "videos/video1.mp4", rate: "⭐8.6" },
  { img: "images copy/image23.jpg", title: "Champion", video: "videos/video1.mp4", rate: "⭐6.0" },
  { img: "images copy/image23.jpg", title: "Shambhala", video: "videos/video1.mp4", rate: "⭐6.8" },
  { img: "images copy/image23.jpg", title: "Anaconda", video: "videos/video1.mp4", rate: "⭐6.2" },
   { img: "images copy/image23.jpg", title: "Shambhala", video: "videos/video1.mp4", rate: "⭐6.8" },
  { img: "images copy/image23.jpg", title: "Anaconda", video: "videos/video1.mp4", rate: "⭐6.2" },
   { img: "images copy/image23.jpg", title: "Shambhala", video: "videos/video1.mp4", rate: "⭐6.8" },
  { img: "images copy/image23.jpg", title: "Anaconda", video: "videos/video1.mp4", rate: "⭐6.2" },
];

const theaterBox = document.getElementById("theaterMovieBox");

moviesInTheaters.forEach((movie, index) => {
  // Create card
  const card = document.createElement("div");
  card.classList.add("movie-card-box");
  card.innerHTML = `
    <img class="movie-poster" src="${movie.img}" />
    <p class="movie-rating">${movie.rate}</p>
    <p class="movie-title">${movie.title}</p>

    <video id="video${index}" class="trailer-video" src="${movie.video}" width="250" style="display:none;"></video>

    <button class="show-btn">🎬 Showtimes</button>
    <button class="trailer-btn">▶ Play</button>
    <button class="back-btn" style="display:none;">⬅ Back</button>
  `;

  theaterBox.appendChild(card);

  const video = card.querySelector(`#video${index}`);
  const playBtn = card.querySelector(".trailer-btn");
  const backBtn = card.querySelector(".back-btn");

  playBtn.addEventListener("click", () => {
    video.style.display = "block";
    backBtn.style.display = "inline-block";
    playBtn.style.display = "none";
    video.play();
  });

  backBtn.addEventListener("click", () => {
    video.pause();
    video.currentTime = 0;
    video.style.display = "none";
    backBtn.style.display = "none";
    playBtn.style.display = "inline-block";
  });
});

// Back to top button
const backToTopBtn = document.getElementById("backToTop");
window.addEventListener("scroll", () => {
  backToTopBtn.style.display = window.scrollY > 300 ? "block" : "none";
});

backToTopBtn.addEventListener("click", () => {
  window.scrollTo({ top: 0, behavior: "smooth" });
});


// --------------------------------------------pending html code
// page5//

// CATEGORY DATA
const data = {
  trending: [
    {img:"images copy/image11.jpg", title:"Disclosure Day", time:"2:06", video:"videos/1.mp4", date:"June 12, 2026"},
    {img:"images copy/image11.jpg", title:"Street Fighter", time:"0:45", video:"videos/2.mp4", date:"Oct 16, 2026"},
    {img:"images copy/image11.jpg", title:"Young Sherlock", time:"1:32", video:"videos/3.mp4", date:"March 4, 2026"},
    {img:"images copy/image11.jpg", title:"Disclosure Day", time:"2:06", video:"videos/1.mp4", date:"June 12, 2026"},
    {img:"images copy/image11.jpg", title:"Street Fighter", time:"0:45", video:"videos/2.mp4", date:"Oct 16, 2026"},
    {img:"images copy/image11.jpg", title:"Young Sherlock", time:"1:32", video:"videos/3.mp4", date:"March 4, 2026"},
    {img:"images copy/image11.jpg", title:"Disclosure Day", time:"2:06", video:"videos/1.mp4", date:"June 12, 2026"},
    {img:"images copy/image11.jpg", title:"Street Fighter", time:"0:45", video:"videos/2.mp4", date:"Oct 16, 2026"},
    {img:"images copy/image11.jpg", title:"Young Sherlock", time:"1:32", video:"videos/3.mp4", date:"March 4, 2026"},
    {img:"images copy/image11.jpg", title:"Disclosure Day", time:"2:06", video:"videos/1.mp4", date:"June 12, 2026"},
    {img:"images copy/image11.jpg", title:"Street Fighter", time:"0:45", video:"videos/2.mp4", date:"Oct 16, 2026"},
    {img:"images copy/image11.jpg", title:"Young Sherlock", time:"1:32", video:"videos/3.mp4", date:"March 4, 2026"},

  ],
  anticipated: [
    {img:"images/supergirl.jpg", title:"Supergirl", time:"2:02", video:"videos/4.mp4", date:"June 26, 2026"},
    {img:"images/spiderman.jpg", title:"Spider-Man", time:"0:09", video:"videos/5.mp4", date:"Jul 31, 2026"},
    {img:"images/supergirl.jpg", title:"Supergirl", time:"2:02", video:"videos/4.mp4", date:"June 26, 2026"},
    {img:"images/spiderman.jpg", title:"Spider-Man", time:"0:09", video:"videos/5.mp4", date:"Jul 31, 2026"},
    {img:"images/supergirl.jpg", title:"Supergirl", time:"2:02", video:"videos/4.mp4", date:"June 26, 2026"},
    {img:"images/spiderman.jpg", title:"Spider-Man", time:"0:09", video:"videos/5.mp4", date:"Jul 31, 2026"},
    {img:"images/supergirl.jpg", title:"Supergirl", time:"2:02", video:"videos/4.mp4", date:"June 26, 2026"},
    {img:"images/spiderman.jpg", title:"Spider-Man", time:"0:09", video:"videos/5.mp4", date:"Jul 31, 2026"},
    {img:"images/supergirl.jpg", title:"Supergirl", time:"2:02", video:"videos/4.mp4", date:"June 26, 2026"},
    {img:"images/spiderman.jpg", title:"Spider-Man", time:"0:09", video:"videos/5.mp4", date:"Jul 31, 2026"},

    
  ],
  popular: [
    {img:"images/anaconda.jpg", title:"Anaconda", time:"1:20", video:"videos/6.mp4", date:"Dec 25, 2025"},
    {img:"images/anaconda.jpg", title:"Anaconda", time:"1:20", video:"videos/6.mp4", date:"Dec 25, 2025"},
    {img:"images/anaconda.jpg", title:"Anaconda", time:"1:20", video:"videos/6.mp4", date:"Dec 25, 2025"},
    {img:"images/anaconda.jpg", title:"Anaconda", time:"1:20", video:"videos/6.mp4", date:"Dec 25, 2025"},
    {img:"images/anaconda.jpg", title:"Anaconda", time:"1:20", video:"videos/6.mp4", date:"Dec 25, 2025"},
    {img:"images/anaconda.jpg", title:"Anaconda", time:"1:20", video:"videos/6.mp4", date:"Dec 25, 2025"},
    {img:"images/anaconda.jpg", title:"Anaconda", time:"1:20", video:"videos/6.mp4", date:"Dec 25, 2025"},
    {img:"images/anaconda.jpg", title:"Anaconda", time:"1:20", video:"videos/6.mp4", date:"Dec 25, 2025"},
    {img:"images/anaconda.jpg", title:"Anaconda", time:"1:20", video:"videos/6.mp4", date:"Dec 25, 2025"},
    {img:"images/anaconda.jpg", title:"Anaconda", time:"1:20", video:"videos/6.mp4", date:"Dec 25, 2025"},
    {img:"images/anaconda.jpg", title:"Anaconda", time:"1:20", video:"videos/6.mp4", date:"Dec 25, 2025"},
    {img:"images/anaconda.jpg", title:"Anaconda", time:"1:20", video:"videos/6.mp4", date:"Dec 25, 2025"}

  ],
  recent: [
    {img:"images/disclosure.jpg", title:"Movie Memories", time:"6:35", video:"videos/7.mp4", date:"Jan 10, 2026"},
     {img:"images/disclosure.jpg", title:"Movie Memories", time:"6:35", video:"videos/7.mp4", date:"Jan 10, 2026"},
    {img:"images/disclosure.jpg", title:"Movie Memories", time:"6:35", video:"videos/7.mp4", date:"Jan 10, 2026"},
    {img:"images/disclosure.jpg", title:"Movie Memories", time:"6:35", video:"videos/7.mp4", date:"Jan 10, 2026"},
    {img:"images/disclosure.jpg", title:"Movie Memories", time:"6:35", video:"videos/7.mp4", date:"Jan 10, 2026"},
    {img:"images/disclosure.jpg", title:"Movie Memories", time:"6:35", video:"videos/7.mp4", date:"Jan 10, 2026"},
    {img:"images/disclosure.jpg", title:"Movie Memories", time:"6:35", video:"videos/7.mp4", date:"Jan 10, 2026"},
    {img:"images/disclosure.jpg", title:"Movie Memories", time:"6:35", video:"videos/7.mp4", date:"Jan 10, 2026"}
  ]
};

const box = document.getElementById("trailerContainer");

// LOAD CATEGORY
function loadCategory(type, tab){
  document.querySelectorAll(".trailerTabs span").forEach(t=>t.classList.remove("activeTab"));
  tab.classList.add("activeTab");

  box.innerHTML="";
  data[type].forEach(movie=>{
    box.innerHTML += `
    <div class="trailerCard">
      <img src="${movie.img}">
      <div class="trailerTime" onclick="playVideo('${movie.video}')">▶ ${movie.time}</div>
      <div class="trailerDetails">
        <h3>${movie.title}</h3>
        <p>${movie.date}</p>
      </div>
    </div>`;
  });
}

// SLIDER
function goLeft(){ box.scrollBy({left:-300,behavior:"smooth"}); }
function goRight(){ box.scrollBy({left:300,behavior:"smooth"}); }

// VIDEO POPUP
function playVideo(src){
  document.getElementById("videoPopup").style.display="flex";
  const video = document.getElementById("player");
  video.src = src;
  video.play();
}
function closeVideo(){
  document.getElementById("videoPopup").style.display="none";
  document.getElementById("player").pause();
}

// DEFAULT LOAD
loadCategory("trending", document.querySelector(".activeTab"));
// ----------------------------------------------------------------------
// page6
// ⭐ Updated People Data (Edit here)
const birthdayPeople = [
  { img: "images copy/image18.jpg", fullName: "Person One", years: 39 },
  { img: "images copy/image18.jpg", fullName: "Person Two", years: 45 },
  { img: "images copy/image18.jpg", fullName: "Person Three", years: 30 },
  { img: "images copy/image18.jpg", fullName: "Person Four", years: 28 },
  { img: "images copy/image18.jpg", fullName: "Person Five", years: 41 },
  { img: "images copy/image18.jpg", fullName: "Person Six", years: 33 },
    { img: "images copy/image18.jpg", fullName: "Person Five", years: 41 },
  { img: "images copy/image18.jpg", fullName: "Person Six", years: 33 },
    { img: "images copy/image18.jpg", fullName: "Person Five", years: 41 },
  { img: "images copy/image18.jpg", fullName: "Person Six", years: 33 },
    { img: "images copy/image18.jpg", fullName: "Person Five", years: 41 },
  
];

// ⭐ NEW Display Class Names
const scrollContainer = document.getElementById("scroll-container");

birthdayPeople.forEach(person => {
  scrollContainer.innerHTML += `
    <div class="birthday-card">
      <img src="${person.img}" alt="">
      <h3 class="person-name">${person.fullName}</h3>
      <p class="person-age">${person.years}</p>
    </div>
  `;
});

// ⭐ NEW Button Functions
function moveLeft(){ scrollContainer.scrollBy({ left: -200, behavior: "smooth" }); }
function moveRight(){ scrollContainer.scrollBy({ left: 200, behavior: "smooth" }); }
// ------------------------------------
// ⭐ NEWS DATA
const newsArticles = [
  {
    img:"images/news1.jpg",
    title:"Disney Box Office Hits Record Break",
    desc:"Disney crosses $6 Billion global box office milestone...",
    date:"Dec 24",
    type:"top"
  },
  {
    img:"images/news2.jpg",
    title:"Pat Finn Dies at 60",
    desc:"'The Middle' and 'Seinfeld' actor passes away...",
    date:"Dec 24",
    type:"celebrity"
  },
  {
    img:"images/news3.jpg",
    title:"Ranveer Singh's 'Dhurandhar 2'",
    desc:"Releases 2026, expands to five languages...",
    date:"Dec 24",
    type:"movie"
  },
  {
    img:"images/news4.jpg",
    title:"Peaky Blinders Movie Trailer Out",
    desc:"Cillian Murphy returns as Tommy Shelby...",
    date:"Dec 24",
    type:"tv"
  }
];

const newsBox = document.getElementById("newsList");

// ⭐ DISPLAY NEWS
function loadNews(list){
  newsBox.innerHTML = "";
  list.forEach(n=>{
    newsBox.innerHTML += `
      <div class="news-card">
        <img src="${n.img}">
        <div class="news-info">
          <h3>${n.title}</h3>
          <p>${n.desc}</p>
          <span>${n.date}</span>
        </div>
      </div>
    `;
  });
}

loadNews(newsArticles); // default load

// ⭐ FILTER BUTTON FUNCTION
function filterNews(type){
  const filtered = newsArticles.filter(n => n.type === type);
  loadNews(filtered.length ? filtered : newsArticles);
}
function openPage(page){
  window.location.href = page;
}