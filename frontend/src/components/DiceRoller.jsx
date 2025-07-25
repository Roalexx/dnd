import React, { useState } from 'react';

function DiceRoller() {
  const DICE_TYPES = [
    { label: 'D4', sides: 4 },
    { label: 'D6', sides: 6 },
    { label: 'D8', sides: 8 },
    { label: 'D10', sides: 10 },
    { label: 'D12', sides: 12 },
    { label: 'D20', sides: 20 },
    { label: 'D100', sides: 100 },
  ];

  const [diceList, setDiceList] = useState([]); // {sides: number, id: string}
  const [results, setResults] = useState([]);
  const [rolling, setRolling] = useState(false);

  const addDice = (sides) => {
    setDiceList([...diceList, { sides, id: Math.random().toString(36).substr(2, 9) }]);
  };

  const removeDice = (id) => {
    setDiceList(diceList.filter(d => d.id !== id));
  };

  const rollAllDice = () => {
    setRolling(true);
    setResults([]);
    setTimeout(() => {
      const newResults = diceList.map(d => ({
        sides: d.sides,
        value: Math.floor(Math.random() * d.sides) + 1,
        id: d.id
      }));
      setResults(newResults);
      setRolling(false);
    }, 900);
  };

  return (
  <div style={{
    textAlign: 'center',
    marginTop: '2rem',
    background: 'radial-gradient(circle at 50% 30%, #e2c08d 0%, #a67c52 100%)',
    fontFamily: 'MedievalSharp, serif',
    color: '#3e2c0b',
    border: '8px solid #7c5c2b',
    borderRadius: '18px',
    boxShadow: '0 0 40px #7c5c2b88',
    maxWidth: '480px',
    marginLeft: 'auto',
    marginRight: 'auto',
    padding: results.length > 0 && !rolling ? '2rem 2rem 1rem 2rem' : '2rem',
    minHeight: rolling ? '480px' : (results.length > 0 ? 'unset' : '100vh'),
    transition: 'min-height 0.3s, padding-bottom 0.3s',
  }}>
    <h2 style={{
      fontFamily: 'MedievalSharp, serif',
      fontSize: '2.2rem',
      letterSpacing: '2px',
      textShadow: '2px 2px 8px #a67c52',
      marginBottom: '1.5rem',
      color: '#3e2c0b',
    }}>DND Dice Roller</h2>
    <div style={{ display: 'flex', justifyContent: 'center', gap: '0.7rem', flexWrap: 'wrap', marginBottom: '1.2rem' }}>
      {DICE_TYPES.map(dice => (
        <button
          key={dice.sides}
          onClick={() => addDice(dice.sides)}
          style={{
            fontFamily: 'MedievalSharp, serif',
            fontSize: '1.1rem',
            padding: '0.4rem 1.1rem',
            background: 'linear-gradient(90deg, #a67c52 0%, #e2c08d 100%)',
            color: '#3e2c0b',
            border: '2px solid #7c5c2b',
            borderRadius: '10px',
            fontWeight: 'bold',
            boxShadow: '0 0 8px #7c5c2b88',
            cursor: 'pointer',
            marginBottom: '0.2rem',
            marginTop: '0.2rem',
            minWidth: '60px',
          }}
          disabled={rolling}
        >
          {dice.label}
        </button>
      ))}
    </div>
    <div style={{ marginBottom: '1.2rem' }}>
      {diceList.length === 0 && <div style={{ fontSize: '1.1rem', color: '#7c5c2b' }}>Zar eklemek için yukarıdan bir zar tipi seçin.</div>}
      {diceList.length > 0 && (
        <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'center', gap: '0.7rem' }}>
          {diceList.map((dice, idx) => (
            <div key={dice.id} style={{ position: 'relative', display: 'inline-block', marginBottom: '0.5rem' }}>
              <svg width="90" height="90" viewBox="0 0 120 120" style={{ transition: 'transform 0.8s', transform: rolling ? 'rotate(720deg)' : 'none', filter: 'drop-shadow(0 0 12px #7c5c2b)' }}>
                <polygon points="60,10 110,35 110,85 60,110 10,85 10,35" fill="#f7e7c1" stroke="#7c5c2b" strokeWidth="5" />
                <text x="60" y="45" textAnchor="middle" fontSize="22" fill="#3e2c0b" fontFamily="MedievalSharp, serif" style={{textShadow:'2px 2px 8px #a67c52'}}>
                  D{dice.sides}
                </text>
                <text
                  x="60"
                  y="80"
                  textAnchor="middle"
                  fontSize="32"
                  fill={(() => {
                    const val = results.find(r => r.id === dice.id)?.value;
                    if (val === dice.sides) return '#e2c08d'; // max
                    if (val === 1) return '#c0392b'; // min
                    return '#7c5c2b';
                  })()}
                  fontFamily="MedievalSharp, serif"
                  style={{
                    textShadow: '2px 2px 8px #e2c08d',
                    animation: (() => {
                      const val = results.find(r => r.id === dice.id)?.value;
                      if (val === dice.sides) return 'flashmax 1.2s linear infinite';
                      if (val === 1) return 'flashmin 1.2s linear infinite';
                      return 'none';
                    })(),
                  }}
                >
                  {rolling ? '?' : (results.find(r => r.id === dice.id)?.value || '')}
                </text>
              </svg>
              <button
                onClick={() => removeDice(dice.id)}
                style={{
                  position: 'absolute',
                  top: '-8px',
                  right: '-8px',
                  background: '#a67c52',
                  color: '#fff',
                  border: 'none',
                  borderRadius: '50%',
                  width: '22px',
                  height: '22px',
                  fontWeight: 'bold',
                  fontSize: '1rem',
                  cursor: 'pointer',
                  boxShadow: '0 0 4px #7c5c2b88',
                }}
                disabled={rolling}
              >
                ×
              </button>
            </div>
          ))}
        </div>
      )}
    </div>
    <button
      onClick={rollAllDice}
      style={{
        marginTop: '0.7rem',
        fontSize: '1.3rem',
        padding: '0.7rem 2.2rem',
        background: 'linear-gradient(90deg, #a67c52 0%, #e2c08d 100%)',
        color: '#3e2c0b',
        border: '3px solid #7c5c2b',
        borderRadius: '12px',
        fontFamily: 'MedievalSharp, serif',
        fontWeight: 'bold',
        boxShadow: '0 0 12px #7c5c2b88',
        cursor: rolling || diceList.length === 0 ? 'not-allowed' : 'pointer',
        transition: 'all 0.2s',
        opacity: rolling || diceList.length === 0 ? 0.7 : 1,
      }}
      disabled={rolling || diceList.length === 0}
    >
      {rolling ? 'Zarlar Atılıyor...' : 'Zarları At'}
    </button>
    {results.length > 0 && !rolling && (
      <div style={{ marginTop: '1.2rem', fontSize: '1.2rem', color: '#7c5c2b', fontFamily: 'MedievalSharp, serif', fontWeight: 'bold' }}>
        <div style={{ marginBottom: '0.5rem', fontSize: '1.3rem' }}>Sonuçlar:</div>
        <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'center', gap: '0.7rem' }}>
          {results.map((res, idx) => (
            <div key={res.id} style={{ background: '#f7e7c1', border: '2px solid #a67c52', borderRadius: '10px', padding: '0.5rem 1.2rem', minWidth: '60px', boxShadow: '0 0 8px #7c5c2b44', marginBottom: '0.5rem' }}>
              <span style={{ color: '#3e2c0b', fontSize: '1.1rem' }}>D{res.sides}: </span>
              <span style={{ color: '#7c5c2b', fontSize: '1.3rem' }}>{res.value}</span>
            </div>
          ))}
        </div>
      </div>
    )}
    <style>{`
      @import url('https://fonts.googleapis.com/css2?family=MedievalSharp&display=swap');
      @keyframes flashmax {
        0% { opacity: 1; filter: drop-shadow(0 0 12px #fff); }
        50% { opacity: 0.3; filter: drop-shadow(0 0 32px #fff); }
        100% { opacity: 1; filter: drop-shadow(0 0 12px #fff); }
      }
      @keyframes flashmin {
        0% { opacity: 1; filter: drop-shadow(0 0 12px #c0392b); }
        50% { opacity: 0.3; filter: drop-shadow(0 0 32px #c0392b); }
        100% { opacity: 1; filter: drop-shadow(0 0 12px #c0392b); }
      }
    `}</style>
  </div>
  );
}

export default DiceRoller;