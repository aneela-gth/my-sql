// src/components/Multimediya.jsx
import "./style.css";

function Multimediya() {
  return (
    <div id="home">
      <div className="main">

        {/* Card 1 */}
        <div className="burger">
          <img src="/rani.jpg" alt="Rani Rudrama Devi" width="200" />
          <h2>Name: Rani Rudrama Devi</h2>
          <video width="200" controls>
            <source src="/ranirudram.mp4" type="video/mp4" />
          </video>
          <audio controls>
            <source src="/Vachinde.mp3" type="audio/mp3" />
          </audio>
        </div>

        {/* Card 2 */}
        <div className="burger">
          <img src="/savitribai-phule.webp" alt="Savitribai Phule" width="200" />
          <h2>Name: Savitribai Phule</h2>
          <video width="200" controls>
            <source src="/chatharapathi.mp4" type="video/mp4" />
          </video>
          <audio controls>
            <source src="/Vachinde.mp3" type="audio/mp3" />
          </audio>
        </div>

        {/* Card 3 */}
        <div className="burger">
          <img src="/shivaji.jpg" alt="Chhatrapati Shivaji Maharaj" width="200" />
          <h2>Name: Chhatrapati Shivaji Maharaj</h2>
          <video width="200" controls>
            <source src="/chatharapathi.mp4" type="video/mp4" />
          </video>
          <audio controls>
            <source src="/Vachinde.mp3" type="audio/mp3" />
          </audio>
        </div>

        {/* Card 4 */}
        <div className="burger">
          <img src="/dr.jpg" alt="Dr. B. R. Ambedkar" width="200" />
          <h2>Name: Dr. B. R. Ambedkar</h2>
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

export default Multimediya;


