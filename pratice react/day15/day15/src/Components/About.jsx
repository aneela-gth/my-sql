import React from "react";
import "./style.css";

const About = () => {
  return (
    <section id="about" className="about">
      <h2 className="section-title">About Me</h2>

      <div className="about-container">
        <div className="about-text">
          <h3>Python Full Stack Developer</h3>

          <p>
            I am a passionate <strong>Python Full Stack Developer</strong> with
            hands-on experience in designing, developing, and deploying web
            applications. I enjoy building complete solutions from intuitive
            user interfaces to powerful backend systems.
          </p>

          <p>
            My expertise includes creating responsive frontend applications
            using <strong>React</strong>, and developing secure, scalable backend
            services using <strong>Python</strong> and <strong>Django</strong>.
            I also have strong experience working with databases and RESTful APIs.
          </p>

          <p>
            I am always eager to learn new technologies, improve my skills,
            and work on challenging projects that solve real-world problems.
          </p>

          <div className="about-skills">
            <span>HTML</span>
            <span>CSS</span>
            <span>JavaScript</span>
            <span>React</span>
            <span>Python</span>
            <span>Django</span>
            <span>MySQL</span>
          </div>
        </div>
      </div>
    </section>
  );
};

export default About;
