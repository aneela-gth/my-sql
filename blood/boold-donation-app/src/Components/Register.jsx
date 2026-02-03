import { useState } from "react";

function Register({ setPage }) {
  const [form, setForm] = useState({
    name: "",
    phone: "",
    blood: "",
    location: "",
    hospital: "",
    role: ""
  });

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    localStorage.setItem("currentUser", JSON.stringify(form));

    if (form.role === "donor") {
      const donors = JSON.parse(localStorage.getItem("donors")) || [];
      donors.push(form);
      localStorage.setItem("donors", JSON.stringify(donors));
    }

    setPage("dashboard");
  };

  return (
    <div className="container">
      <h2>Blood Donation Registration</h2>

      <form onSubmit={handleSubmit}>
        <input name="name" placeholder="Name" onChange={handleChange} required />
        <input name="phone" placeholder="Phone" onChange={handleChange} required />

        <select name="blood" onChange={handleChange} required>
          <option value="">Blood Group</option>
          <option>O+</option>
          <option>A+</option>
          <option>B+</option>
          <option>AB+</option>
        </select>

        <input name="location" placeholder="City" onChange={handleChange} required />
        <input name="hospital" placeholder="Hospital" onChange={handleChange} required />

        <select name="role" onChange={handleChange} required>
          <option value="">Register As</option>
          <option value="donor">Donor</option>
          <option value="user">Patient</option>
        </select>

        <button type="submit">Register</button>
      </form>
    </div>
  );
}

export default Register;
