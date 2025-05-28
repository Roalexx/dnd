import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import CharacterForm from '../components/CharacterForm';
import api from '../api/axios'; 

const CharacterDetailPage = () => {
  const { id: characterId } = useParams();  
  const [character, setCharacter] = useState(null);
  const [dropdownOptions, setDropdownOptions] = useState({});

  useEffect(() => {
    const fetchCharacter = async () => {
      try {
        const [
          charRes,
          spellsRes,
          equipmentRes,
          skillsRes,
          languagesRes,
          traitsRes,
          conditionsRes
        ] = await Promise.all([
          api.get(`/characters/${characterId}`),
          api.get(`/characters/${characterId}/spells`),
          api.get(`/characters/${characterId}/equipment`),
          api.get(`/characters/${characterId}/skills`),
          api.get(`/characters/${characterId}/languages`),
          api.get(`/characters/${characterId}/traits`),
          api.get(`/characters/${characterId}/conditions`)
        ]);

        setCharacter({
          ...charRes.data,
          spells: spellsRes.data,
          equipment: equipmentRes.data,
          skills: skillsRes.data,
          languages: languagesRes.data,
          traits: traitsRes.data,
          conditions: conditionsRes.data
        });
      } catch (err) {
        console.error("Character fetch error:", err);
      }
    };

    const fetchDropdowns = async () => {
      try {
        const [races, classes, alignments, sizes] = await Promise.all([
          api.get('/races'),
          api.get('/classes'),
          api.get('/alignments'),
          api.get('/character-sizes')
        ]);
        setDropdownOptions({
          races: races.data,
          classes: classes.data,
          alignments: alignments.data,
          sizes: sizes.data
        });
      } catch (err) {
        console.error("Dropdown fetch error:", err);
      }
    };

    fetchCharacter();
    fetchDropdowns();
  }, [characterId]);

  if (!character) return <p>Yükleniyor...</p>;

  return (
    <div>
      <label htmlFor=""></label>
      <CharacterForm character={character} readOnly={true} dropdownOptions={dropdownOptions} />
    </div>
  );
};

export default CharacterDetailPage;
