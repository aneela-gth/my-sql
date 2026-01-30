import { useState } from "react";

function App() {
  const [success, setSuccess] = useState(false);
  const [serial, setSerial] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();

    // generate serial number 1–4
    const serialNumber = Math.floor(Math.random() * 4) + 1;
    setSerial(serialNumber);
    setSuccess(true);

    e.target.reset();
  };

  return (
    <div className="container">
      <h1>🏥 Online Hospital OP</h1>

      <form className="form-box" onSubmit={handleSubmit}>
        <input type="text" placeholder="Patient Name" required />
        <input type="tel" placeholder="Mobile Number" required />

        <select required>
          <option value="">Gender</option>
          <option>Male</option>
          <option>Female</option>
        </select>

        <input type="number" placeholder="Age" required />
        <input type="text" placeholder="Staying Place" required />
        <input type="text" placeholder="Mandal" required />
        <input type="text" placeholder="District" required />

        <select required>
          <option value="">Select Doctor</option>
          <option>Dr. Kumar – Cardiology</option>
          <option>Dr. Anitha – Neurology</option>
          <option>Dr. Ramesh – Orthopedic</option>
          <option>Dr. Suresh – General</option>
        </select>

        <select required>
          <option value="">Payment Mode</option>
          <option>Online Payment</option>
          <option>Offline Payment</option>
        </select>

        <button type="submit">Submit OP</button>
      </form>

      {success && (
        <div className="success-box">
          <h3>✅ OP Registration Successful</h3>
          <p>✔ Successfully completed your registration</p>
          <p>📱 Message sent to your phone</p>
          <p>
            🔢 Your OP Serial Number is <b>{serial}</b>
          </p>
        </div>
      )}
    </div>
  );
}

export default App;
