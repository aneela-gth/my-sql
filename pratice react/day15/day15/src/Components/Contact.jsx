import React from "react";
import "./Style.css";

export default function Contact() {
  return (
    <section className="contact-section" id="contact">
      <h2>Contact Me</h2>
      <p className="contact-subtitle">
        Feel free to reach out for collaborations or opportunities
      </p>

      <div className="contact-box">
        {/* Email */}
        <div className="contact-item">
          <span>Ⓜ️ Email</span>
          <p>aneelabandi9951@gmail.com</p>
        </div>

        {/* Phone */}
        <div className="contact-item">
          <span>📞 Phone</span>
          <p>+91 7674087691</p>
        </div>

        {/* Location */}
        <div className="contact-item">
          <span>📍 Location</span>
          <p>Hyderabad, India</p>
        </div>

        {/* GitHub */}
        <div className="contact-item">
          <span>💼 GitHub</span>
          <p>
            <a
              href="https://github.com/aneela-gth/react/tree/main/day15/day15"
              target="_blank"
              rel="noreferrer"
            >
              github.com/aneela-gth
            </a>
          </p>
        </div>

        {/* LinkedIn */}
        <div className="contact-item">
          <span>🔗 LinkedIn</span>
          <p>
            <a
              href="https://linkedin.com/in/aneela-bandi"
              target="_blank"
              rel="noreferrer"
            >
              linkedin.com/in/aneela-bandi
            </a>
          </p>
        </div>
      </div>
    </section>
  );
}
