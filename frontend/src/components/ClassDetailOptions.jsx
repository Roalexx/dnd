import React, { useEffect, useState } from "react";

function ClassDetailOptions({
  selectedClass,
  classLevelData,
  equipmentList = [],
  proficiencyList = [],
  abilityScoreList = [],
}) {
  const [selectedOptions, setSelectedOptions] = useState({});

  useEffect(() => {
    setSelectedOptions({});
  }, [selectedClass]);

  if (!selectedClass || !classLevelData) return null;

  const getNameFromList = (list, id) => {
    const found = list.find((item) => item.id === id);
    return found?.name || `#${id}`;
  };

  const {
    name,
    hit_die,
    spellcasting_description,
    proficiency_choices_desc,
    proficiency_choices_choose,
    classes_starting_equipment = [],
    classes_starting_equipment_options = [],
    classes_proficiency_choices = [],
    class_multi_classing_proficiencies = [],
    classes_proficiencies = [],
    classes_saving_throws = [],
    features = [],
    spells_classes = [],
  } = selectedClass;

  const {
    cantrips_known,
    spells_known,
    level,
    prof_bonus,
    ability_score_bonuses,
  } = classLevelData;

  // 🔧 spells_classes doğrudan kullanılacak
  const classSpells = spells_classes.map((s) => ({
    id: s.spells_id,
    name: s.spell_name,
    description: s.spell_description,
  }));

  const renderDropdowns = (title, prefix, count, options = [], desc = "") => (
    <div style={{ marginBottom: "1rem" }}>
      {title && <h4>{title}</h4>}
      {desc && <p style={{ fontStyle: "italic", marginTop: "-0.5rem" }}>{desc}</p>}

      {[...Array(count)].map((_, idx) => {
        const key = `${prefix}-${idx}`;
        const selectedValue = selectedOptions[key] || "";

        const filteredOptions = options.filter((opt) => {
          const optionId = (opt.id || opt.index || opt.name)?.toString();
          return (
            !Object.entries(selectedOptions).some(
              ([k, val]) => k !== key && val === optionId
            ) || selectedValue === optionId
          );
        });

        return (
          <div key={key}>
            <select
              value={selectedValue}
              onChange={(e) =>
                setSelectedOptions((prev) => ({
                  ...prev,
                  [key]: e.target.value,
                }))
              }
              style={{ display: "block", width: "100%", marginBottom: "0.5rem" }}
            >
              <option value="">Seçim {idx + 1}</option>
              {filteredOptions.map((opt, i) => (
                <option
                  key={i}
                  value={opt.id}
                  title={opt.description || ""}
                >
                  {opt.name}
                </option>
              ))}
            </select>
          </div>
        );
      })}
    </div>
  );

  return (
    <div className="class-detail-container">
      <h2>{name} - Class Details</h2>

      <p><strong>Level:</strong> {level}</p>
      <p><strong>Hit Die:</strong> d{hit_die}</p>
      <p><strong>Proficiency Bonus:</strong> {prof_bonus}</p>
      <p><strong>Ability Score Bonus:</strong> {ability_score_bonuses}</p>

      {spellcasting_description && <p>{spellcasting_description}</p>}

      {cantrips_known > 0 &&
        renderDropdowns("Cantrip Seçimi", "cantrip", cantrips_known, classSpells)}

      {spells_known > 0 &&
        renderDropdowns("Spell Seçimi", "spell", spells_known, classSpells)}

      {classes_starting_equipment.length > 0 && (
        <p>
          <strong>Başlangıç Ekipmanları:</strong>{" "}
          {classes_starting_equipment
            .map(
              (eq) =>
                `${getNameFromList(equipmentList, eq.equipment_id)} (x${eq.quantity})`
            )
            .join(", ")}
        </p>
      )}

      {classes_starting_equipment_options.length > 0 && (
        <div>
          <p><strong>Başlangıç Ekipman Seçenekleri:</strong> {selectedClass.starting_equipment_options_desc || ""}</p>
          {renderDropdowns(
            null,
            "equipment",
            selectedClass.starting_equipment_options_choose || 1,
            classes_starting_equipment_options.map((opt) => ({
              id: opt.equipment_id,
              name: getNameFromList(equipmentList, opt.equipment_id),
            }))
          )}
        </div>
      )}

      {classes_proficiency_choices.length > 0 &&
        renderDropdowns(
          "Proficiency Seçimi",
          "prof",
          proficiency_choices_choose || 1,
          classes_proficiency_choices.map((p) => ({
            id: p.proficiency_id,
            name: getNameFromList(proficiencyList, p.proficiency_id),
          })),
          proficiency_choices_desc
        )}

      {classes_proficiencies.length > 0 && (
        <p>
          <strong>Varsayılan Proficiencies:</strong>{" "}
          {classes_proficiencies
            .map((p) => getNameFromList(proficiencyList, p.proficiency_id))
            .join(", ")}
        </p>
      )}

      {class_multi_classing_proficiencies.length > 0 && (
        <p>
          <strong>Multi-Classing Proficiencies:</strong>{" "}
          {class_multi_classing_proficiencies
            .map((p) => getNameFromList(proficiencyList, p.proficiency_id))
            .join(", ")}
        </p>
      )}

      {classes_saving_throws.length > 0 && (
        <p>
          <strong>Saving Throws:</strong>{" "}
          {classes_saving_throws
            .map((s) => getNameFromList(abilityScoreList, s.ability_score_id))
            .join(", ")}
        </p>
      )}

      {features.filter((f) => f.level === 1).length > 0 && (
        <div>
          <h4>1. Seviye Özellikler</h4>
          {features
            .filter((f) => f.level === 1)
            .map((f, i) => (
              <div key={i} className="feature-box">
                <strong>{f.name}</strong>
                <p>{f.description}</p>
              </div>
            ))}
        </div>
      )}
    </div>
  );
}

export default ClassDetailOptions;
