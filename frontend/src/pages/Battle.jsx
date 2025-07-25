import React, { useState } from "react";
import DiceRoller from '../components/DiceRoller';

import bg1 from "../assets/images/battle_comps/bgDesign/bg1.png";
import bg2 from "../assets/images/battle_comps/bgDesign/bg2.png";
import bg3 from "../assets/images/battle_comps/bgDesign/bg3.png";
import bg4 from "../assets/images/battle_comps/bgDesign/bg4.png";
import bg5 from "../assets/images/battle_comps/bgDesign/bg5.png";
import orb1 from "../assets/images/battle_comps/bgDesign/itsmars_orb_fill1.png";
import orb1s from "../assets/images/battle_comps/bgDesign/itsmars_orb_fill1s.png";
import orb2 from "../assets/images/battle_comps/bgDesign/itsmars_orb_fill2.png";
import orb2s from "../assets/images/battle_comps/bgDesign/itsmars_orb_fill2s.png";
import orb3 from "../assets/images/battle_comps/bgDesign/itsmars_orb_fill3.png";
import orb3s from "../assets/images/battle_comps/bgDesign/itsmars_orb_fill3s.png";
import orb4 from "../assets/images/battle_comps/bgDesign/itsmars_orb_fill4.png";
import orb4s from "../assets/images/battle_comps/bgDesign/itsmars_orb_fill4s.png";
import orb5 from "../assets/images/battle_comps/bgDesign/itsmars_orb_fill5.png";
import orb5s from "../assets/images/battle_comps/bgDesign/itsmars_orb_fill5s.png";

import hpOrb from "../assets/images/battle_comps/battleSim/hpOrb.png";
import hpSetOrb from "../assets/images/battle_comps/battleSim/hpSetOrb.png";
import rightOrb from "../assets/images/battle_comps/battleSim/rightOrb.png";
import slots from "../assets/images/battle_comps/battleSim/slots.png";

const orbPaths = [orb1, orb2, orb3, orb4, orb5];
const orbActivePaths = [orb1s, orb2s, orb3s, orb4s, orb5s];
const bgPaths = [bg1, bg2, bg3, bg4, bg5];

