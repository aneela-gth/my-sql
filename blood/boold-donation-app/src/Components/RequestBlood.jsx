import { useState } from "react";
import DonorList from "./DonorList";

function RequestBlood() {
  const [blood, setBlood] = useState("");
  const [location, setLocation] = useState("");
  const [selectedDonor, setSelectedDonor] = useState(null);

  return (
    <>
      <h3>🔍 Request Blood</h3>

      <select onChange={(e) => setBlood(e.target.value)}>
        <option value="">Select Blood Group</option>
        <option>O+</option>
        <option>A+</option>
        <option>B+</option>
        <option>AB+</option>
      </select>

      <input
        placeholder="Enter City"
        onChange={(e) => setLocation(e.target.value)}
      />

      <DonorList
        blood={blood}
        location={location}
        setSelectedDonor={setSelectedDonor}
      />

      {/* Selected donor info */}
      {selectedDonor && (
        <div className="card">
          <h3>🩸 Selected Donor</h3>
          <p><b>Name:</b> {selectedDonor.name}</p>
          <p><b>Blood:</b> {selectedDonor.blood}</p>
          <p><b>Phone:</b> {selectedDonor.phone}</p>
          <p><b>Hospital:</b> {selectedDonor.hospital}</p>

          <button onClick={() => alert("Blood request sent successfully ✅")}>
            Send Blood Request
          </button>
        </div>
      )}
    </>
  );
}

export default RequestBlood;

