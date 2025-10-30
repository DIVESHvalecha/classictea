// import { useState } from "react";
// import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
// import UserForm from "./UserForm";
// import UserCard from "./UserCard";
// import UsersList from "./UsersList";

// function App() {
//   const [userName, setUserName] = useState("");
//   const [users, setUsers] = useState([]); // For list rendering

//   const addUser = (name) => {
//     setUsers([...users, name]); // Event + Key usage
//   };

//   return (
//     <Router>
//       <div style={{ textAlign: "center", marginTop: "40px" }}>
//         <h1>React Basics with Events, Router, Refs & Keys ✅</h1>

//         {/* Navigation Menu */}
//         <nav style={{ marginBottom: "20px" }}>
//           <Link to="/" style={{ marginRight: "10px" }}>Home</Link>
//           <Link to="/users">Users List</Link>
//         </nav>

//         {/* Routing */}
//         <Routes>
//           <Route
//             path="/"
//             element={
//               <>
//                 <UserForm setUserName={setUserName} addUser={addUser} />
//                 {userName && <UserCard name={userName} />}
//               </>
//             }
//           />
//           <Route path="/users" element={<UsersList users={users} />} />
//         </Routes>
//       </div>
//     </Router>
//   );
// }

// export default App;


// Import the main React library so you can use JSX and React features
import React from "react";

// Import your JSX example component from JSXExample.js
import JSXExample from "./JSXExample";

// Import the Welcome component from Welcome.js
import Welcome from "./Welcome";

// Import the Counter component (demonstrates State) from Counter.js
import Counter from "./Counter";

// Import the FormExample component (demonstrates Forms) from FormExample.js
import FormExample from "./FormExample";

// Define the main App component
function App() {
  // The return statement defines what should be displayed on the page
  return (
    <div> {/* This is a container div for all components below */}
      <JSXExample /> {/* Render the JSXExample component */}
      <Welcome name="Ankita" /> {/* Render Welcome, passing "Ankita" as the name prop */}
      <Welcome name="Rahul" />   {/* Render Welcome again, with "Rahul" as the name prop */}
      <Counter />  {/* Render the Counter component which shows state usage */}
      <FormExample /> {/* Render the FormExample component that shows handling forms */}
    </div>
  );
}

// Export the App component so it can be used by other files (like index.js)
export default App;
