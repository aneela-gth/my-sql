const express = require("express");
const sqlite3 = require("sqlite3").verbose();
const path = require("path");

const app = express();
app.use(express.json());
app.use(express.static(path.join(__dirname, "public")));

const db = new sqlite3.Database("students.db");

db.run(`CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT,
    age INTEGER,
    grade TEXT
)`);

// GET all students
app.get("/api/students", (req, res) => {
  db.all("SELECT * FROM students", [], (err, rows) => {
    res.json(rows);
  });
});

// ADD student
app.post("/api/students", (req, res) => {
  const { name, email, age, grade } = req.body;

  db.run(
    `INSERT INTO students(name, email, age, grade) VALUES(?,?,?,?)`,
    [name, email, age, grade],
    function (err) {
      res.json({ id: this.lastID });
    }
  );
});

// UPDATE student
app.put("/api/students/:id", (req, res) => {
  const { name, email, age, grade } = req.body;
  const id = req.params.id;

  db.run(
    `UPDATE students SET name=?, email=?, age=?, grade=? WHERE id=?`,
    [name, email, age, grade, id],
    () => res.json({ updated: true })
  );
});

// DELETE student
app.delete("/api/students/:id", (req, res) => {
  db.run(`DELETE FROM students WHERE id=?`, [req.params.id], () =>
    res.json({ deleted: true })
  );
});

app.listen(3000, () => console.log("Server running on http://localhost:3000"));
