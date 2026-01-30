import React from "react";

const Contact = () => {
  return (
    <section id="contact" className="contact-section">
      <h2 className="contact-title">Contact Me</h2>
      <p className="contact-subtitle">
        Feel free to reach out for collaborations or opportunities
      </p>

      <div className="contact-grid">
        {/* Email */}
        <div className="contact-card">
          <div className="contact-icon">📧</div>
          <h3>Email</h3>
          <p>aneelabandi9951@gmail.com</p>
        </div>

        {/* Phone */}
        <div className="contact-card">
          <div className="contact-icon">📞</div>
          <h3>Phone</h3>
          <p>+91 7674087691</p>
        </div>

        {/* Location */}
        <div className="contact-card">
          <div className="contact-icon">📍</div>
          <h3>Location</h3>
          <p>Hyderabad, India</p>
        </div>

        {/* GitHub */}
        <div className="contact-card">
          <div className="contact-icon">💻</div>
          <h3>GitHub</h3>
          <a
            href="https://github.com/aneela-gth"
            target="_blank"
            rel="noopener noreferrer"
          >
            github.com/aneela-gth
          </a>
        </div>

        {/* LinkedIn */}
        <div className="contact-card">
          <div className="contact-icon">🔗</div>
          <h3>LinkedIn</h3>
          <a
            href="https://linkedin.com/in/aneela-bandi"
            target="_blank"
            rel="noopener noreferrer"
          >
            linkedin.com/in/aneela-bandi
          </a>
        </div>
      </div>
    </section>
  );
};

export default Contact;
