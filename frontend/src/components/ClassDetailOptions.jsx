import React, { useEffect, useState } from "react";
import "./ClassDetailOptions.css"; // (Opsiyonel stil için)

function ClassDetailOptions({ selectedClass, classData }) {
  const [selectedProficiencies, setSelectedProficiencies] = useState([]);
  const [selectedEquipment, setSelectedEquipment] = useState("");

  const classInfo = classData[selectedClass];

  useEffect(() => {
    setSelectedProficiencies([]);
    setSelectedEquipment("");
  }, [selectedClass]);

  if (!classInfo) return null;

  const profChoices = classInfo.proficiency_choices || { choose: 0, from: [] };
  const equipOptions = classInfo.starting_equipment_options || { choose: 0, from: [] };

  const handleProficiencyChange = (index, value) => {
    const updated = [...selectedProficiencies];
    updated[index] = value;
    setSelectedProficiencies(updated);
  };

  return (
    <div className="class-detail-options">
      <h3>{classInfo.name} Details</h3>

      <p><strong>Hit Die:</strong> d{classInfo.hit_die}</p>

      <p><strong>Saving Throws:</strong> {
        Array.isArray(classInfo.saving_throws)
        ? classInfo.saving_throws.map(s => typeof s === "string" ? s : s.name).join(", ")
        : "N/A"
      }</p>

      {/* Proficiency Dropdownları */}
      {profChoices.choose > 0 && (
        <div>
          <strong>Choose {profChoices.choose} Proficiencies:</strong>
          {[...Array(profChoices.choose)].map((_, idx) => (
            <select
              key={idx}
              value={selectedProficiencies[idx] || ""}
              onChange={(e) => handleProficiencyChange(idx, e.target.value)}
            >
              <option value="">-- Select --</option>
              {profChoices.from.map((p, i) => (
                <option key={i} value={p} disabled={selectedProficiencies.includes(p)}>
                  {p}
                </option>
              ))}
            </select>
          ))}
        </div>
      )}

      {/* Ekipman Seçimi */}
      {equipOptions.from?.length > 0 && (
        <div style={{ marginTop: "10px" }}>
          <strong>Choose Starting Equipment:</strong>
          <select value={selectedEquipment} onChange={(e) => setSelectedEquipment(e.target.value)}>
            <option value="">-- Select --</option>
            {equipOptions.from.map((item, idx) => (
              <option key={idx} value={item}>{item}</option>
            ))}
          </select>
        </div>
      )}

      {/* Özellikler */}
      {classInfo.features?.length > 0 && (
        <div style={{ marginTop: "15px" }}>
          <strong>Features:</strong>
          <ul>
            {classInfo.features.map((feat, idx) => (
              <li key={idx}><b>Lvl {feat.level} – {feat.name}:</b> {feat.desc}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default ClassDetailOptions;
