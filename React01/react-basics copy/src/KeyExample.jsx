import React from "react";
function KeyExample() {
  const fruits = ["Apple", "Banana", "Cherry"];
  return (
    <div>
      <h3>Keys Example</h3>
      <ul>
        {fruits.map((fruit, index) => (
          <li key={index}>{fruit}</li>
        ))}
      </ul>
    </div>
  );
}
export default KeyExample;
