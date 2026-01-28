import React from "react";
import "./Style.css";

const Resume = () => {
  return (
    <section id="resume" className="resume-section">
      <h2 className="resume-title">My Resume</h2>

      <div className="resume-container">
        <iframe
          src="https://drive.google.com/file/d/17KWr1PhUCczFVJwzHqVirOudeptSa-AP/preview"
          title="Bandi Aneela Resume"
          className="resume-frame"
          allow="autoplay"
        ></iframe>
      </div>

      <div className="resume-buttons">
        <a
          href="https://drive.google.com/file/d/17KWr1PhUCczFVJwzHqVirOudeptSa-AP/view?usp=sharing"
          target="_blank"
          rel="noopener noreferrer"
          className="resume-btn"
        >
          👁 View on Google Drive
        </a>

        <a
          href="https://drive.google.com/uc?export=download&id=17KWr1PhUCczFVJwzHqVirOudeptSa-AP"
          className="resume-btn"
        >
          📄 Download Resume
        </a>
      </div>
    </section>
  );
};

export default Resume;



