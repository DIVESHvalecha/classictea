import React, { useState } from "react"; // Import React and useState hook

// Define functional component
function Counter() {
  const [count, setCount] = useState(0); // useState creates a variable 'count', initial value 0

  return (
    <div> {/* Parent div */}
      <h3>State Example</h3> {/* Heading */}
      <p>Count: {count}</p> {/* Show current count */}
      <button onClick={() => setCount(count + 1)}>Increment</button> {/* Button to increase count */}
    </div>
  );
}

export default Counter; // Export component