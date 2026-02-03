import React from "react";

const doctors = [
  { id: 1, name: "Dr. Anil", department: "Cardiology" },
  { id: 2, name: "Dr. Priya", department: "Dermatology" },
  { id: 3, name: "Dr. Ravi", department: "Orthopedics" }
];

function DoctorList({ setSelectedDoctor }) {
  return (
    <div>
      <h2>👨‍⚕️ Available Doctors</h2>

      {doctors.map((doc) => (
        <div key={doc.id}>
          <p><b>{doc.name}</b> - {doc.department}</p>
          <button onClick={() => setSelectedDoctor(doc)}>
            Book OP
          </button>
        </div>
      ))}
    </div>
  );
}

export default DoctorList;
