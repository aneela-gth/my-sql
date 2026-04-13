
import React, { useState } from "react";

function TaskForm({ addTask }) {
  const [title, setTitle] = useState("");
  const [category, setCategory] = useState("Python");

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!title) return;

    addTask(title, category);
    setTitle("");
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Enter task..."
        value={title}
        onChange={(e) => setTitle(e.target.value)}
      />

      <select onChange={(e) => setCategory(e.target.value)}>
        <option>Python</option>
        <option>JavaScript</option>
        <option>CSS</option>
        <option>React</option>
      </select>

      <button>Add</button>
    </form>
  );
}

export default TaskForm;