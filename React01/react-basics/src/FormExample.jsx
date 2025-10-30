import React, { useState } from "react"; // Import React and useState

// Define functional component
function FormExample() {
  const [name, setName] = useState(""); // useState for an input field

  // Function for handling form submission
  const handleSubmit = (e) => {
    e.preventDefault(); // Prevents the page from refreshing
    alert("Hello, " + name + "!"); // Show alert with name entered
  };

  return (
    <div> {/* Parent div */}
      <h3>Form Example</h3> {/* Heading */}
      <form onSubmit={handleSubmit}> {/* Form with submit handler */}
        <input
          type="text"
          placeholder="Enter your name"
          value={name}
          onChange={(e) => setName(e.target.value)} // Update name state on input change
        />
        <button type="submit">Submit</button> {/* Submit button */}
      </form>
    </div>
  );
}

export default FormExample; // Export component