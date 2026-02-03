import profileImg from "../assets/WhatsApp Image 2025-10-27 at 12.30.47_2f04ba51.jpg";

const Home = () => {
  return (
    <section className="hero" id="home">
      <div className="hero-left">
        <p className="hello">Hello, It’s Me</p>
        <h1>Aneela</h1>
        <h2 className="role">Python Full Stack Developer</h2>

        <p className="desc">
          I’m a Python Full Stack Developer with hands-on experience in building
          responsive web applications. I specialize in creating scalable
          frontend interfaces and robust backend systems using modern
          technologies.
        </p>

        <p><strong>Frontend:</strong> HTML, CSS, JavaScript, React</p>
        <p><strong>Backend:</strong> Python, Django, REST APIs</p>
        <p><strong>Database:</strong> MySQL</p>

        <div className="socials">
          <span>in</span>
          <span>gh</span>
          <span>ig</span>
          <span>yt</span>
        </div>

        <button className="btn">More About Me</button>
      </div>

      <div className="hero-right">
        <img src={profileImg} alt="Aneela" />

        {/* image from public folder */}
        {/* <img src="/src/assets/WhatsApp Image 2025-10-27 at 12.30.47_2f04ba51.jpg" alt="Aneela" /> */}
      </div>
    </section>
  );
};

export default Home;
