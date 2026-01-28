import cert1 from "../assets/cert1.jpg";
import cert2 from "../assets/cert2.jpg";

function Certificates() {
  return (
    <section className="section">
      <h2>Certificates</h2>
      <img src={cert1} alt="Certificate 1" className="cert" />
      <img src={cert2} alt="Certificate 2" className="cert" />
    </section>
  );
}
export default Certificates;
