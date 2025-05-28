from flask import Blueprint, jsonify
from flasgger import swag_from
from config import SessionLocal as db
from models.player.character_details import CharacterLanguage
from models.player.character_details import CharacterSkill
from models.player.character_equipment import CharacterEquipment
from models.player.character_spell import CharacterSpell
from models.player.character_details import CharacterTrait
from models.player.character_details import CharacterCondition
from models.models import Languages
from models.models import Skills
from models.models import Equipment
from models.models import Spells
from models.models import Traits
from models.models import Conditions

character_data_bp = Blueprint("character_data", __name__, url_prefix="/api/characters")

@character_data_bp.route('/<int:character_id>/languages', methods=['GET'])
@swag_from({
    'tags': ['Character Details'],
    'summary': 'Get character languages',
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
            'description': 'List of known languages for the character',
            'examples': {
                'application/json': [
                    {'id': 1, 'name': 'Common'},
                    {'id': 2, 'name': 'Elvish'}
                ]
            }
        }
    }
})
def get_character_languages(character_id):
    session = db()
    results = (
        session.query(Languages.id, Languages.name)
        .join(CharacterLanguage, Languages.id == CharacterLanguage.language_id)
        .filter(CharacterLanguage.character_id == character_id)
        .all()
    )
    return jsonify([{'id': r.id, 'name': r.name} for r in results])


@character_data_bp.route('/<int:character_id>/skills', methods=['GET'])
@swag_from({
    'tags': ['Character Details'],
    'summary': 'Get character skills',
    'parameters': [
        {'name': 'character_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {
            'description': 'List of character skills',
            'examples': {
                'application/json': [
                    {'id': 3, 'name': 'Stealth'},
                    {'id': 5, 'name': 'Investigation'}
                ]
            }
        }
    }
})
def get_character_skills(character_id):
    session = db()
    results = (
        session.query(Skills.id, Skills.name)
        .join(CharacterSkill, Skills.id == CharacterSkill.skill_id)
        .filter(CharacterSkill.character_id == character_id)
        .all()
    )
    return jsonify([{'id': r.id, 'name': r.name} for r in results])


@character_data_bp.route('/<int:character_id>/equipment', methods=['GET'])
@swag_from({
    'tags': ['Character Details'],
    'summary': 'Get character equipment',
    'parameters': [
        {'name': 'character_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {
            'description': 'List of equipment',
            'examples': {
                'application/json': [
                    {'id': 10, 'name': 'Longsword'},
                    {'id': 12, 'name': 'Shield'}
                ]
            }
        }
    }
})
def get_character_equipment(character_id):
    session = db()
    results = (
        session.query(Equipment.id, Equipment.name)
        .join(CharacterEquipment, Equipment.id == CharacterEquipment.equipment_id)
        .filter(CharacterEquipment.character_id == character_id)
        .all()
    )
    return jsonify([{'id': r.id, 'name': r.name} for r in results])


@character_data_bp.route('/<int:character_id>/spells', methods=['GET'])
@swag_from({
    'tags': ['Character Details'],
    'summary': 'Get character spells',
    'parameters': [
        {'name': 'character_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {
            'description': 'List of spells',
            'examples': {
                'application/json': [
                    {'id': 7, 'name': 'Fireball'},
                    {'id': 9, 'name': 'Mage Armor'}
                ]
            }
        }
    }
})
def get_character_spells(character_id):
    session = db()
    results = (
        session.query(Spells.id, Spells.name)
        .join(CharacterSpell, Spells.id == CharacterSpell.spell_id)
        .filter(CharacterSpell.character_id == character_id)
        .all()
    )
    return jsonify([{'id': r.id, 'name': r.name} for r in results])


@character_data_bp.route('/<int:character_id>/traits', methods=['GET'])
@swag_from({
    'tags': ['Character Details'],
    'summary': 'Get character traits',
    'parameters': [
        {'name': 'character_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {
            'description': 'List of traits',
            'examples': {
                'application/json': [
                    {'id': 4, 'name': 'Brave'},
                    {'id': 6, 'name': 'Lucky'}
                ]
            }
        }
    }
})
def get_character_traits(character_id):
    session = db()
    results = (
        session.query(Traits.id, Traits.name)
        .join(CharacterTrait, Traits.id == CharacterTrait.trait_id)
        .filter(CharacterTrait.character_id == character_id)
        .all()
    )
    return jsonify([{'id': r.id, 'name': r.name} for r in results])


@character_data_bp.route('/<int:character_id>/conditions', methods=['GET'])
@swag_from({
    'tags': ['Character Details'],
    'summary': 'Get character conditions',
    'parameters': [
        {'name': 'character_id', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {
            'description': 'List of conditions',
            'examples': {
                'application/json': [
                    {'id': 8, 'name': 'Poisoned'},
                    {'id': 11, 'name': 'Stunned'}
                ]
            }
        }
    }
})
def get_character_conditions(character_id):
    session = db()
    results = (
        session.query(Conditions.id, Conditions.name)
        .join(CharacterCondition, Conditions.id == CharacterCondition.condition_id)
        .filter(CharacterCondition.character_id == character_id)
        .all()
    )
    return jsonify([{'id': r.id, 'name': r.name} for r in results])
