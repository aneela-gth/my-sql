import React from "react";

function Skills() {
  return (
    <section className="skills-section">
      <h2 className="skills-title">My Skills</h2>

      <div className="skills-category">

        {/* FRONTEND */}
        <div className="skills-block">
          <h3 className="skills-heading">Frontend</h3>
          <div className="skills-grid">
            <div className="skill-card"><span>🌐</span><p>HTML</p></div>
            <div className="skill-card"><span>🎨</span><p>CSS</p></div>
            <div className="skill-card"><span>⚡</span><p>JavaScript</p></div>
            <div className="skill-card"><span>⚛️</span><p>React JS</p></div>
          </div>
        </div>

        {/* BACKEND */}
        <div className="skills-block">
          <h3 className="skills-heading">Backend</h3>
          <div className="skills-grid">
            <div className="skill-card"><span>🐍</span><p>Python</p></div>
            <div className="skill-card"><span>🟢</span><p>Django</p></div>
          </div>
        </div>

        {/* DATABASES */}
        <div className="skills-block">
          <h3 className="skills-heading">Databases</h3>
          <div className="skills-grid">
            <div className="skill-card"><span>🗄️</span><p>SQL</p></div>
          </div>
        </div>

      </div>
    </section>
  );
}

export default Skills;

