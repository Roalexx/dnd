import React from "react";
import { useNavigate } from "react-router-dom";

function TopBar() {
  const navigate = useNavigate();
  const token = localStorage.getItem("token");

  const handleLogout = () => {
    localStorage.removeItem("token");
    navigate("/"); // login sayfasına gönder
  };

  return (
    <div style={styles.navbar}>
      <h3 style={styles.title} onClick={() => navigate("/dashboard")}>DND Dashboard</h3>
      <div>
        {token ? (
          <button onClick={handleLogout} style={styles.button}>Logout</button>
        ) : (
          <button onClick={() => navigate("/")} style={styles.button}>Login</button>
        )}
      </div>
    </div>
  );
}

const styles = {
  navbar: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    padding: "10px 20px",
    backgroundColor: "#222",
    color: "white",
  },
  title: {
    cursor: "pointer",
  },
  button: {
    padding: "6px 12px",
    backgroundColor: "#555",
    color: "white",
    border: "none",
    borderRadius: "4px",
    cursor: "pointer",
  }
};

export default TopBar;
