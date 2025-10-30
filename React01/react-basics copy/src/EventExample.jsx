import React, { useState } from "react";
function ClickCounter() {
  // State variable to store click count
  const [count, setCount] = useState(0);
  // Event handler function
  function handleClick() {
    setCount(count + 1);
  }
  return (
    <div>
      <h3>Event Example - Button Click Counter</h3>
      <p>You clicked the button {count} times.</p>
      <button onClick={handleClick}>Click Me</button>
    </div>
  );
}
export default ClickCounter;
