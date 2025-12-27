function Contact() {
  return (
    <div id="contact">
       <h1 style={{backgroundColor:"greenyellow", textAlign:"center"}}>CONTACT</h1>
      {/* TOP ADDRESS SECTION */}
      <div
        style={{background: "#f5f0f0",padding: "40px",textAlign: "center"}}
      >
        <h2 style={{ color: "deeppink" }}>
          UNIT 0123 , ABC BUILDING, BUSINESS PARK
        </h2>
        <p>
          If you're having problems editing this website template,
          don't hesitate to ask for help.
        </p>
      </div>

      {/* MAIN CONTACT SECTION */}
      <div style={{display: "flex",padding: "60px",gap: "40px"}}
      >
        {/* LEFT FORM */}
        <div style={{ width: "65%" }}>
          <h2 style={{ color: "deeppink" }}>INQUIRY FORM</h2>

          <input type="text" placeholder="Name" style={inputStyle}/>

          <input type="email" placeholder="Email" style={inputStyle}/>

          <input type="text" placeholder="Subject" style={inputStyle}/>

          <textarea placeholder="Share your thoughts" rows="6" style={inputStyle}></textarea>

          <button style={btnStyle}>SEND MESSAGE</button>
        </div>

        

      </div>
    </div>
  );
}

/* SIMPLE STYLES */
const inputStyle = {
  width: "100%",
  padding: "12px",
  marginBottom: "15px",
  border: "1px solid #ccc"
};

const btnStyle = {
  padding: "12px 25px",
  border: "1px solid deeppink",
  background: "transparent",
  color: "deeppink",
  cursor: "pointer"
};

export default Contact;
