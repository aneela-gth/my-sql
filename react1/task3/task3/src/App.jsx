import Navbar from "./components/Navbar";
import Hero from "./components/hero";
import "./App.css";
import NewProduct from "./components/NewProducts";
import About from "./components/About";
import Blog from "./components/Blog";
import Contact from "./components/Contact";


function App() {
  return (
    <>
      <Navbar />
      <Hero/>
      <NewProduct/>
      <About/>
      <Blog/>
      <Contact/>
     
      
    </>
  );
}

export default App;

