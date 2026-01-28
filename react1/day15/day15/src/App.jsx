import Navbar from "./Components/Navbar";
import "./Components/style.css";
import Home from "./Components/Home";
import Projects from "./Components/Projects";
import About from "./Components/About";
import Skills from "./Components/Skils";
import Contact from "./Components/Contact";
import Resume from "./Components/Resume";
import Certificates from "./Components/Certificates";



function App() {
  return (
    <>

      <Navbar />
      <Home></Home>
      <About></About>
      <Skills></Skills>
      <Projects></Projects>
      <Resume></Resume>
      <Certificates></Certificates>
      <Contact></Contact>
       
      
  
     
    </>
  );
}

export default App;
