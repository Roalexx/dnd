import React from "react";
import { useNavigate } from "react-router-dom";
import "./TopBar.css"; // doğru dizindeyse bu yeterli

function TopBar() {
  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/");
  };

  return (
    <div className="topbar">
      <h3 className="topbar-title" onClick={() => navigate("/dashboard")}>
        DND Dashboard
      </h3>
      <div>
        {token ? (
          <button onClick={handleLogout} className="topbar-button">
            Logout
          </button>
        ) : (
          <button onClick={() => navigate("/")} className="topbar-button">
            Login
          </button>
        )}
      </div>
    </div>
  );
}

export default TopBar;
