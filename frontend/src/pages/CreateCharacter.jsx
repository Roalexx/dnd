import React, { useEffect, useState } from "react";
import api from "../api/axios";
import ClassDetailOptions from "../components/ClassDetailOptions";
import "../components/CharacterForm.css";

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

function CreateCharacter() {
  const [dropdowns, setDropdowns] = useState({
    races: [],
    classes: [],
    alignments: [],
    sizes: [],
    proficiencies: [],
    ability_scores: [],
  });

  const [selectedClass, setSelectedClass] = useState("");
  const [classMap, setClassMap] = useState(null);
  const [selectedClassData, setSelectedClassData] = useState(null);
  const [classLevelData, setClassLevelData] = useState(null);
  const [scores, setScores] = useState([8, 8, 8, 8, 8, 8]);
  const [remainingPoints, setRemainingPoints] = useState(27);
  const [showClassOptions, setShowClassOptions] = useState(false);

  useEffect(() => {
    const fetchDropdowns = async () => {
      const token = localStorage.getItem("token");
      const config = { headers: { Authorization: `Bearer ${token}` } };
      const [races, classes, alignments, sizes, proficiencies, abilityScores] =
        await Promise.all([
          api.get("/races", config),
          api.get("/classes", config),
          api.get("/alignments", config),
          api.get("/character-sizes", config),
          api.get("/proficiencies", config),
          api.get("/ability-scores", config),
        ]);

      setDropdowns({
        races: races.data,
        classes: classes.data,
        alignments: alignments.data,
        sizes: sizes.data,
        proficiencies: proficiencies.data,
        ability_scores: abilityScores.data,
      });

      const classMapTemp = {};
      classes.data.forEach((c) => (classMapTemp[c.name.toLowerCase()] = c));
      setClassMap(classMapTemp);
    };

    fetchDropdowns();
  }, []);

  useEffect(() => {
    if (selectedClass && CLASS_DEFAULT_STATS[selectedClass]) {
      setScores(CLASS_DEFAULT_STATS[selectedClass]);
      setShowClassOptions(true);
    } else {
      setShowClassOptions(false);
    }
  }, [selectedClass]);

  useEffect(() => {
    const total = scores.reduce(
      (acc, val) => acc + (val > 15 ? 999 : SCORE_COST[val - 8]),
      0
    );
    setRemainingPoints(27 - total);
  }, [scores]);

  useEffect(() => {
    const fetchClassDetails = async () => {
      if (!selectedClass || !classMap) return;
      const token = localStorage.getItem("token");
      const config = { headers: { Authorization: `Bearer ${token}` } };
      const normalizedClass = Object.keys(classMap).find(
        (key) => key.toLowerCase() === selectedClass.toLowerCase()
      );
      const classId = classMap[normalizedClass]?.id;
      if (!classId) return;

      try {
        const [levelRes, classRes] = await Promise.all([
          api.get(`/class-levels/${classId}/1`, config),
          api.get(`/classes/${classId}`, config),
        ]);
        setClassLevelData(levelRes.data);
        setSelectedClassData(classRes.data);
      } catch (error) {
        console.error("Class verileri alınamadı:", error);
      }
    };

    fetchClassDetails();
  }, [selectedClass, classMap]);

  const updateScore = (index, delta) => {
    const newScore = scores[index] + delta;
    if (newScore < 8 || newScore > 15) return;
    const tempScores = [...scores];
    const newTotal = scores.reduce(
      (sum, val, i) =>
        i === index
          ? sum + SCORE_COST[newScore - 8]
          : sum + SCORE_COST[val - 8],
      0
    );
    if (newTotal > 27) return;
    tempScores[index] = newScore;
    setScores(tempScores);
  };

  const labels = ["STR", "DEX", "CON", "INT", "WIS", "CHA"];

  return (
    <div className="character-form medieval-theme">
      <h2>Create Your Hero</h2>

      <label>Character Name:</label>
      <input type="text" placeholder="Enter name..." />

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

      <label>Race:</label>
      <select>
        <option value="">Select</option>
        {dropdowns.races.map((r) => (
          <option key={r.id} value={r.id}>
            {r.name}
          </option>
        ))}
      </select>

      <label>Alignment:</label>
      <select>
        <option value="">Select</option>
        {dropdowns.alignments.map((a) => (
          <option key={a.id} value={a.id}>
            {a.name}
          </option>
        ))}
      </select>

      <label>Size:</label>
      <select>
        <option value="">Select</option>
        {dropdowns.sizes.map((s) => (
          <option key={s.id} value={s.id}>
            {s.name}
          </option>
        ))}
      </select>

      <h3>Ability Scores</h3>
      <div className="remaining-points-container">
        <p>
          Remaining Points: <strong>{remainingPoints}</strong>
          <span className="tooltip-trigger">
            ❓
            <span className="tooltip-text">
              Each ability starts at 8. You have 27 points to spend. <br />
              Score costs: <br />9 → 1pt, 10 → 2pt, 11 → 3pt, 12 → 4pt, 13 →
              5pt, 14 → 7pt, 15 → 9pt.
            </span>
          </span>
        </p>
      </div>

      {scores.map((score, idx) => (
        <div key={labels[idx]} className="score-row">
          <label>{labels[idx]}:</label>
          <button disabled={score <= 8} onClick={() => updateScore(idx, -1)}>
            -
          </button>
          <input value={score} readOnly />
          <button
            disabled={
              score >= 15 || SCORE_COST[score + 1 - 8] > remainingPoints
            }
            onClick={() => updateScore(idx, 1)}
          >
            +
          </button>
        </div>
      ))}
    </div>
  );
}

export default CreateCharacter;
