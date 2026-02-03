
import React, { useState } from "react";
import BookAppointment from "./Components/BookAppointment";
import AppointmentList from "./Components/AppointmentList";
import DoctorList from "./Components/DoctoeList";
import "./App.css";

function App() {
  const [appointments, setAppointments] = useState([]);
  const [selectedDoctor, setSelectedDoctor] = useState(null);

  const bookAppointment = (appointment) => {
    setAppointments([...appointments, appointment]);
  };

  return (
    <div>
      <h1>🏥 Online Doctor Consultation & OP Booking</h1>

      <DoctorList setSelectedDoctor={setSelectedDoctor} />

      {selectedDoctor && (
        <BookAppointment
          doctor={selectedDoctor}
          bookAppointment={bookAppointment}
        />
      )}

      <AppointmentList appointments={appointments} />
    </div>
  );
}

export default App;
