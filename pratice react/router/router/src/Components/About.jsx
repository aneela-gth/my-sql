import "./Home.css"

function About() {
  return (
    <div className="home">
      <h1 className="title">About Page</h1>

      <div className="intro">
        <h2>About Us</h2>
        <p>
          Lorem ipsum dolor sit amet consectetur adipisicing elit.
          Exercitationem ut architecto consequuntur labore.
        </p>
      </div>

      <h3>Popular Actors</h3>

      <ul className="about-list">
        <li>NTR</li>
        <li>Mahesh Babu</li>
        <li>Surya</li>
        <li>Ravi Teja</li>
      </ul>
    </div>
  )
}

export default About
