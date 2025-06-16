import React, { useEffect, useState } from "react";

function RaceDetailOptions({
  selectedRace,
  onAbilityBonusChooseChange,
  onFixedAbilityBonusesChange,
  onLanguageOptionSelect,
  onProficiencySelect,
}) {
  const [selectedAbilityBonuses, setSelectedAbilityBonuses] = useState({});
  const [selectedLanguage, setSelectedLanguage] = useState("");
  const [selectedProficiency, setSelectedProficiency] = useState("");

  useEffect(() => {
    let fixed = [];

    if (selectedRace?.race_ability_bonuses?.length > 0) {
      fixed = selectedRace.race_ability_bonuses.map((b) => ({
        name: b.ability_score?.name,
        value: b.ability_bonus,
      }));
    } else if (
      selectedRace?.ability_score?.name &&
      selectedRace?.ability_bonus
    ) {
      fixed = [
        {
          name: selectedRace.ability_score.name,
          value: selectedRace.ability_bonus,
        },
      ];
    }

    onFixedAbilityBonusesChange(fixed);
  }, [selectedRace, onFixedAbilityBonusesChange]);

  useEffect(() => {
    const selectedValues = Object.values(selectedAbilityBonuses).filter(
      Boolean
    );
    onAbilityBonusChooseChange(selectedValues);
  }, [selectedAbilityBonuses, onAbilityBonusChooseChange]);

  useEffect(() => {
    onLanguageOptionSelect?.(selectedLanguage);
  }, [selectedLanguage, onLanguageOptionSelect]);

  useEffect(() => {
    onProficiencySelect?.(selectedProficiency);
  }, [selectedProficiency, onProficiencySelect]);

  if (!selectedRace) return null;

  const {
    alignment,
    age,
    language_desc,
    size,
    size_description,
    speed,
    race_languages = [],
    race_traits = [],
    race_proficiency_options = [],
    race_ability_bonus_options = [],
    race_language_options = [],
    ability_bonus_choose,
  } = selectedRace;

  const abilityBonusChooseCount = ability_bonus_choose || 0;

  const handleAbilityBonusChange = (index, value) => {
    setSelectedAbilityBonuses((prev) => ({ ...prev, [index]: value }));
  };

  return (
    <div>
      <h3>Race Traits</h3>
      <p>
        <strong>Alignment:</strong> {alignment}
      </p>
      <p>
        <strong>Age:</strong> {age}
      </p>
      <p>
        <strong>Size:</strong> {size}
      </p>
      <p>
        <strong>Size Description:</strong> {size_description}
      </p>
      <p>
        <strong>Base Speed:</strong> {speed} feet
      </p>

      {/* Languages */}
      <div style={{ marginTop: "1rem" }}>
        <h4>Known Languages</h4>
        <p>{language_desc}</p>
        <ul>
          {race_languages.map((lang) => (
            <li key={lang.language_id}>{lang.language_name}</li>
          ))}
        </ul>
      </div>

      {/* Select Extra Language */}
      {race_language_options.length > 0 && (
        <div style={{ marginTop: "1rem" }}>
          <label>Choose an Additional Language</label>
          <select
            value={selectedLanguage}
            onChange={(e) => setSelectedLanguage(e.target.value)}
            style={{ width: "100%", marginTop: "0.5rem" }}
          >
            <option value="">Select</option>
            {race_language_options.map((lang) => (
              <option key={lang.language_id} value={lang.language_name}>
                {lang.language_name}
              </option>
            ))}
          </select>
        </div>
      )}

      {/* Fixed Ability Bonuses */}
      {(selectedRace?.race_ability_bonuses?.length > 0 ||
        (selectedRace?.ability_score?.name && selectedRace?.ability_bonus)) && (
        <div style={{ marginTop: "1.5rem" }}>
          <h4>Racial Ability Score Bonuses</h4>
          <ul>
            {selectedRace.race_ability_bonuses?.map((bonus, idx) => (
              <li key={idx}>
                +{bonus.ability_bonus} to{" "}
                <strong>{bonus.ability_score?.name}</strong>
              </li>
            ))}
            {!selectedRace.race_ability_bonuses &&
              selectedRace.ability_score?.name &&
              selectedRace.ability_bonus && (
                <li>
                  +{selectedRace.ability_bonus} to{" "}
                  <strong>{selectedRace.ability_score.name}</strong>
                </li>
              )}
          </ul>
        </div>
      )}

      {/* Choose Ability Bonuses */}
      {abilityBonusChooseCount > 0 && race_ability_bonus_options.length > 0 && (
        <div style={{ marginTop: "1rem" }}>
          <label>
            Choose {abilityBonusChooseCount} ability score
            {abilityBonusChooseCount > 1 ? "s" : ""} to receive +1
          </label>
          {[...Array(abilityBonusChooseCount)].map((_, idx) => (
            <select
              key={`ability-bonus-${idx}`}
              style={{ width: "100%", marginTop: "0.5rem" }}
              onChange={(e) => handleAbilityBonusChange(idx, e.target.value)}
              value={selectedAbilityBonuses[idx] || ""}
            >
              <option value="">Select</option>
              {race_ability_bonus_options
                .filter(
                  (opt) =>
                    !Object.values(selectedAbilityBonuses).includes(
                      opt.ability_score_name
                    ) || selectedAbilityBonuses[idx] === opt.ability_score_name
                )
                .map((opt) => (
                  <option
                    key={opt.ability_score_id}
                    value={opt.ability_score_name}
                  >
                    {opt.ability_score_name}
                  </option>
                ))}
            </select>
          ))}
        </div>
      )}

      {/* Choose Proficiency */}
      {race_proficiency_options.length > 0 && (
        <div style={{ marginTop: "1.5rem" }}>
          <h4>Choose a Tool or Skill Proficiency</h4>
          <select
            value={selectedProficiency}
            onChange={(e) => setSelectedProficiency(e.target.value)}
            style={{ width: "100%", marginTop: "0.5rem" }}
          >
            <option value="">Select</option>
            {race_proficiency_options.map((prof) => (
              <option key={prof.proficiency_id} value={prof.proficiency_id}>
                {prof.proficiency_type}: {prof.proficiency_name}
              </option>
            ))}
          </select>
        </div>
      )}

      {/* Traits */}
      {race_traits.length > 0 && (
        <div style={{ marginTop: "1rem" }}>
          <h4>Special Traits</h4>
          <ul>
            {race_traits.map((trait) => (
              <li key={trait.trait_id}>
                <strong>{trait.trait_name}:</strong> {trait.trait_description}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default RaceDetailOptions;
