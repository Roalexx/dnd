import React, { useEffect, useState } from "react";
import { useNavigate, useParams } from "react-router-dom";
import api from "../api/axios";

function CharacterDetailsPage() {
  const { id } = useParams();
  const navigate = useNavigate();
  const [character, setCharacter] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchCharacter = async () => {
      try {
        const token = localStorage.getItem("token");
        const res = await api.get(`/characters/${id}`, {
          headers: { Authorization: `Bearer ${token}` },
        });
        setCharacter(res.data);
      } catch (err) {
        console.error("Karakter verisi alınamadı:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchCharacter();
  }, [id]);

  if (loading) return <p>Yükleniyor...</p>;
  if (!character) return <p>Karakter bilgisi bulunamadı.</p>;

  const renderList = (label, items, fields) => (
    <div>
      <h4>{label}</h4>
      {items?.length === 0 ? (
        <p>Yok</p>
      ) : (
        <ul>
          {items.map((item, index) => (
            <li key={index}>
              {fields.map((f) => item[f]).join(" - ")}
            </li>
          ))}
        </ul>
      )}
    </div>
  );

  return (
    <div>
      <button onClick={() => navigate("/dashboard")}>← Geri Dön</button>
      <h2>{character.name}</h2>

      <p><strong>Level:</strong> {character.level}</p>
      <p><strong>Class ID:</strong> {character.class_id}</p>
      <p><strong>Subclass ID:</strong> {character.subclass_id}</p>
      <p><strong>Race ID:</strong> {character.race_id}</p>
      <p><strong>Feat ID:</strong> {character.feat_id}</p>
      <p><strong>Alignment ID:</strong> {character.alignment_id}</p>
      <p><strong>Experience:</strong> {character.experience}</p>

      <h3>Ability Scores</h3>
      <ul>
        {Object.entries(character.ability_scores || {}).map(([key, value]) => (
          <li key={key}>{key}: {value}</li>
        ))}
      </ul>

      <h3>Combat</h3>
      <p><strong>Hit Points:</strong> {character.hit_points}</p>
      <p><strong>Armor Class:</strong> {character.armor_class}</p>
      <p><strong>Speed:</strong> {character.speed}</p>
      <p><strong>Size ID:</strong> {character.character_size_id}</p>

      <h3>Currency</h3>
      <p>Gold: {character.currency?.gold} | Silver: {character.currency?.silver} | Copper: {character.currency?.copper}</p>

      <h3>Background</h3>
      <p><strong>Background:</strong> {character.background}</p>

      <h3>Text Blocks</h3>
      <p><strong>Personality:</strong> {character.text_blocks?.personality}</p>
      <p><strong>Ideals:</strong> {character.text_blocks?.ideals}</p>
      <p><strong>Bonds:</strong> {character.text_blocks?.bonds}</p>
      <p><strong>Flaws:</strong> {character.text_blocks?.flaws}</p>
      <p><strong>Notes:</strong> {character.text_blocks?.notes}</p>

      <h3>Diğer Özellikler</h3>
      {renderList("Spells", character.spells, ["name", "level"])}
      {renderList("Equipment", character.equipment, ["name", "quantity", "category"])}
      {renderList("Languages", character.languages, ["name"])}
      {renderList("Skills", character.skills, ["name", "ability_score"])}
      {renderList("Traits", character.traits, ["name", "description"])}
      {renderList("Saving Throws", character.saving_throws, ["ability_score", "value"])}
      {renderList("Conditions", character.conditions, ["name", "description"])}
    </div>
  );
}

export default CharacterDetailsPage;
