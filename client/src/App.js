import Homepage from "./pages/Homepage";
import LiveViewPage from "./pages/LiveViewPage"
import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom"
import "./App.css";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Homepage />} />
        <Route path="/liveview" element={<LiveViewPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
