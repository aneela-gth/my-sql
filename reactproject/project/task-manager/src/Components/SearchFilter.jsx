import React from "react";

function SearchFilter({ setSearch, setFilter, setCategoryFilter }) {
  return (
    <div>
      <input
        type="text"
        placeholder="Search task..."
        onChange={(e) => setSearch(e.target.value)}
      />

      <select onChange={(e) => setFilter(e.target.value)}>
        <option value="all">All</option>
        <option value="completed">Completed</option>
        <option value="pending">Pending</option>
      </select>

      <select onChange={(e) => setCategoryFilter(e.target.value)}>
        <option>All</option>
        <option>Python</option>
        <option>JavaScript</option>
        <option>CSS</option>
        <option>React</option>
      </select>
    </div>
  );
}

export default SearchFilter;