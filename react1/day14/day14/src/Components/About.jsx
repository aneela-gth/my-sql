import React from "react";

function About() {
  return (
    <section className="about-section">
      <h2 className="about-title">About Me</h2>

      <div className="about-container">
        <p className="about-text">
          I am a passionate <strong>React Developer</strong> with experience in
          building modern, responsive, and user-friendly web applications.
          I enjoy working with clean UI designs and writing reusable,
          maintainable code.
        </p>

        <div className="about-cards">
          <div className="about-card">
            <h3>🎯 Career Goal</h3>
            <p>
              To work as a Frontend / React Developer and contribute to building
              impactful web applications.
            </p>
          </div>

          <div className="about-card">
            <h3>💻 Tech Focus</h3>
            <p>
              React JS, JavaScript, HTML, CSS, Django basics, and REST APIs.
            </p>
          </div>

          <div className="about-card">
            <h3>📚 Learning</h3>
            <p>
              Continuously improving my skills in full-stack development and
              modern UI technologies.
            </p>
          </div>
        </div>
      </div>
    </section>
  );
}

export default About;
