import React, { useEffect } from "react";

export function ComponentLifeCycle() {
  useEffect(() => {
    console.log("mounting phase -1");
  }, []);

  return (
    <>
      <h1>Mounting phase</h1>
    </>
  );
}
