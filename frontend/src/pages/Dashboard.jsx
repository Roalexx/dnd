import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";

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
        console.error("Karakterler alınırken hata oluştu:", error);
        navigate("/");
      }
    };

    fetchCharacters();
  }, [navigate]);

  const goToCharacter = (id) => {
    navigate(`/characters/${id}`);
  };

  if (loading) return <p>Yükleniyor...</p>;

  return (
    <div>
      <h2>Dashboard</h2>

      <section>
        <h3>Sahip Olduğun Karakterler</h3>
        {ownedCharacters.length === 0 ? (
          <p>Hiç karakterin yok.</p>
        ) : (
          <ul>
            {ownedCharacters.map((char) => (
              <li key={char.id} onClick={() => navigate(`/characters/${char.id}`)}>
                {char.name} - Level {char.level}
              </li>
            ))}
          </ul>
        )}
      </section>

      <section>
        <h3>Yönettiğin Karakterler (DM olarak)</h3>
        {dmCharacters.length === 0 ? (
          <p>DM olduğun karakter yok.</p>
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
