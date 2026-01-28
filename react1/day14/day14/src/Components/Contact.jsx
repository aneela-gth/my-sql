import React from "react";

function Contact() {
  return (
    <section className="contact-section">
      <h2 className="contact-title">Contact Me</h2>

      <div className="contact-cards">
        <div className="contact-card">
          <span>📧</span>
          <h4>Email</h4>
          <p>aneela@gmail.com</p>
        </div>

        <div className="contact-card">
          <span>🐙</span>
          <h4>GitHub</h4>
          <a
            href="https://github.com/aneela"
            target="_blank"
            rel="noreferrer"
          >
            github.com/aneela
          </a>
        </div>

        <div className="contact-card">
          <span>💼</span>
          <h4>LinkedIn</h4>
          <a
            href="https://linkedin.com/in/aneela"
            target="_blank"
            rel="noreferrer"
          >
            linkedin.com/in/aneela
          </a>
        </div>
      </div>
    </section>
  );
}

export default Contact;
