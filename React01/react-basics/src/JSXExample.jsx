import React from "react"; // Import React for JSX support

// Define a functional component named JSXExample
function JSXExample() {
  const name = "John"; // Define a variable for name
  const age = 20;      // Define a variable for age
  return (
    <div> {/* Parent div to wrap the content */}
      <h3>JSX Example</h3> {/* Heading for this example */}
      <p>Hello, my name is {name} and I am {age} years old.</p> {/* Show values using curly braces */}
    </div>
  );
}

export default JSXExample; // Export component so it can be imported elsewhere