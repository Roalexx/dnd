import React, { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api/axios";
import ClassDetailOptions from "../components/ClassDetailOptions";
import RaceDetailOptions from "../components/RaceDetailOptions";
import "../components/CharacterForm.css";
import {
  calculateHitPoints,
  calculateArmorClass,
  calculateSpeed,
  getCharacterSizeId,
} from "../utils/characterCalculations";

/* ---------- sabitler ---------- */
const CLASS_DEFAULT_STATS = {
  Barbarian: [15, 14, 14, 8, 10, 8],
  Bard: [8, 14, 14, 10, 10, 15],
  Cleric: [10, 12, 14, 8, 15, 10],
  Druid: [8, 14, 14, 10, 15, 8],
  Fighter: [15, 14, 14, 8, 10, 8],
  Monk: [10, 15, 14, 8, 14, 8],
  Paladin: [15, 10, 14, 8, 10, 14],
  Ranger: [10, 15, 14, 10, 12, 8],
  Rogue: [8, 15, 14, 10, 10, 12],
  Sorcerer: [8, 14, 14, 10, 10, 15],
  Warlock: [8, 14, 14, 10, 10, 15],
  Wizard: [8, 14, 14, 15, 10, 8],
};
const SCORE_COST = [0, 1, 2, 3, 4, 5, 7, 9];
const DEFAULT_SIZE_ID = 3; // Medium

function CreateCharacter() {
  const navigate = useNavigate();

  /* ---------- state ---------- */
  const [dropdowns, setDropdowns] = useState({
    races: [],
    classes: [],
    alignments: [],
    proficiencies: [],
    ability_scores: [],
  });

  const [selectedClass, setSelectedClass] = useState("");
  const [selectedRace, setSelectedRace] = useState("");
  const [selectedAlignmentId, setSelectedAlignmentId] = useState("");
  const [characterName, setCharacterName] = useState("");

  const [classMap, setClassMap] = useState(null);
  const [selectedClassData, setSelectedClassData] = useState(null);
  const [selectedRaceData, setSelectedRaceData] = useState(null);
  const [selectedAbilityBonusChoices, setSelectedAbilityBonusChoices] =
    useState([]);
  const [fixedAbilityBonuses, setFixedAbilityBonuses] = useState([]);
  const [classLevelData, setClassLevelData] = useState(null);

  const [scores, setScores] = useState([8, 8, 8, 8, 8, 8]);
  const [remainingPoints, setRemainingPoints] = useState(27);

  const [showClassOptions, setShowClassOptions] = useState(false);
  const [showRaceOptions, setShowRaceOptions] = useState(false);

  const [currency, setCurrency] = useState({
    gold: 75,
    silver: 20,
    copper: 75,
  });
  const [personalityTraits, setPersonalityTraits] = useState({
    personality: "",
    ideals: "",
    bonds: "",
    flaws: "",
    notes: "",
  });

  const [loading, setLoading] = useState(false);

  /* ---------- hesaplamalar ---------- */
  const hitPoints = calculateHitPoints(
    selectedClassData?.hit_die || 8,
    scores[2]
  );
  const armorClass = calculateArmorClass(scores[1]);
  const speed = calculateSpeed(selectedRaceData);
  const characterSizeId =
    getCharacterSizeId(selectedRaceData) || DEFAULT_SIZE_ID;

  /* ---------- puan güncelle ---------- */
  const updateScore = (index, delta) => {
    const next = scores[index] + delta;
    if (next < 8 || next > 15) return;

    const costDiff = SCORE_COST[next - 8] - SCORE_COST[scores[index] - 8];
    if (remainingPoints - costDiff < 0) return;

    const newScores = [...scores];
    newScores[index] = next;
    setScores(newScores);
  };

  /* ---------- dropdown verileri (1 kere) ---------- */
  useEffect(() => {
    (async () => {
      try {
        const [races, classes, alignments, profs, abilityScores] =
          await Promise.all([
            api.get("/races"),
            api.get("/classes"),
            api.get("/alignments"),
            api.get("/proficiencies"),
            api.get("/ability-scores"),
          ]);

        setDropdowns({
          races: races.data,
          classes: classes.data,
          alignments: alignments.data,
          proficiencies: profs.data,
          ability_scores: abilityScores.data,
        });

        const map = {};
        classes.data.forEach((c) => (map[c.name.toLowerCase()] = c));
        setClassMap(map);
      } catch (err) {
        console.error("Dropdown verisi alınamadı:", err);
      }
    })();
  }, []);

  /* ---------- sınıf seçimi ---------- */
  useEffect(() => {
    if (selectedClass && CLASS_DEFAULT_STATS[selectedClass]) {
      setScores(CLASS_DEFAULT_STATS[selectedClass]);
      setShowClassOptions(true);
    } else {
      setShowClassOptions(false);
    }
  }, [selectedClass]);

  /* ---------- remaining point ---------- */
  useEffect(() => {
    const total = scores.reduce((acc, v) => acc + SCORE_COST[v - 8], 0);
    setRemainingPoints(27 - total);
  }, [scores]);

  /* ---------- class detayını çek ---------- */
  useEffect(() => {
    if (!selectedClass || !classMap) return;

    const fetchClassDetails = async () => {
      const classId = classMap[selectedClass.toLowerCase()]?.id;
      if (!classId) return;
      try {
        const [levelRes, classRes] = await Promise.all([
          api.get(`/class-levels/${classId}/1`),
          api.get(`/classes/${classId}`),
        ]);
        setClassLevelData(levelRes.data);
        setSelectedClassData(classRes.data);
      } catch (err) {
        console.error("Class detay alınamadı:", err);
      }
    };
    fetchClassDetails();
  }, [selectedClass, classMap]);

  /* ---------- race detayını çek ---------- */
  useEffect(() => {
    if (!selectedRace) return;
    const raceObj = dropdowns.races.find((r) => r.name === selectedRace);
    if (!raceObj) return;

    (async () => {
      try {
        const res = await api.get(`/races/${raceObj.id}`);
        setSelectedRaceData(res.data);
        setShowRaceOptions(true);
      } catch (err) {
        console.error("Race detay alınamadı:", err);
      }
    })();
  }, [selectedRace, dropdowns.races]);

  /* ---------- oluştur ---------- */
  const handleCreate = async () => {
    setLoading(true);
    const payload = {
      name: characterName,
      class_id: selectedClassData?.id,
      race_id: selectedRaceData?.id,
      alignment_id: Number(selectedAlignmentId) || null,
      character_size_id: Number(characterSizeId) || 3,
      ability_scores: {
        strength: scores[0],
        dexterity: scores[1],
        constitution: scores[2],
        intelligence: scores[3],
        wisdom: scores[4],
        charisma: scores[5],
      },
      hit_points: hitPoints,
      armor_class: armorClass,
      speed,
      gold: currency.gold,
      silver: currency.silver,
      copper: currency.copper,
      text_blocks: personalityTraits,
      feat_id: null,
      dungeon_master_id: null,
    };

    try {
      const res = await api.post("/characters", payload);
      navigate(`/characters/${res.data.character_id}`);
    } catch (err) {
      console.error(err.response?.data || err);
      alert(err.response?.data?.error || "Character creation failed");
    } finally {
      setLoading(false);
    }
  };

  /* ---------- render ---------- */
  return (
    <div className="character-form medieval-theme">
      <h2>Create Your Hero</h2>

      {/* NAME */}
      <label>Character Name:</label>
      <input
        type="text"
        value={characterName}
        onChange={(e) => setCharacterName(e.target.value)}
      />

      {/* CLASS */}
      <label>Class:</label>
      <select onChange={(e) => setSelectedClass(e.target.value)}>
        <option value="">Select</option>
        {dropdowns.classes.map((c) => (
          <option key={c.id} value={c.name}>
            {c.name}
          </option>
        ))}
      </select>

      {selectedClass && classMap && (
        <button
          type="button"
          className="class-details-toggle-button"
          onClick={() => setShowClassOptions(!showClassOptions)}
        >
          +
        </button>
      )}

      {selectedClass &&
        showClassOptions &&
        classLevelData &&
        selectedClassData && (
          <div className="detail-box">
            <ClassDetailOptions
              selectedClass={selectedClassData}
              classLevelData={classLevelData}
              proficiencyList={dropdowns.proficiencies}
              abilityScoreList={dropdowns.ability_scores}
            />
          </div>
        )}

      {/* RACE */}
      <label>Race:</label>
      <select onChange={(e) => setSelectedRace(e.target.value)}>
        <option value="">Select</option>
        {dropdowns.races.map((r) => (
          <option key={r.id} value={r.name}>
            {r.name}
          </option>
        ))}
      </select>

      {selectedRace && (
        <button
          type="button"
          className="class-details-toggle-button"
          onClick={() => setShowRaceOptions(!showRaceOptions)}
        >
          +
        </button>
      )}

      {selectedRace && showRaceOptions && selectedRaceData && (
        <div className="detail-box">
          <RaceDetailOptions
            selectedRace={selectedRaceData}
            onAbilityBonusChooseChange={setSelectedAbilityBonusChoices}
            onFixedAbilityBonusesChange={setFixedAbilityBonuses}
          />
        </div>
      )}

      {/* ALIGNMENT */}
      <label>Alignment:</label>
      <select onChange={(e) => setSelectedAlignmentId(e.target.value)}>
        <option value="">Select</option>
        {dropdowns.alignments.map((a) => (
          <option key={a.id} value={a.id}>
            {a.name}
          </option>
        ))}
      </select>

      {/* ABILITY SCORES */}
      <h3>Ability Scores</h3>
      <div className="remaining-points-container">
        Remaining Points: <strong>{remainingPoints}</strong>
      </div>
      {["STR", "DEX", "CON", "INT", "WIS", "CHA"].map((label, idx) => {
        const bonus =
          (fixedAbilityBonuses.find((b) => b.name === label)?.value || 0) +
          selectedAbilityBonusChoices.filter((b) => b === label).length;
        const total = scores[idx] + bonus;
        return (
          <div key={label} className="score-row">
            <label>{label}:</label>
            <button
              disabled={scores[idx] <= 8}
              onClick={() => updateScore(idx, -1)}
            >
              -
            </button>
            <input value={total} readOnly />
            <button
              disabled={
                scores[idx] >= 15 ||
                SCORE_COST[scores[idx] + 1 - 8] > remainingPoints
              }
              onClick={() => updateScore(idx, 1)}
            >
              +
            </button>
            {bonus > 0 && <span className="racial-bonus">+{bonus}</span>}
          </div>
        );
      })}

      {/* CURRENCY */}
      <h3 style={{ textAlign: "center", marginTop: "2rem" }}>CURRENCY</h3>
      <div className="currency-section">
        {["gold", "silver", "copper"].map((type) => (
          <div key={type}>
            <label>{type.charAt(0).toUpperCase() + type.slice(1)}:</label>
            <input
              type="number"
              min={0}
              value={currency[type]}
              onChange={(e) => {
                const v = parseInt(e.target.value);
                if (Number.isInteger(v) && v >= 0)
                  setCurrency((prev) => ({ ...prev, [type]: v }));
              }}
            />
          </div>
        ))}
      </div>

      {/* PERSONALITY */}
      <h3 style={{ textAlign: "center", marginTop: "2rem" }}>
        PERSONALITY TRAITS
      </h3>
      <div className="personality-section">
        {Object.keys(personalityTraits).map((key) => (
          <div key={key}>
            <label>{key.charAt(0).toUpperCase() + key.slice(1)}:</label>
            <textarea
              value={personalityTraits[key]}
              onChange={(e) =>
                setPersonalityTraits((prev) => ({
                  ...prev,
                  [key]: e.target.value,
                }))
              }
            />
          </div>
        ))}
      </div>

      {/* SUBMIT */}
      <div style={{ textAlign: "center", marginTop: "2rem" }}>
        <button
          className="submit-button"
          onClick={handleCreate}
          disabled={
            loading ||
            !characterName ||
            !selectedClassData ||
            !selectedRaceData ||
            !selectedAlignmentId
          }
        >
          {loading ? "Creating..." : "Create Character"}
        </button>
      </div>
    </div>
  );
}

export default CreateCharacter;
