import "./IdCard.css";

function IdCard() {
  return (
    <div className="card">
      <h2 className="college">
        UNIVERSITY ARTS & SCIENCE COLLEGE
      </h2>
      <h4 className="sub">(Autonomous) – Kakatiya University</h4>
      <p className="place">Subedari, Warangal – 506001</p>

      <h3 className="title">IDENTITY CARD</h3>

      <img src="/WhatsApp Image .jpg" alt="student" className="photo" />

      <div className="details">
        <p><b>Student Name:</b> B. Aneela</p>
        <p><b>Father Name:</b> Thirapaiah</p>
        <p><b>Course:</b> MCA</p>
        <p><b>Hallticket No:</b> 2400110008</p>
        <p><b>Aadhar No:</b> 8002 9256 3215</p>
        <p><b>Validity:</b> 2023 - 2025</p>
      </div>

      <p className="sign">Principal</p>
    </div>
  );
}

export default IdCard;
