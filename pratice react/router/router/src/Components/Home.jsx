import "./Home.css"

function Home() {
  return (
    <div className="home">
      <h1 className="title">Home Page</h1>

      <div className="intro">
        <h2>Welcome to our website</h2>
        <p>Lorem ipsum dolor sit amet consectetur</p>
      </div>

      <div className="buttons">
        <button className="btn primary">Get Ready</button>
        <button className="btn secondary">Welcome to Page</button>
      </div>

      <img
        className="home-img"
        src="https://cdn-icons-png.flaticon.com/512/25/25694.png"
        alt="home"
      />

      <h3>This is the home page</h3>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
    </div>
  )
}

export default Home
