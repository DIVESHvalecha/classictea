import React from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
function Home() {
  return <h3>Home Page</h3>;
  
}
function About() {
  return <h3>About Page</h3>;
}
function RouterExample() {
  return (
    <Router>
      <div>
        <h3>Router Example</h3>
        <Link to="/">Home</Link> | <Link to="/about">About</Link>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </div>
    </Router>
  );
}

export default RouterExample;