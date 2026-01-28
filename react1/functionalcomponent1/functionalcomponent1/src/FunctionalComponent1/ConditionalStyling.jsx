import { useState } from "react";

export function ConditionalStyling() {
  const [highlight, setHighlight] = useState(true);

  return (
    <>
      <h1
        style={{
          color: highlight ? "green" : "red",
          
        }}
      >
        {highlight ? "Active User" : "Inactive User"}
      </h1>

      <button onClick={() => setHighlight(!highlight)}>
        {highlight ? "Good" : "Bad"}
      </button>
    </>
  );
}
