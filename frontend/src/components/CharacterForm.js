import React, { useEffect, useState } from "react";
import api from "../api/axios";

function CharacterForm({ formData = {}, onChange, readOnly = false }) {
  const [races, setRaces] = useState([]);
  const [classes, setClasses] = useState([]);
  const [alignments, setAlignments] = useState([]);
  const [sizes, setSizes] = useState([]);

  useEffect(() => {
    const fetchDropdowns = async () => {
      try {
        const token = localStorage.getItem("token");
        const config = { headers: { Authorization: `Bearer ${token}` } };

        const [raceRes, classRes, alignmentRes, sizeRes] = await Promise.all([
          api.get("/races", config),
          api.get("/classes", config),
          api.get("/alignments", config),
          api.get("/character-sizes", config),
        ]);

        setRaces(raceRes.data);
        setClasses(classRes.data);
        setAlignments(alignmentRes.data);
        setSizes(sizeRes.data);
      } catch (err) {
        console.error("Dropdown verileri alınamadı:", err);
      }
    };
    fetchDropdowns();
  }, []);

  const handleInput = (e) => {
    if (readOnly) return;
    const { name, value } = e.target;
    onChange?.({ ...formData, [name]: value });
  };

  return (
    <form>
      <label>Karakter Adı:</label>
      <input
        type="text"
        name="name"
        value={formData.name || ""}
        onChange={handleInput}
        disabled={readOnly}
      /><br />

      <label>Irk:</label>
      <select
        name="race_id"
        value={formData.race_id || ""}
        onChange={handleInput}
        disabled={readOnly}
      >
        <option value="">Seçin</option>
        {races.map((r) => (
          <option key={r.id} value={r.id}>{r.name}</option>
        ))}
      </select><br />

      <label>Sınıf:</label>
      <select
        name="class_id"
        value={formData.class_id || ""}
        onChange={handleInput}
        disabled={readOnly}
      >
        <option value="">Seçin</option>
        {classes.map((c) => (
          <option key={c.id} value={c.id}>{c.name}</option>
        ))}
      </select><br />

      <label>Hizalanma:</label>
      <select
        name="alignment_id"
        value={formData.alignment_id || ""}
        onChange={handleInput}
        disabled={readOnly}
      >
        <option value="">Seçin</option>
        {alignments.map((a) => (
          <option key={a.id} value={a.id}>{a.name}</option>
        ))}
      </select><br />

      <label>Boyut:</label>
      <select
        name="character_size_id"
        value={formData.character_size_id || ""}
        onChange={handleInput}
        disabled={readOnly}
      >
        <option value="">Seçin</option>
        {sizes.map((s) => (
          <option key={s.id} value={s.id}>{s.name}</option>
        ))}
      </select><br />

      {/* Diğer alanlar buraya eklenebilir: statlar, image, background, vs. */}
    </form>
  );
}

export default CharacterForm;
