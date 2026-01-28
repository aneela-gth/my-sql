import React from "react";
import "./style.css";

const Skills = () => {
  return (
    <section id="skills" className="skills">
      <h2 className="section-title">Skills</h2>

      <div className="skills-container">
        {/* FRONTEND */}
        <div className="skills-card frontend">
          <h3>Frontend</h3>
          <ul>
            <li>HTML5</li>
            <li>CSS3</li>
            <li>JavaScript (ES6+)</li>
            <li>React.js</li>
            <li>Responsive Design</li>
          </ul>
        </div>

        {/* BACKEND */}
        <div className="skills-card backend">
          <h3>Backend</h3>
          <ul>
            <li>Python</li>
            <li>Django</li>
            <li>Django REST Framework</li>
            <li>REST APIs</li>
            <li>Authentication & Authorization</li>
          </ul>
        </div>

        {/* DATABASE */}
        <div className="skills-card database">
          <h3>Databases</h3>
          <ul>
            <li>MySQL</li>
            <li>PostgreSQL</li>
            <li>SQLite</li>
          </ul>
        </div>
      </div>
    </section>
  );
};

export default Skills;
