import { useState } from "react";

export function ToggleExample() {
  const [loggedIn, setLoggedIn] = useState(false);

  return (
    <>
      <h1>{loggedIn ? "Welcome to page" : "Please login"}</h1>

      <button onClick={() => setLoggedIn(!loggedIn)}>
        {loggedIn ? "Logout" : "Login"}
      </button>
    </>
  );
}
