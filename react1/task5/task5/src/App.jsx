import React, { useState } from "react";

function App() {
  const [bulb, setBulb] = useState("off");

  const onStyle = {
    backgroundColor: "green",
    color: "white",
    padding: "12px 30px",
    fontSize: "18px",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer"
  };

  const offStyle = {
    backgroundColor: "red",
    color: "white",
    padding: "12px 30px",
    fontSize: "18px",
    border: "none",
    borderRadius: "8px",
    cursor: "pointer"
  };

  return (
    <div
      style={{
        textAlign: "center",
        minHeight: "100vh",
        backgroundColor: "black",
        color: "white",
        paddingTop: "50px"
      }}
    >
      <h1>Bulb ON / OFF</h1>

      <img
        src={bulb === "on" ? "/image2.png" : "/img1.png"}
        alt="Bulb"
        width="350"
      />

      <br /><br />

      {/* Styled Buttons */}
      <button style={onStyle} onClick={() => setBulb("on")}>
        ON
      </button>
      &nbsp;&nbsp;&nbsp;
      <button style={offStyle} onClick={() => setBulb("off")}>
        OFF
      </button>
    </div>
  );
}

export default App;
