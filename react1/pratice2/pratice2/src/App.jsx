import { useState } from "react";
import Home from "./Home";
import ApplicationForm from "./ApplicationForm";
import "./App.css";

function App() {
  const [showForm, setShowForm] = useState(false);

  return (
    <div className="container">
      {showForm ? (
        <ApplicationForm />
      ) : (
        <Home onOk={() => setShowForm(true)} />
      )}
    </div>
  );
}

export default App;
