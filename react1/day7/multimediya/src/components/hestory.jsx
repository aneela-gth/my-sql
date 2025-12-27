// src/components/Hestory.jsx
import "./style1.css";

function Hestory() {
  return (
    <div id="history">
      <div className="main">

        {/* Card 1 */}
        <div className="burger">
          <img src="/Kakatiya-Rulers-exploretelangana.jpg" alt="Kakatiya dynasty" width="200" />
          <h2>Name: Kakatiya dynasty</h2>
          <video width="200" controls>
            <source src="/ranirudram.mp4" type="video/mp4" />
          </video>
          <audio controls>
            <source src="/Vachinde.mp3" type="audio/mp3" />
          </audio>
        </div>

        {/* Card 2 */}
        <div className="burger">
          <img src="/10.Golconda-Fort-Images.jpg" alt="Golconda Fort" width="200" />
          <h2>Name: Golconda Fort</h2>
          <video width="200" controls>
            <source src="/chatharapathi.mp4" type="video/mp4" />
          </video>
          <audio controls>
            <source src="/Vachinde.mp3" type="audio/mp3" />
          </audio>
        </div>

        {/* Card 3 */}
        <div className="burger">
          <img src="/entrance_bridge_to_hyderabad_india1.avif" alt="Nizam rule" width="200" />
          <h2>Name: Nizam rule</h2>
          <video width="200" controls>
            <source src="/chatharapathi.mp4" type="video/mp4" />
          </video>
          <audio controls>
            <source src="/Vachinde.mp3" type="audio/mp3" />
          </audio>
        </div>

        {/* Card 4 */}
        <div className="burger">
          <img src="/OIP.webp" alt="Charminar" width="200" />
          <h2>Name: Charminar</h2>
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

export default Hestory;


