// CharacterForm.jsx
import React from "react";
import "./CharacterForm.css";

function CharacterForm({ character, readOnly = false, dropdownOptions = {} }) {
  const formData = character || {};

  return (
    <form style={{ maxWidth: "600px", margin: "0 auto" }}>
      <h2>Character Details</h2>

      {/* Basic Info */}
      <label>Character Name:</label>
      <input
        type="text"
        value={formData.name || ""}
        readOnly
      /><br />

      <label>Race:</label>
      <select value={formData.race_id || ""} disabled>
        <option value="">Select</option>
        {dropdownOptions.races?.map((r) => (
          <option key={r.id} value={r.id}>{r.name}</option>
        ))}
      </select><br />

      <label>Class:</label>
      <select value={formData.class_id || ""} disabled>
        <option value="">Select</option>
        {dropdownOptions.classes?.map((c) => (
          <option key={c.id} value={c.id}>{c.name}</option>
        ))}
      </select><br />

      <label>Alignment:</label>
      <select value={formData.alignment_id || ""} disabled>
        <option value="">Select</option>
        {dropdownOptions.alignments?.map((a) => (
          <option key={a.id} value={a.id}>{a.name}</option>
        ))}
      </select><br />

      <label>Size:</label>
      <select value={formData.character_size_id || ""} disabled>
        <option value="">Select</option>
        {dropdownOptions.sizes?.map((s) => (
          <option key={s.id} value={s.id}>{s.name}</option>
        ))}
      </select><br />

      {/* Ability Scores */}
      <h3>Ability Scores</h3>
      <label>Strength:</label>
      <input value={` ${formData.ability_scores?.strength || 0}`} readOnly /><br />
      <label>Dexterity:</label>
      <input value={` ${formData.ability_scores?.dexterity || 0}`} readOnly /><br />
      <label>Constitution:</label>
      <input value={` ${formData.ability_scores?.constitution || 0}`} readOnly /><br />
      <label>Intelligence:</label>
      <input value={` ${formData.ability_scores?.intelligence || 0}`} readOnly /><br />
      <label>Wisdom:</label>
      <input value={` ${formData.ability_scores?.wisdom || 0}`} readOnly /><br />
      <label>Charisma:</label>
      <input value={` ${formData.ability_scores?.charisma || 0}`} readOnly /><br />

      {/* Currency */}
      <h3>Currency</h3>
      <label>Gold:</label>
      <input value={` ${formData.currency?.gold || 0}`} readOnly /><br />
      <label>Silver:</label>
      <input value={` ${formData.currency?.silver || 0}`} readOnly /><br />
      <label>Copper:</label>
      <input value={` ${formData.currency?.copper || 0}`} readOnly /><br />

      {/* Text Blocks */}
      <h3>Personality Traits</h3>
      <label>Personality:</label>
      <textarea value={formData.text_blocks?.personality || ""} readOnly /><br />

      <label>Ideals:</label>
      <textarea value={formData.text_blocks?.ideals || ""} readOnly /><br />

      <label>Bonds:</label>
      <textarea value={formData.text_blocks?.bonds || ""} readOnly /><br />

      <label>Flaws:</label>
      <textarea value={formData.text_blocks?.flaws || ""} readOnly /><br />

      <label>Notes:</label>
      <textarea value={formData.text_blocks?.notes || ""} readOnly /><br />

      {/* Equipment */}
      <h3>Equipment</h3>
      <ul>
        {formData.equipment?.map((item, i) => (
          <li key={i}>{item.name} x{item.quantity}</li>
        ))}
      </ul>

      {/* Languages */}
      <h3>Languages</h3>
      <ul>
        {formData.languages?.map((lang, i) => (
          <li key={i}>{lang.name}</li>
        ))}
      </ul>
    </form>
  );
}

export default CharacterForm;
