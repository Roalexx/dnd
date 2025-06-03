import React, { useEffect, useState } from "react";
import MultiDropdownWithDescription from "./MultiDropdownWithDescription";

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

  const classSpells = spells_classes.map((s) => ({
    id: s.spells_id,
    name: s.spell_name,
    description: s.spell_description,
  }));

  const renderDropdowns = (title, prefix, count, options = [], desc = "") => (
    <div className="class-detail-options" style={{ marginBottom: "1rem" }}>
      {title && <h4>{title}</h4>}
      {desc && (
        <p className="highlight-label" style={{ marginTop: "-0.5rem" }}>
          {desc}
        </p>
      )}

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
              style={{
                display: "block",
                width: "100%",
                marginBottom: "0.5rem",
              }}
            >
              <option value="">Choice {idx + 1}</option>
              {filteredOptions.map((opt, i) => (
                <option key={i} value={opt.id} title={opt.description || ""}>
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
    <div className="class-detail-options">
      <h2>{name} - Class Details</h2>

      <p>
        <strong>Level:</strong> {level}
      </p>
      <p>
        <strong>Hit Die:</strong> d{hit_die}
      </p>
      <p>
        <strong>Proficiency Bonus:</strong> {prof_bonus}
      </p>
      <p>
        <strong>Ability Score Bonus:</strong> {ability_score_bonuses}
      </p>

      {spellcasting_description && (
        <p className="highlight-label">{spellcasting_description}</p>
      )}

      {cantrips_known > 0 && (
        <MultiDropdownWithDescription
          title="Cantrip Selection"
          prefix="cantrip"
          count={cantrips_known}
          options={classSpells}
        />
      )}

      {spells_known > 0 && (
        <MultiDropdownWithDescription
          title="Spell Selection"
          prefix="spell"
          count={spells_known}
          options={classSpells}
        />
      )}

      {classes_starting_equipment.length > 0 && (
        <p>
          <strong>Starting Equipment:</strong>{" "}
          {classes_starting_equipment
            .map((eq) => {
              const name = eq.equipment_name || `#${eq.equipment_id}`;
              const quantity = eq.equipment_quantity || eq.quantity || 1;
              return `${name} (x${quantity})`;
            })
            .join(", ")}
        </p>
      )}

      {classes_starting_equipment_options.length > 0 && (
        <div>
          <p>
            <strong>Optional Starting Equipment:</strong>{" "}
            {selectedClass.starting_equipment_options_desc || ""}
          </p>
          {renderDropdowns(
            null,
            "equipment",
            selectedClass.starting_equipment_options_choose || 1,
            classes_starting_equipment_options.map((opt) => ({
              id: opt.equipment_id,
              name: opt.equipment_name,
            }))
          )}
        </div>
      )}

      {classes_proficiency_choices.length > 0 &&
        renderDropdowns(
          "Proficiency Selection",
          "prof",
          proficiency_choices_choose || 1,
          classes_proficiency_choices.map((p) => ({
            id: p.proficiency_id,
            name:
              proficiencyList.find((x) => x.id === p.proficiency_id)?.name ||
              `#${p.proficiency_id}`,
          })),
          proficiency_choices_desc
        )}

      {classes_proficiencies.length > 0 && (
        <p>
          <strong>Default Proficiencies:</strong>{" "}
          {classes_proficiencies
            .map(
              (p) =>
                proficiencyList.find((x) => x.id === p.proficiency_id)?.name ||
                `#${p.proficiency_id}`
            )
            .join(", ")}
        </p>
      )}

      {class_multi_classing_proficiencies.length > 0 && (
        <p>
          <strong>Multi-Classing Proficiencies:</strong>{" "}
          {class_multi_classing_proficiencies
            .map(
              (p) =>
                proficiencyList.find((x) => x.id === p.proficiency_id)?.name ||
                `#${p.proficiency_id}`
            )
            .join(", ")}
        </p>
      )}

      {classes_saving_throws.length > 0 && (
        <p>
          <strong>Saving Throws:</strong>{" "}
          {classes_saving_throws
            .map(
              (s) =>
                abilityScoreList.find((x) => x.id === s.ability_score_id)
                  ?.name || `#${s.ability_score_id}`
            )
            .join(", ")}
        </p>
      )}

      {features.filter((f) => f.level === 1).length > 0 && (
        <div>
          <p>
            <strong>Level 1 Features:</strong>
          </p>
          <ul className="feature-list">
            {features
              .filter((f) => f.level === 1)
              .map((f, i) => (
                <li key={i} className="feature-item">
                  <p className="feature-title">{f.name}</p>
                  <p className="feature-description">{f.description}</p>
                </li>
              ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default ClassDetailOptions;
