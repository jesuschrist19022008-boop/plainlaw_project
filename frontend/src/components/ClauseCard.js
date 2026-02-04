import React from "react";

function ClauseCard({ clause, label, score }) {
  const borderColor =
    label === "Liability/Limitations" ? "red" : "green";

  return (
    <div style={{
      border: `2px solid ${borderColor}`,
      padding: "15px",
      margin: "10px 0",
      borderRadius: "10px"
    }}>
      <p><b>Clause:</b> {clause}</p>
      <p><b>Category:</b> {label}</p>
      <p><b>Confidence:</b> {score.toFixed(2)}</p>
    </div>
  );
}

export default ClauseCard;