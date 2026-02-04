import React, { useState } from "react";
import ClauseCard from "./ClauseCard";

function Dashboard() {
  const [clauses, setClauses] = useState([]);

  const loadData = async () => {
    const res = await fetch("http://127.0.0.1:8000/get_results");
    const data = await res.json();
    setClauses(data);
  };

  return (
    <div style={{ padding: "20px" }}>
      <h1>PlainLaw Assistant</h1>
      <button onClick={loadData}>Load Results</button>

      {clauses.map((item, idx) => (
        <ClauseCard key={idx} {...item} />
      ))}
    </div>
  );
}

export default Dashboard;
