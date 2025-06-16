export function calculateHitPoints(hitDie, conScore, level = 1) {
  const conMod = Math.floor((conScore - 10) / 2);
  const avgPerLevel = Math.floor(hitDie / 2) + 1;
  return hitDie + (level - 1) * (avgPerLevel + conMod);
}

export function calculateArmorClass(dexScore) {
  const dexMod = Math.floor((dexScore - 10) / 2);
  return 10 + dexMod; // default base armor
}

export function calculateSpeed(raceData) {
  return raceData?.speed || 30;
}

export function getCharacterSizeId(raceData) {
  return raceData?.size?.id || null;
}
