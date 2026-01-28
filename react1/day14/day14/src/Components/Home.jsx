import React from "react";

function Home() {
  return (
  
    <section className="hero">
      <div className="hero-left">
        <h1>
          Hi I'm <span>Aneela</span>
        </h1>

        <h2>React Developer</h2>

        <p>
          Passionate Full Stack Developer focused on building
          modern, scalable and user-friendly web applications.
        </p>

        <div className="hero-buttons">
          <a href="#projects" className="btn primary">Explore Work</a>
          <a href="/Aneela_Resume.pdf" target="_blank" className="btn outline">
            Resume
          </a>
        </div>
      </div>

      <div className="hero-right">
        <div className="profile-ring">
          <img src="WhatsApp Image 2025-08-26 at 09.48.07_ba809a75.jpg" alt="Aneela" />
        </div>
      </div>
    </section>
  );
}

export default Home;
