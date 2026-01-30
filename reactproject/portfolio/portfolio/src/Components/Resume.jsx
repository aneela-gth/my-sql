import React from "react";
import "./Resume.css";

const Resume = () => {
  return (
    <section id="resume" className="resume-section">
      <h2 className="resume-title">My Resume</h2>

      <div className="resume-container">
        <iframe
          src="https://docs.google.com/document/d/12oQBp68MbzSsr7XeKzdTjTgyyh1ckdYY/preview"
          title="Bandi Aneela Resume"
          className="resume-frame"
          allow="autoplay"
        ></iframe>
      </div>

      <div className="resume-buttons">
        <a
          href="https://docs.google.com/document/d/12oQBp68MbzSsr7XeKzdTjTgyyh1ckdYY/view"
          target="_blank"
          rel="noopener noreferrer"
          className="resume-btn"
        >
          👁 View Resume
        </a>

        <a
          href="https://docs.google.com/document/d/12oQBp68MbzSsr7XeKzdTjTgyyh1ckdYY/export?format=pdf"
          className="resume-btn"
        >
          📄 Download PDF
        </a>
      </div>
    </section>
  );
};

export default Resume;

