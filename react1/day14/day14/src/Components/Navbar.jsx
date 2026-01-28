import React from "react";

function Navbar() {
  return (
    <nav className="navbar">
      <h2 className="logo">Aneela</h2>

      <ul className="nav-links">
        <li><a href="#Home">home</a></li>
        <li><a href="#About">about</a></li>
        <li><a href="#Skills">Skills</a></li>
        <li><a href="#Projects">Projects</a></li>
        <li><a href="#Contact">Contact</a></li>
        <li><a href="#Contact">Resumes</a></li>
        <li><a href="#Contact">Ccrtficates</a></li>
      </ul>
    </nav>
  );
}

export default Navbar;
