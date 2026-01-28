import { useState } from "react";

const Roadmap = () => {
  const [skills, setSkills] = useState([
    { name: "HTML", status: "Not Started" },
    { name: "CSS", status: "Not Started" },
    { name: "JavaScript", status: "Not Started" },
    { name: "React", status: "Not Started" },
  ]);

  const changeStatus = (index) => {
    const updatedSkills = [...skills];

    if (updatedSkills[index].status === "Not Started") {
      updatedSkills[index].status = "In Progress";
    } else if (updatedSkills[index].status === "In Progress") {
      updatedSkills[index].status = "Completed";
    } else {
      updatedSkills[index].status = "Not Started";
    }

    setSkills(updatedSkills);
  };

  // ⭐ Progress Calculation
  const completedCount = skills.filter(
    (skill) => skill.status === "Completed"
  ).length;

  const progressPercent = Math.round(
    (completedCount / skills.length) * 100
  );

  return (
    <div>
      {/* Progress Bar */}
      <div className="progress-box">
        <p>Progress: {progressPercent}%</p>
        <div className="progress-bar">
          <div
            className="progress-fill"
            style={{ width: `${progressPercent}%` }}
          ></div>
        </div>
      </div>

      {/* Skills */}
      <div className="roadmap">
        {skills.map((skill, index) => (
          <div className="card" key={index}>
            <h3>{skill.name}</h3>
            <p>{skill.status}</p>
            <button onClick={() => changeStatus(index)}>
              Change Status
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Roadmap;

