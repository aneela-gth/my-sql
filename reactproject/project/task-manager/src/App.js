import React, { useEffect, useState } from "react";
import axios from "axios";
import TaskForm from "./Components/TaskForm";   // ✅ small letters
import TaskList from "./Components/TaskList";
import SearchFilter from "./Components/SearchFilter";
import "./App.css";

function App() {
  const [tasks, setTasks] = useState([]);
  const [search, setSearch] = useState("");
  const [filter, setFilter] = useState("all");
  const [categoryFilter, setCategoryFilter] = useState("All"); // ✅ moved inside
 
  // Fetch API data
  useEffect(() => {
    axios
      .get("https://jsonplaceholder.typicode.com/todos?_limit=5")
      .then((res) => {
        // add default category
        const updated = res.data.map((t) => ({
          ...t,
          category: "Python",
        }));
        setTasks(updated);
      })
      .catch((err) => console.log(err));
  }, []);

  // ✅ Add Task with category
  const addTask = (title, category) => {
    const newTask = {
      id: Date.now(),
      title,
      category,
      completed: false,
    };
    setTasks([newTask, ...tasks]);
  };

  const deleteTask = (id) => {
    setTasks(tasks.filter((task) => task.id !== id));
  };

  const toggleTask = (id) => {
    setTasks(
      tasks.map((task) =>
        task.id === id
          ? { ...task, completed: !task.completed }
          : task
      )
    );
  };

  const updateTask = (id, newTitle) => {
    setTasks(
      tasks.map((task) =>
        task.id === id ? { ...task, title: newTitle } : task
      )
    );
  };

  // ✅ FULL FILTER LOGIC
  const filteredTasks = tasks
    .filter((task) =>
      task.title.toLowerCase().includes(search.toLowerCase())
    )
    .filter((task) => {
      if (filter === "completed") return task.completed;
      if (filter === "pending") return !task.completed;
      return true;
    })
    .filter((task) => {
      if (categoryFilter === "All") return true;
      return task.category === categoryFilter;
    });

  return (
    <div className="container">
      <h1>Advanced Task Manager 🚀</h1>

      <TaskForm addTask={addTask} />

      <SearchFilter
        setSearch={setSearch}
        setFilter={setFilter}
        setCategoryFilter={setCategoryFilter} // ✅ pass prop
      />

      <TaskList
        tasks={filteredTasks}
        deleteTask={deleteTask}
        toggleTask={toggleTask}
        updateTask={updateTask}
      />
      
    </div>
    
  );
}

export default App;