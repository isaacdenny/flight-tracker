import Homepage from "./pages/Homepage";
import { BrowserRouter, Route, Routes } from "react-router-dom"
import "./App.css";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Homepage/>} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
