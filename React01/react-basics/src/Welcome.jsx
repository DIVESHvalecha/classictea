import React from "react"; // Import React library

// Define a functional component that takes props
function Welcome(props) {
  return <h2>Hello, {props.name}!</h2>; // Renders a greeting using prop
}

export default Welcome; // Export component for use in other files