import "./Home.css"

function Contact() {
  return (
    <div className="home">
      <h1 className="title">Contact Page</h1>

      <div className="intro">
        <h2>Get in Touch</h2>
        <p>We would love to hear from you</p>
      </div>

      <ol className="contact-info">
        <li>#123, 5th, 4th cross, KPHB, Hyderabad</li>
        <li>📞 8765432345</li>
        <li>📧 a@gmail.com</li>
      </ol>

      <form className="contact-form">
        <label>Enter your name</label>
        <input type="text" placeholder="Your name" />

        <label>Enter your problem</label>
        <textarea rows="5" placeholder="Type your message"></textarea>

        <button className="btn primary">Send Message</button>
      </form>
    </div>
  )
}

export default Contact

