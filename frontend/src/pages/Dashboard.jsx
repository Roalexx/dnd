import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";
import "../components/Dashboard.css";

function Dashboard() {
  const [ownedCharacters, setOwnedCharacters] = useState([]);
  const [dmCharacters, setDmCharacters] = useState([]);
  const [loading, setLoading] = useState(true);
  const navigate = useNavigate();

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      navigate("/");
      return;
    }

    const fetchCharacters = async () => {
      try {
        const response = await api.get("/characters/my-characters", {
          headers: {
            Authorization: `Bearer ${token}`,
          },
          withCredentials: true,
        });
        setOwnedCharacters(response.data.owned_characters);
        setDmCharacters(response.data.dm_characters);
        setLoading(false);
      } catch (error) {
        console.error("Error while fetching characters:", error);
        navigate("/");
      }
    };

    fetchCharacters();
  }, [navigate]);

  const goToCharacter = (id) => {
    navigate(`/characters/${id}`);
  };

  if (loading) return <p>Loading...</p>;

  return (
    <div>
      <h2>Dashboard</h2>

      <section>
        <h3>Your Characters</h3>
        <button className="add-button" onClick={() => navigate("/create-character")}>＋</button>
        {ownedCharacters.length === 0 ? (
          <p>You don't have any characters.</p>
        ) : (
          <ul>
            {ownedCharacters.map((char) => (
              <li key={char.id} style={{ display: "flex", alignItems: "center", gap: "12px" }}>
                <span onClick={() => navigate(`/characters/${char.id}`)} style={{ cursor: "pointer" }}>
                  {char.name} - Level {char.level}
                </span>
                <button
                  style={{
                    padding: "4px 12px",
                    background: "linear-gradient(90deg, #23272a 0%, #444950 100%)",
                    color: "#e0e0e0",
                    border: "2px solid #444950",
                    borderRadius: "8px",
                    fontFamily: "MedievalSharp, serif",
                    cursor: "pointer",
                    fontWeight: "bold"
                  }}
                  onClick={() => navigate(`/battle/${char.id}`)}
                >
                  Join Battle
                </button>
              </li>
            ))}
          </ul>
        )}
      </section>

      <section>
        <h3>Characters You Manage (as DM)</h3>
        {dmCharacters.length === 0 ? (
          <p>You are not managing any characters.</p>
        ) : (
          <ul>
            {dmCharacters.map((char) => (
              <li
                key={char.id}
                onClick={() => goToCharacter(char.id)}
                style={{ cursor: "pointer", color: "blue", textDecoration: "underline" }}
              >
                {char.name} - Level {char.level}
              </li>
            ))}
          </ul>
        )}
      </section>
    </div>
  );
}

export default Dashboard;
