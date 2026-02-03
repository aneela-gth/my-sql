import React from "react";

function AppointmentList({ appointments }) {
  return (
    <div>
      <h2>📋 Booked Appointments</h2>

      {appointments.length === 0 && <p>No appointments yet</p>}

      {appointments.map((app, index) => (
        <div className="appointment-card" key={index}>
          <p><b>Patient:</b> {app.patientName}</p>
          <p><b>Age:</b> {app.age}</p>
          <p><b>Gender:</b> {app.gender}</p>
          <p><b>Phone:</b> {app.phone}</p>
          <p><b>Disease:</b> {app.disease}</p>
          <p><b>Doctor:</b> {app.doctorName}</p>
          <p><b>Department:</b> {app.department}</p>
          <p><b>Date:</b> {app.date} | <b>Time:</b> {app.time}</p>
        </div>
      ))}
    </div>
  );
}

export default AppointmentList;
