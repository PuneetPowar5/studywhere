import React from "react";
import { Link } from "react-router-dom";
import Logout from "./Logout";
import "./Navbar.css";

const Navbar = () => {
  return (
    <nav className="nav">
      <h1>
        <Link to="/" className="home">
          STUDYWHERE - UTM
        </Link>
      </h1>
      <ul className="Links">
        <Link to="/DH" className="DhNav">
          <li>DH</li>
        </Link>
        <Link to="/DV" className="DvNav">
          <li>DV</li>
        </Link>
        <Link to="/MN" className="MnNav">
          <li>MN</li>
        </Link>
        <Link to="/IB" className="IbNav">
          <li>IB</li>
        </Link>
        <Link to="/KN" className="KnNav">
          <li>KN</li>
        </Link>
        <Link to="/CCT" className="CcNav">
          <li>CCT</li>
        </Link>
        <Link to="/Events" className="EventNav">
          <li>Events</li>
        </Link>
        <Link to="/Reservations" className="ReserveNav">
          <li>Your Reservations</li>
        </Link>
        <div className="Logout">
          <Logout />
        </div>
      </ul>
    </nav>
  );
};

export default Navbar;
