const Skills = () => {
  return (
    <section className="skills-section" id="skills">
      <h2 className="skills-title">Skills</h2>

      <div className="skills-container">
        {/* Frontend */}
        <div className="skill-card">
          <h3 className="frontend">Frontend</h3>
          <ul>
            <li>HTML5</li>
            <li>CSS3</li>
            <li>JavaScript (ES6+)</li>
            <li>React.js</li>
            <li>Responsive Design</li>
          </ul>
        </div>

        {/* Backend */}
        <div className="skill-card">
          <h3 className="backend">Backend</h3>
          <ul>
            <li>Python</li>
            <li>Django</li>
            <li>Django REST Framework</li>
            <li>REST APIs</li>
            <li>Authentication & Authorization</li>
          </ul>
        </div>

        {/* Databases */}
        <div className="skill-card">
          <h3 className="database">Databases</h3>
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
