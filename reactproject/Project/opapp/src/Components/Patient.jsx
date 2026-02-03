import React, { useEffect, useState } from "react";
import { db } from "../firebase";
import { collection, getDocs } from "firebase/firestore";

function PatientList() {
  const [patients, setPatients] = useState([]);

  useEffect(() => {
    const fetchPatients = async () => {
      const data = await getDocs(collection(db, "patients"));
      setPatients(data.docs.map(doc => ({ ...doc.data(), id: doc.id })));
    };

    fetchPatients();
  }, []);

  return (
    <div>
      <h2>📋 Patient Records</h2>

      {patients.map((p) => (
        <div className="appointment-card" key={p.id}>
          <p><b>Name:</b> {p.patientName}</p>
          <p><b>Disease:</b> {p.disease}</p>
          <p><b>Doctor:</b> {p.doctorName}</p>
          <p><b>Department:</b> {p.department}</p>
        </div>
      ))}
    </div>
  );
}

export default PatientList;
