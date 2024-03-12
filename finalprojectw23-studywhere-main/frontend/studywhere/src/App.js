import React, { useState } from "react";
import Home from "./components/Home";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import DH from "./components/DH";
import MN from "./components/MN";
import IB from "./components/IB";
import CCT from "./components/CCT";
import DV from "./components/DV";
import KN from "./components/KN";
import Events from "./components/Events";
import Login from "./components/Login";
import Reservations from "./components/Reservations";

function App() {
  const [loginToken, setLoginToken] = useState();

  if (!loginToken) {
    return <Login setLoginToken={setLoginToken} />;
  }

  return (
    <div>
      <Router>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/DH" element={<DH />} />
          <Route path="/MN" element={<MN />} />
          <Route path="/IB" element={<IB />} />
          <Route path="/CCT" element={<CCT />} />
          <Route path="/DV" element={<DV />} />
          <Route path="/KN" element={<KN />} />
          <Route path="/Events" element={<Events />} />
          <Route path="/Reservations" element={<Reservations />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
