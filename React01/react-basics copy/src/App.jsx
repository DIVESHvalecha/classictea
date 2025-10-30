// App.js
import React from "react";
import EventExample from "./EventExample";
import RouterExample from "./RouterExample";
import RefExample from "./RefExample";
import KeyExample from "./KeyExample";

function App() {
  return (
    <div>
      <h2 style={{ textAlign: "center", marginTop: "20px" }}>
        React Core Concepts Examples
      </h2>
      <EventExample />
      <RouterExample />
      <RefExample />
      <KeyExample />
    </div>
  );
}

export default App;
