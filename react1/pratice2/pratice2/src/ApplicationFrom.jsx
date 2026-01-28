import { useState } from "react";

function ApplicationForm() {
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [msg, setMsg] = useState("");

  const submitForm = async (e) => {
    e.preventDefault();

    const res = await fetch("http://127.0.0.1:8000/apply/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ name, email }),
    });

    if (res.ok) {
      setMsg("✅ Application submitted successfully");
      setName("");
      setEmail("");
    } else {
      setMsg("❌ Error");
    }
  };

  return (
    <div className="card">
      <h2>Application Form</h2>

      <form onSubmit={submitForm}>
        <input
          className="input"
          placeholder="Name"
          value={name}
          onChange={(e) => setName(e.target.value)}
          required
        />

        <input
          className="input"
          placeholder="Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
        />

        <button className="btn">Submit</button>
      </form>

      <p>{msg}</p>
    </div>
  );
}

export default ApplicationForm;
