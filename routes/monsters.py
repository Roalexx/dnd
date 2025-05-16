from flask import Blueprint, jsonify
from sqlalchemy.orm import selectinload
from models.models import (
    Monsters, MonsterActions, MonsterConditionImmunities,
    MonsterLegendaryActions, MonsterReactions, MonstersSpecialAbilities,
    MonsterProficiencies, MonsterSpells
)
from config import SessionLocal

monsters_bp = Blueprint("monsters", __name__)

@monsters_bp.route("/monsters/<int:monster_id>", methods=["GET"])
def get_monster_by_id(monster_id):
    session = SessionLocal()
    monster = session.query(Monsters).options(
        selectinload(Monsters.monster_actions),
        selectinload(Monsters.monster_condition_immunities),
        selectinload(Monsters.monster_legendary_actions),
        selectinload(Monsters.monster_reactions),
        selectinload(Monsters.monsters_special_abilities).selectinload(MonstersSpecialAbilities.monster_spells),
        selectinload(Monsters.monster_proficiencies),
    ).filter(Monsters.id == monster_id).first()

    if not monster:
        return jsonify({"error": "Monster not found"}), 404

    return jsonify({
        "id": monster.id,
        "name": monster.name,
        "hit_points": monster.hit_points,
        "challenge_rating": monster.challenge_rating,
        "speed": monster.speed,
        "monster_actions": [a.name for a in monster.monster_actions],
        "monster_reactions": [r.name for r in monster.monster_reactions],
        "monster_legendary_actions": [l.name for l in monster.monster_legendary_actions],
        "monster_proficiencies": [p.proficiency.name for p in monster.monster_proficiencies if p.proficiency],
        "monster_condition_immunities": [c.condition.name for c in monster.monster_condition_immunities if c.condition],
        "monsters_special_abilities": [
            {
                "name": s.name,
                "description": s.description,
                "spells": [sp.spell.name for sp in s.monster_spells if sp.spell]
            } for s in monster.monsters_special_abilities
        ]
    })
