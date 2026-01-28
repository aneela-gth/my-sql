import React from "react";

function Projects() {
  const projects = [
    {
      title: "IoT Enabled Smart Traffic Management System",
      type: "Academic Project",
      description:
        "An IoT-based system designed to manage traffic efficiently using sensors and real-time data to reduce congestion and waiting time at traffic signals.",
      tech: "IoT, Python, Sensors, Cloud",
      demo: "https://your-deployment-link.com",
      code: "https://github.com/yourusername/smart-traffic-iot"
    },
    {
      title: "Notes Application",
      type: "Web App",
      description:
        "A full-stack notes application where users can create, edit, delete, and upload notes securely.",
      tech: "React, Django, REST API",
      demo: "https://notes-app-demo.netlify.app",
      code: "https://github.com/yourusername/notes-app"
    },
    {
      title: "Portfolio Website",
      type: "Web App",
      description:
        "Personal portfolio website showcasing skills, projects, certificates, and contact details.",
      tech: "React JS, CSS, React Router",
      demo: "https://your-portfolio.netlify.app",
      code: "https://github.com/yourusername/portfolio"
    },
    {
      title: "Todo App",
      type: "Web App",
      description:
        "A simple and efficient todo application with add, update, and delete functionalities.",
      tech: "React JS, Hooks",
      demo: "https://todo-app-demo.netlify.app",
      code: "https://github.com/yourusername/todo-app"
    }
  ];

  return (
    <section className="projects-section">
      <h2 className="projects-title">Projects</h2>

      <div className="projects-grid">
        {projects.map((project, index) => (
          <div className="project-card" key={index}>
            <span className="project-type">{project.type}</span>
            <h3>{project.title}</h3>
            <p className="project-desc">{project.description}</p>

            <p className="project-tech">
              <strong>Technologies:</strong> {project.tech}
            </p>

            <div className="project-links">
              <a href={project.demo} target="_blank" rel="noreferrer">
                Live Demo
              </a>
              <a href={project.code} target="_blank" rel="noreferrer">
                GitHub Code
              </a>
            </div>
          </div>
        ))}
      </div>
    </section>
  );
}

export default Projects;
