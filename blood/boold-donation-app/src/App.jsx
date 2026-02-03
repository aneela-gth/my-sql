import { useState } from "react";
import Register from "./Components/Register";
import Dashboard from "./Components/Dashboard";

function App() {
  const [page, setPage] = useState("register");

  return (
    <>
      {page === "register" && <Register setPage={setPage} />}
      {page === "dashboard" && <Dashboard />}
      
    </>
  );
}

export default App;


