function Multimedia() {
  return (
    <div>
      <h1>Multimedia React App</h1>

      <img src="image1.jpg" width="150" /><br></br>

      <video width="300" controls>
        <source src="Surya Web Series __ Episode - 1 __ Shanmukh Jaswanth __ Mounika Reddy __ Infinitum Media.mp4" type="video/mp4" />
      </video>

      <audio controls>
        <source src="[iSongs.info] 01 - Vachinde.mp3" type="audio/mp3" />
      </audio>
    </div>
  );
}

export default Multimedia;
