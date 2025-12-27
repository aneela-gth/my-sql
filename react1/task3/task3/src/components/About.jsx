function About() {
  return (
    <div id="about">
      {/* PAGE TITLE */}
      <h1 className="about-title" style={{backgroundColor:"greenyellow"}}>ABOUT</h1>

      {/* IMAGE */}
      <div className="about-image">
        <img src="/yogurt.jpg" alt="Yogurt" />
      </div>

      {/* CONTENT SECTION */}
      <div className="about-container">
        {/* LEFT RECTANGLE */}
        <div className="left-rect">
          <h2>
            BE PART OF OUR <br /> COMMUNITY
          </h2>

          <p>If you’re experiencing</p>
          <p>issues or having concerns</p>
          <p>about this website</p>
          <p>template, join the</p>
          <p>
            discussion <a href="#">on our forum</a>
          </p>
          <p>and meet other people in</p>
          <p>the community who share</p>
          <p>the same interests.</p>
        </div>

        {/* RIGHT CONTENT */}
        <div className="right-content">
          <h2>WE HAVE FREE TEMPLATES FOR EVERYONE</h2>
          <p>
            Our website templates are created with inspiration, checked for
            quality and originality and meticulously sliced and coded.
          </p>
        
        <div className="right-content">
          <h2>WE HAVE FREE TEMPLATES FOR EVERYONE</h2>
          <p>
            Our website templates are created with inspiration, checked for
            quality and originality and meticulously sliced and coded.
          </p>
        </div>
        <div className="right-content">
          <h2>WE HAVE FREE TEMPLATES FOR EVERYONE</h2>
          <p>
            Our website templates are created with inspiration, checked for
            quality and originality and meticulously sliced and coded.
          </p>
        </div>
        <div className="right-content">
          <h2>WE HAVE FREE TEMPLATES FOR EVERYONE</h2>
          <p>
            Our website templates are created with inspiration, checked for
            quality and originality and meticulously sliced and coded.
          </p>
        </div>
        </div>
      </div>
    </div>
  );
}

export default About;
