// src/components/Festiveles.jsx
import "./style.css"; // rename CSS file for clarity

function Festiveles() {
  return (
    <div id="festivals">
      <div className="main">

        {/* Card 1 */}
        <div className="burger">
          <img src="/bathukamma2.jpg" alt="Bathukamma" width="200" />
          <h2>Name: Bathukamma</h2>
          <video width="200" controls>
            <source src="/ranirudram.mp4" type="video/mp4" />
          </video>
          <audio controls>
            <source src="/Vachinde.mp3" type="audio/mp3" />
          </audio>
        </div>

        {/* Card 2 */}
        <div className="burger">
          <img src="/fetch.jpeg" alt="Bonalu" width="200" />
          <h2>Name: Bonalu</h2>
          <video width="200" controls>
            <source src="/chatharapathi.mp4" type="video/mp4" />
          </video>
          <audio controls>
            <source src="/Vachinde.mp3" type="audio/mp3" />
          </audio>
        </div>

        {/* Card 3 */}
        <div className="burger">
          <img src="/christmas.jpg" alt="Christmas" width="200" />
          <h2>Name: Christmas</h2>
          <video width="200" controls>
            <source src="/chatharapathi.mp4" type="video/mp4" />
          </video>
          <audio controls>
            <source src="/Vachinde.mp3" type="audio/mp3" />
          </audio>
        </div>

        {/* Card 4 */}
        <div className="burger">
          <img src="/ramajan.webp" alt="Ramzan" width="200" />
          <h2>Name: Ramzan (Eid-ul-Fitr)</h2>
          <video width="200" controls>
            <source src="/chatharapathi.mp4" type="video/mp4" />
          </video>
          <audio controls>
            <source src="/Vachinde.mp3" type="audio/mp3" />
          </audio>
        </div>

      </div>
    </div>
  );
}

export default Festiveles;


