import React, { useState } from "react";

function BookAppointment({ doctor, bookAppointment }) {
  const [patientName, setPatientName] = useState("");
  const [disease, setDisease] = useState("");
  const [age, setAge] = useState("");
  const [gender, setGender] = useState("");
  const [phone, setPhone] = useState("");
  const [date, setDate] = useState("");
  const [time, setTime] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    bookAppointment({
      patientName,
      disease,
      age,
      gender,
      phone,
      doctorName: doctor.name,
      department: doctor.department,
      date,
      time
    });

    // clear form
    setPatientName("");
    setDisease("");
    setAge("");
    setGender("");
    setPhone("");
    setDate("");
    setTime("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>📅 Book OP for {doctor.name}</h2>

      <input
        placeholder="Patient Name"
        value={patientName}
        onChange={(e) => setPatientName(e.target.value)}
        required
      />

      <input
        placeholder="Disease"
        value={disease}
        onChange={(e) => setDisease(e.target.value)}
        required
      />

      <input
        type="number"
        placeholder="Age"
        value={age}
        onChange={(e) => setAge(e.target.value)}
        required
      />

      <select value={gender} onChange={(e) => setGender(e.target.value)} required>
        <option value="">Select Gender</option>
        <option value="Male">Male</option>
        <option value="Female">Female</option>
      </select>

      <input
        placeholder="Phone Number"
        value={phone}
        onChange={(e) => setPhone(e.target.value)}
        required
      />

      <input type="date" value={date} onChange={(e) => setDate(e.target.value)} required />
      <input type="time" value={time} onChange={(e) => setTime(e.target.value)} required />

      <button type="submit">Confirm Appointment</button>
    </form>
  );
}

export default BookAppointment;
