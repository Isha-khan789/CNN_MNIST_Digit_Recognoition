import React from "react";
import Navbar from "./components/Navbar";
import Hero from "./components/Hero";

const App = () => {
  return (
    <div className="min-h-screen bg-slate-950">
      <Navbar />
      <Hero />
    </div>
  );
};

export default App;
