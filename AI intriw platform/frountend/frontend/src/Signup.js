import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./App.css";

function Signup() {
  const [form, setForm] = useState({
    username: "",
    email: "",
    password: "",
  });

  const handleSignup = async () => {
    const res = await fetch("http://127.0.0.1:8000/api/signup/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(form),
    });

    const data = await res.json();

    alert(data.message || data.error);
  };

  return (
    <div className="auth-container">
      <h2>Signup</h2>

      <input
        placeholder="Username"
        onChange={(e) =>
          setForm({ ...form, username: e.target.value })
        }
      />

      <input
        placeholder="Email"
        onChange={(e) =>
          setForm({ ...form, email: e.target.value })
        }
      />

      <input
        type="password"
        placeholder="Password"
        onChange={(e) =>
          setForm({ ...form, password: e.target.value })
        }
      />

      <button className="auth-btn" onClick={handleSignup}>
        Signup
      </button>

      <p className="auth-link">
        Already have an account? <Link to="/">Login</Link>
      </p>
    </div>
  );
}

export default Signup;