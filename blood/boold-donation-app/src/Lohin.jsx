import axios from "axios";
import { useState } from "react";

function Login() {
  const [data, setData] = useState({
    username: "",
    password: ""
  });

  const handleLogin = async () => {
    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/login/",
        data
      );

      if (res.data.user_id) {
        localStorage.setItem("user_id", res.data.user_id);
        alert("Login successful");
      } else {
        alert("Invalid login");
      }
    } catch (err) {
      alert("Error");
    }
  };

  return (
    <div>
      <h2>Login</h2>

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

      <button onClick={handleLogin}>Login</button>
    </div>
  );
}

export default Login;