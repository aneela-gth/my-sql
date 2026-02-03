
import React from "react";


const certificates = [
  {
    title: "Introduction to HTML",
    provider: "Simplilearn SkillUp",
    name: "Bandi Aneela",
    date: "27 August 2025",
    code: "8864249",
    image: "/certificates/html-certificate.png",
    verify: "https://www.simplilearn.com/skillup"
  }
];

const Certificates = () => {
  return (
    <section id="certificates" className="certificates-section">
      <h2 className="section-title">Certificates</h2>

      <div className="certificates-grid">
        {certificates.map((cert, index) => (
          <div className="certificate-card" key={index}>
            <img
              src="/Screenshot 2026-01-27 131155.png"
              alt={cert.title}
              className="certificate-img"
            />

            <h3>{cert.title}</h3>
            <p><strong>Name:</strong> {cert.name}</p>
            <p><strong>Platform:</strong> {cert.provider}</p>
            <p><strong>Date:</strong> {cert.date}</p>
            <p><strong>Certificate Code:</strong> {cert.code}</p>

            <a
              href={cert.verify}
              target="_blank"
              rel="noopener noreferrer"
              className="verify-btn"
            >
              Verify Certificate
            </a>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Certificates;

