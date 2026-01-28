import React from "react";
import "./style.css";
import "./Hero.css";
import profileImg from "../assets/WhatsApp Image 2025-10-27 at 12.30.47_2f04ba51.jpg";

const Home = () => {
  return (
    <section id="home" className="home">
      <div className="home-left">
        <h4>Hello, It’s Me</h4>

        <h1>
          Aneela <br />
          <span className="moving-text">Python Full Stack Developer</span>
        </h1>

        <p>
          I’m a Python Full Stack Developer with hands-on experience in building
          responsive web applications. I specialize in creating scalable
          frontend interfaces and robust backend systems using modern
          technologies.
        </p>

        <p>
          <strong>Frontend:</strong> HTML, CSS, JavaScript, React <br />
          <strong>Backend:</strong> Python, Django, REST APIs <br />
          <strong>Database:</strong> MySQL
        </p>

        <div className="social-icons">
          <span>in</span>
          <span>gh</span>
          <span>ig</span>
          <span>yt</span>
        </div>

        <button className="btn">More About Me</button>
      </div>

      <div className="home-right">
        <div className="image-ring">
          <img src={profileImg} alt="profile" />
        </div>
      </div>
    </section>
  );
};

export default Home;
