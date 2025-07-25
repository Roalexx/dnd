from flask import Blueprint, jsonify
from flasgger import swag_from
from config import SessionLocal as db
from models.player.character import Character
from models.player.character_spell import CharacterSpell
from models.models import Spells

char_info_bp = Blueprint("char_info_for_battle", __name__, url_prefix="/api/char-info")

@char_info_bp.route('/<int:character_id>', methods=['GET'])
@swag_from({
    'tags': ['Battle Info'],
    'summary': 'Get character info for battle',
    'parameters': [
        {
            'name': 'character_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the character'
        }
    ],
    'responses': {
        200: {
            'description': 'Character battle info',
            'examples': {
                'application/json': {
                    'hit_points': 27,
                    'spell_slots': { '1': 4, '2': 2 },
                    'cantrips': [ {'id': 1, 'name': 'Fire Bolt'}, {'id': 2, 'name': 'Mage Hand'} ],
                    'known_spells': [ {'id': 3, 'name': 'Magic Missile'}, {'id': 4, 'name': 'Shield'} ]
                }
            }
        }
    }
})
def get_char_info_for_battle(character_id):
    session = db()
    char = session.query(Character).filter(Character.id == character_id).first()
    if not char:
        return jsonify({'error': 'Character not found'}), 404

    # Can (hit_points)
    hit_points = char.hit_points

    # Spell slotları (örnek: slot sayıları karakterden veya başka bir tablodan alınabilir)
    # Burada örnek olarak level'a göre slot sayısı verildi, kendi slot tablon varsa oradan çek
    spell_slots = {}  # slot_level: slot_count
    # Örnek: char.spell_slots gibi bir alan varsa onu kullanabilirsin

    # Cantrips ve bilinen büyüler
    spells_query = (
        session.query(Spells.id, Spells.name, Spells.level)
        .join(CharacterSpell, Spells.id == CharacterSpell.spell_id)
        .filter(CharacterSpell.character_id == character_id)
        .all()
    )
    cantrips = [{'id': s.id, 'name': s.name} for s in spells_query if s.level == 0]
    known_spells = [{'id': s.id, 'name': s.name, 'level': s.level} for s in spells_query if s.level > 0]

    # Sahip olunan spell slotları (örnek, slot tablon varsa oradan çek)
    # spell_slots = { '1': 4, '2': 2 } gibi doldurulmalı

    return jsonify({
        'hit_points': hit_points,
        'spell_slots': spell_slots,
        'cantrips': cantrips,
        'known_spells': known_spells
    })