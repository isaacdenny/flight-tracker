import React from "react";
import { Link } from "react-router-dom";

const Homepage = () => {
  return (
    <div className="App">
      <header className="App-header">
        <h1>TouchNGo</h1>
        <p>Paramoter Flight Tracker</p>
        <Link to="/liveview">
          liveview
        </Link>
      </header>
    </div>
  );
};

export default Homepage;
