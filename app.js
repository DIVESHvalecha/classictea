// 1. Callback Example
function greetUser(name, callback) {
    console.log("Hello, " + name);
    callback();
}

greetUser("Jeet", function () {
    console.log("Callback function executed!\n");
});

// 2. Event Example
const EventEmitter = require("events");
const event = new EventEmitter();

event.on("greet", () => {
    console.log("Event triggered: Hello from EventEmitter!\n");
});

event.emit("greet");

// 3. Loop Example
console.log("Loop Example:");
for (let i = 1; i <= 5; i++) {
    console.log("Count:", i);
}
console.log("\n");

// 4. Creating a Simple Express App
const express = require("express");
const app = express();

// Home route
app.get("/", (req, res) => {
    res.send("Welcome to the Express App!");
});

// About route
app.get("/about", (req, res) => {
    res.send("This is the About Page!");
});

// Start server
const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Express server running on http://localhost:${PORT}`);
});
