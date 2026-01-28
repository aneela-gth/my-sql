import React from "react";
import "./style.css";

const Projects = () => {
  return (
    <section id="projects" className="projects">
      <h2 className="section-title">My Projects</h2>

      {/* PROJECT 1 */}
      <div className="project-card glass">
        <div className="project-header">
          <h3>Notes Getting & Uploading App</h3>
          <span className="tag backend">Full Stack</span>
        </div>

        <p className="project-desc">
          A Python Full Stack application that allows users to upload, store,
          and download notes securely. Built mainly for students to manage
          academic materials easily.
        </p>

        <div className="timeline">
          <p>✔ User authentication</p>
          <p>✔ Upload & download notes (PDF / Images)</p>
          <p>✔ Django REST API integration</p>
          <p>✔ Secure file storage</p>
        </div>

        <p className="tech">
          <strong>Tech Stack:</strong> React, Python, Django, REST API, MySQL
        </p>

        <div className="project-links">
          <a href="#" target="_blank">Live Demo</a>
          <a href="#" target="_blank">Source Code</a>
        </div>
      </div>

      {/* PROJECT 2 */}
      <div className="project-card gradient">
        <div className="project-header">
          <h3>I-Studio Website</h3>
          <span className="tag frontend">Frontend</span>
        </div>

        <p className="project-desc">
          A modern and responsive business portfolio website developed for a
          client to showcase services, work, and contact information.
        </p>

        <div className="timeline">
          <p>✔ Clean & modern UI</p>
          <p>✔ Fully responsive design</p>
          <p>✔ Smooth navigation</p>
          <p>✔ SEO-friendly structure</p>
        </div>

        <p className="tech">
          <strong>Tech Stack:</strong> HTML, CSS
        </p>

        <div className="project-links">
          <a href="#" target="_blank">Live Demo</a>
          <a href="#" target="_blank">Source Code</a>
        </div>
      </div>
    </section>
  );
};

export default Projects;
