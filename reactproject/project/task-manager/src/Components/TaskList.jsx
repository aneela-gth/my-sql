import React, { useState } from "react";

function TaskList({ tasks, deleteTask, toggleTask, updateTask }) {
  const [editId, setEditId] = useState(null);
  const [editText, setEditText] = useState("");

  return (
    <ul>
      {tasks.map(task => (
        <li key={task.id}>
          {editId === task.id ? (
            <>
              <input
                value={editText}
                onChange={(e) => setEditText(e.target.value)}
              />
              <button onClick={() => {
                updateTask(task.id, editText);
                setEditId(null);
              }}>Save</button>
            </>
          ) : (
            <>
              <span
                onClick={() => toggleTask(task.id)}
                style={{
                  textDecoration: task.completed ? "line-through" : "none",
                  cursor: "pointer"
                }}
              >
                {task.title}
              </span>

              <button onClick={() => deleteTask(task.id)}>Delete</button>
              <button onClick={() => {
                setEditId(task.id);
                setEditText(task.title);
              }}>Edit</button>
            </>
          )}
        </li>
      ))}
    </ul>
  );
}

export default TaskList;