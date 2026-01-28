import resume from "../assets/resume.pdf";

function Resume() {
  return (
    <section id="resume" className="section">
      <h2>Resume</h2>
      <a href={resume} download className="btn">
        Download Resume
      </a>
    </section>
  );
}
export default Resume;
