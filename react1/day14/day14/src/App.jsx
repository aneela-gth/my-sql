import React from "react";

import "./App.css";
import Navbar from "./Components/Navbar";
import Home from "./Components/Home";
import Contact from "./Components/Contact";
import Projects from "./Components/Projects";
import Skills from "./Components/Skills";
import About from "./Components/About";

function App() {
  return (
    <div>
      <Navbar></Navbar>
      <Home></Home>
      <Contact></Contact>
      <Projects></Projects>
      <Skills></Skills>
      <About></About>

    </div>
  );
}

export default App;
