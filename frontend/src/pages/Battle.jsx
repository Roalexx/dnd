import React, { useState } from "react";

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

const orbPaths = [orb1, orb2, orb3, orb4, orb5];
const orbActivePaths = [orb1s, orb2s, orb3s, orb4s, orb5s];
const bgPaths = [bg1, bg2, bg3, bg4, bg5];

export default function Battle() {
  const [selectedBg, setSelectedBg] = useState(0);

  const bgUrl = bgPaths[selectedBg];

  return (
    <div
      style={{
        width: '100%',
        minHeight: 'calc(100vh - 48px)',
        background: `url(${bgUrl}) center/cover no-repeat`,
        paddingTop: '48px',
        position: 'relative',
        overflowX: 'hidden'
      }}
    >
      <div
        style={{
          position: 'absolute',
          top: 16,
          right: 16,
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
    </div>
  );
}