export default function Battle() {
  const [selectedBg, setSelectedBg] = useState(0);
  const [hp, setHp] = useState(100);
  const maxHp = 100;
  const [showHpModal, setShowHpModal] = useState(false);
  const [modalHp, setModalHp] = useState(hp);

  const bgUrl = bgPaths[selectedBg];
  const hpPercent = Math.max(0, Math.min(1, hp / maxHp));

  // Modal açıldığında mevcut hp'yi göster
  const openHpModal = () => {
    setModalHp(hp);
    setShowHpModal(true);
  };

  // Modal kapat
  const closeHpModal = () => setShowHpModal(false);

  // Modalda onayla
  const confirmHpModal = () => {
    setHp(Math.max(0, Math.min(maxHp, modalHp)));
    setShowHpModal(false);
  };

  return (
    <div
      style={{
        width: '100%',
        minHeight: '100vh',
        position: 'relative',
        background: `url(${bgUrl}) center/cover no-repeat`,
        overflow: 'hidden'
      }}
    >
      {/* Arka plan seçme butonları */}
      <div
        style={{
          position: 'absolute',
          top: 24,
          right: 32,
          display: 'flex',
          gap: 12,
          zIndex: 10
        }}
      >
        {orbPaths.map((orb, i) => (
          <button
            key={i}
            onClick={() => setSelectedBg(i)}
            style={{
              width: 32,
              height: 32,
              padding: 0,
              border: 'none',
              background: 'none',
              opacity: selectedBg === i ? 1 : 0.3,
              cursor: 'pointer',
              transition: 'opacity 0.2s'
            }}
          >
            <img
              src={selectedBg === i ? orbActivePaths[i] : orbPaths[i]}
              alt={`bg orb ${i + 1}`}
              style={{ width: 32, height: 32, display: 'block' }}
            />
          </button>
        ))}
      </div>

      {/* Savaş menüsü en altta ortalanmış, birleşik tek parça */}
      <div
        style={{
          position: 'absolute',
          left: 0,
          right: 0,
          bottom: 0,
          width: '100%',
          display: 'flex',
          alignItems: 'flex-end',
          justifyContent: 'center',
          paddingBottom: 32,
          zIndex: 5,
          gap: 0
        }}
      >
        {/* Sol HP orb */}
        <div
          style={{
            position: 'relative',
            width: 312,
            height: 309,
            cursor: 'pointer',
            marginRight: 0
          }}
          onClick={openHpModal}
        >
          {/* Bordo overlay en altta */}
          <div
            style={{
              position: 'absolute',
              left: 0,
              bottom: 0,
              width: '100%',
              height: `${hpPercent * 100}%`,
              background: 'rgba(110, 20, 35, 0.85)', // daha opak ve bordo
              borderRadius: '50%',
              zIndex: 1, // EN ALTA ALINDI
              transition: 'height 0.3s'
            }}
          />
          {/* Orb PNG üstte */}
          <img
            src={hpOrb}
            alt="HP Orb"
            style={{
              width: '100%',
              height: '100%',
              position: 'absolute',
              left: 0,
              top: 0,
              zIndex: 2
            }}
          />
          {/* HP yazısı en üstte */}
          <div
            style={{
              position: 'absolute',
              left: 0,
              top: 0,
              width: '100%',
              height: '100%',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: '#CCBDA4',
              fontSize: 64,
              fontFamily: 'Quintessential',
              fontWeight: 400,
              zIndex: 3,
              pointerEvents: 'none'
            }}
          >
            {hp}/{maxHp}
          </div>
        </div>

        {/* Ortadaki slotlar */}
        <img
          src={slots}
          alt="Slots"
          style={{
            width: 816,
            height: 173,
            alignSelf: 'flex-end',
            margin: '0' // boşluk kaldırıldı
          }}
        />

        {/* Sağ End Turn orb */}
        <button
          style={{
            position: 'relative',
            width: 308,
            height: 309,
            marginLeft: 0, // boşluk kaldırıldı
            background: 'none',
            border: 'none',
            padding: 0,
            cursor: 'pointer'
          }}
        >
          <img src={rightOrb} alt="End Turn Orb" style={{ width: '100%', height: '100%' }} />
          <div
            style={{
              position: 'absolute',
              left: 0,
              top: 0,
              width: '100%',
              height: '100%',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center',
              color: '#CCBDA4',
              fontSize: 48,
              fontFamily: 'Quintessential',
              fontWeight: 400,
              textAlign: 'center',
              zIndex: 2,
              pointerEvents: 'none'
            }}
          >
            END<br />TURN
          </div>
        </button>
      </div>

      {/* Zar atma paneli */}
      <div style={{ position: 'absolute', left: 0, right: 0, bottom: 340, zIndex: 6 }}>
        <DiceRoller />
      </div>

      {/* HP Ayarlama Popup */}
      {showHpModal && (
        <div
          style={{
            position: 'fixed',
            left: 0,
            top: 0,
            width: '100vw',
            height: '100vh',
            background: 'rgba(0,0,0,0.5)',
            zIndex: 100,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center'
          }}
          onClick={closeHpModal}
        >
          <div
            style={{
              background: 'linear-gradient(180deg, #e7d9c7 0%, #b6a89a 100%)',
              borderRadius: 32,
              padding: 32,
              minWidth: 320,
              boxShadow: '0 4px 32px rgba(0,0,0,0.3)',
              position: 'relative',
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center'
            }}
            onClick={e => e.stopPropagation()}
          >
            <div
              style={{
                color: '#5A3333',
                fontSize: 48,
                fontFamily: 'Quintessential',
                marginBottom: 24
              }}
            >
              Can Ayarla
            </div>
            <div style={{ display: 'flex', alignItems: 'center', gap: 16 }}>
              <button
                style={{
                  width: 48,
                  height: 48,
                  fontSize: 32,
                  background: '#FFE6B7',
                  border: 'none',
                  borderRadius: 12,
                  cursor: 'pointer'
                }}
                onClick={() => setModalHp(Math.max(0, modalHp - 5))}
              >-</button>
              <input
                type="number"
                min={0}
                max={maxHp}
                value={modalHp}
                onChange={e => setModalHp(Math.max(0, Math.min(maxHp, Number(e.target.value))))}
                style={{
                  width: 80,
                  fontSize: 32,
                  textAlign: 'center',
                  border: '1px solid #b6a89a',
                  borderRadius: 8,
                  background: '#fff',
                  color: '#5A3333'
                }}
              />
              <button
                style={{
                  width: 48,
                  height: 48,
                  fontSize: 32,
                  background: '#FFE6B7',
                  border: 'none',
                  borderRadius: 12,
                  cursor: 'pointer'
                }}
                onClick={() => setModalHp(Math.min(maxHp, modalHp + 5))}
              >+</button>
            </div>
            <button
              style={{
                marginTop: 32,
                padding: '12px 32px',
                fontSize: 24,
                background: '#5A3333',
                color: '#fff',
                border: 'none',
                borderRadius: 16,
                cursor: 'pointer'
              }}
              onClick={confirmHpModal}
            >
              Onayla
            </button>
          </div>
        </div>
      )}
    </div>
  );
}