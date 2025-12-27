import "./style.css";

function Card() {
  return (
    <div>
      <h1 style={{backgroundColor:"black",color:"white",textAlign:"center"}}>CARDES</h1>
    <div className="main">
    
        <div className="burger">
            <img src="/burger.jpg" alt="Burger" />
            <h2> name:Burger</h2>
            <h3>prize:80</h3>
            <button className="btn1">BUY NOW</button>
        </div>
        <div className="burger">
                <img src="/piza.jpg"></img>
                <h2> name:PIZA</h2>
                <h3>prize:200</h3>
                <button className="btn1">BUY NOW</button>

        </div>
        <div className="burger">
            <img src="/Pani_Puri1.JPG" width={"200px"}></img>
            <h2> name:PANIPURI</h2>
            <h3>prize:30</h3>
            <button className="btn1">BUY NOW</button>
        </div>
        <div className="burger">
            <img src="/magi.jpg" width={"200px"}></img>
            <h2> name:MAGI</h2>
            <h3>prize:60</h3>
            <button className="btn1">BUY NOW</button>

        </div>
        </div>
        
    </div>
  );
}

export default Card;


