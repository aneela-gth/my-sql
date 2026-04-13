import axios from "axios";
import { useState } from "react";

function Signup() {
  const [data, setData] = useState({
    username: "",
    password: ""
  });

  const handleSubmit = async () => {
    try {
      await axios.post("http://127.0.0.1:8000/signup/", data);
      alert("Signup successful");
    } catch (err) {
      alert("Error");
    }
  };

  return (
    <div>
      <h2>Signup</h2>

      <input
        placeholder="Username"
        onChange={(e) =>
          setData({ ...data, username: e.target.value })
        }
      />

      <input
        type="password"
        placeholder="Password"
        onChange={(e) =>
          setData({ ...data, password: e.target.value })
        }
      />

      <button onClick={handleSubmit}>Signup</button>
    </div>
  );
}

export default Signup;