import React from 'react';

function CharacterForm({ character, readOnly = false }) {
  return (
    <form>
      <label>İsim:</label>
      <input type="text" value={character.name} readOnly={readOnly} /><br />

      <label>Seviye:</label>
      <input type="number" value={character.level} readOnly={readOnly} /><br />

      <label>Sınıf:</label>
      <input type="text" value={character.class_id} readOnly={readOnly} /><br />

      <label>Irk:</label>
      <input type="text" value={character.race_id} readOnly={readOnly} /><br />

      <label>HP:</label>
      <input type="number" value={character.hit_points} readOnly={readOnly} /><br />

      {/* Diğer alanlar da sırayla eklenebilir */}
    </form>
  );
}

export default CharacterForm;
