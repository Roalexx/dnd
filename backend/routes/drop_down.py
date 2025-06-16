from flask import Blueprint, jsonify
from flasgger import swag_from
from sqlalchemy.orm import selectinload
from config import SessionLocal
from models.models import (
    Races, Classes, Alignments, CharacterSize,
    Proficiencies, AbilityScores
)

# --------- BLUEPRINTS ---------
races_bp = Blueprint("races", __name__)
classes_bp = Blueprint("classes", __name__)
alignments_bp = Blueprint("alignments", __name__)
sizes_bp = Blueprint("character_sizes", __name__)

# --------- RACES ---------
@races_bp.route("/api/races", methods=["GET"])
@swag_from({
    'tags': ['Dropdown'],
    'summary': 'Get all races with relationships',
    'description': 'Returns all races with their fields and relationships.',
    'responses': {200: {'description': 'List of all races'}}
})
def get_races():
    session = SessionLocal()
    try:
        races = session.query(Races).options(*[
            selectinload(getattr(Races, rel.key)) for rel in Races.__mapper__.relationships
        ]).all()

        result = []
        for race in races:
            race_dict = {col.name: getattr(race, col.name) for col in Races.__table__.columns}
            for rel in Races.__mapper__.relationships:
                rel_data = getattr(race, rel.key)
                if isinstance(rel_data, list):
                    race_dict[rel.key] = [{col.name: getattr(item, col.name) for col in item.__table__.columns} for item in rel_data]
                elif rel_data:
                    race_dict[rel.key] = {col.name: getattr(rel_data, col.name) for col in rel_data.__table__.columns}
            result.append(race_dict)
        return jsonify(result), 200
    finally:
        session.close()

@races_bp.route("/api/races/<int:race_id>", methods=["GET"])
@swag_from({
    'tags': ['Dropdown'],
    'summary': 'Get a single race with relationships',
    'description': 'Returns a specific race and all its fields and related options like ability bonuses, traits, languages, proficiencies, and subraces.',
    'parameters': [
        {
            'name': 'race_id',
            'in': 'path',
            'required': True,
            'schema': {'type': 'integer'},
            'description': 'ID of the race to retrieve'
        }
    ],
    'responses': {
        200: {'description': 'Race data returned successfully'},
        404: {'description': 'Race not found'}
    }
})
def get_race_by_id(race_id):
    session = SessionLocal()
    try:
        race = session.query(Races).options(*[
            selectinload(getattr(Races, rel.key)) for rel in Races.__mapper__.relationships
        ]).filter(Races.id == race_id).first()

        if not race:
            return jsonify({"error": "Race not found"}), 404

        race_dict = {col.name: getattr(race, col.name) for col in Races.__table__.columns}

        for rel in Races.__mapper__.relationships:
            rel_data = getattr(race, rel.key)

            if isinstance(rel_data, list):
                if rel.key == "race_ability_bonus_options":
                    race_dict[rel.key] = [
                        {
                            "id": item.id,
                            "ability_score_id": item.ability_score_id,
                            "ability_score_name": item.ability_score.name if item.ability_score else None
                        }
                        for item in rel_data
                    ]
                elif rel.key == "race_languages":
                    race_dict[rel.key] = [
                        {
                            "id": item.id,
                            "language_id": item.language_id,
                            "language_name": item.language.name if item.language else None
                        }
                        for item in rel_data
                    ]
                elif rel.key == "race_language_options":
                    race_dict[rel.key] = [
                        {
                            "id": item.id,
                            "language_id": item.language_id,
                            "language_name": item.language.name if item.language else None
                        }
                        for item in rel_data
                    ]
                elif rel.key == "race_proficiency_options":
                    race_dict[rel.key] = [
                        {
                            "id": item.id,
                            "proficiency_id": item.proficiency_id,
                            "proficiency_name": item.proficiency.name if item.proficiency else None,
                            "proficiency_type": item.proficiency.type if item.proficiency else None
                        }
                        for item in rel_data
                    ]
                elif rel.key == "race_traits":
                    race_dict[rel.key] = [
                        {
                            "id": item.id,
                            "trait_id": item.trait_id,
                            "trait_name": item.trait.name if item.trait else None,
                            "trait_description": item.trait.description if item.trait else None
                        }
                        for item in rel_data
                    ]
                elif rel.key == "race_proficiencies":
                    race_dict[rel.key] = [
                        {
                            "id": item.id,
                            "proficiency_id": item.proficiency_id,
                            "proficiency_name": item.proficiency.name if item.proficiency else None,
                            "proficiency_type": item.proficiency.type if item.proficiency else None
                        }
                        for item in rel_data
                    ]
                else:
                    race_dict[rel.key] = [
                        {col.name: getattr(item, col.name) for col in item.__table__.columns}
                        for item in rel_data
                    ]

            elif rel_data:
                race_dict[rel.key] = {
                    col.name: getattr(rel_data, col.name) for col in rel_data.__table__.columns
                }

        return jsonify(race_dict), 200

    finally:
        session.close()



# --------- CLASSES ---------
@classes_bp.route("/api/classes", methods=["GET"])
@swag_from({
    'tags': ['Dropdown'],
    'summary': 'Get all classes with relationships',
    'description': 'Returns all classes with fields and relationships.',
    'responses': {200: {'description': 'List of all classes'}}
})
def get_classes():
    session = SessionLocal()
    try:
        classes = session.query(Classes).options(*[
            selectinload(getattr(Classes, rel.key)) for rel in Classes.__mapper__.relationships
        ]).all()

        result = []
        for cls in classes:
            cls_dict = {col.name: getattr(cls, col.name) for col in Classes.__table__.columns}
            for rel in Classes.__mapper__.relationships:
                rel_data = getattr(cls, rel.key)
                if isinstance(rel_data, list):
                    cls_dict[rel.key] = [{col.name: getattr(item, col.name) for col in item.__table__.columns} for item in rel_data]
                elif rel_data:
                    cls_dict[rel.key] = {col.name: getattr(rel_data, col.name) for col in rel_data.__table__.columns}
            result.append(cls_dict)
        return jsonify(result), 200
    finally:
        session.close()


@classes_bp.route("/api/classes/<int:class_id>", methods=["GET"])
@swag_from({
    'tags': ['Dropdown'],
    'summary': 'Get a single class with relationships',
    'description': 'Returns a specific class and all its fields and relationships.',
    'parameters': [
        {
            'name': 'class_id',
            'in': 'path',
            'required': True,
            'schema': {'type': 'integer'},
            'description': 'ID of the class to retrieve'
        }
    ],
    'responses': {
        200: {'description': 'Class data returned successfully'},
        404: {'description': 'Class not found'}
    }
})
def get_class_by_id(class_id):
    session = SessionLocal()
    try:
        cls = session.query(Classes).options(*[
            selectinload(getattr(Classes, rel.key)) for rel in Classes.__mapper__.relationships
        ]).filter(Classes.id == class_id).first()

        if not cls:
            return jsonify({"error": "Class not found"}), 404

        cls_dict = {col.name: getattr(cls, col.name) for col in Classes.__table__.columns}

        for rel in Classes.__mapper__.relationships:
            rel_data = getattr(cls, rel.key)

            if isinstance(rel_data, list):
                if rel.key == 'spells_classes':
                    cls_dict[rel.key] = [
                        {
                            "id": item.id,
                            "spells_id": item.spells_id,
                            "classes_id": item.classes_id,
                            "spell_name": item.spells.name if item.spells else None,
                            "spell_description": item.spells.description if item.spells else None
                        }
                        for item in rel_data
                    ]
                elif rel.key in ['classes_starting_equipment', 'classes_starting_equipment_options']:
                    cls_dict[rel.key] = [
                        {
                            "id": item.id,
                            "equipment_id": item.equipment_id,
                            "class_id": getattr(item, "class_id", None),
                            "equipment_name": item.equipment.name if item.equipment else None,
                            "equipment_description": item.equipment.description if item.equipment else None,
                            "equipment_quantity": getattr(item, "quantity", None)
                        }
                        for item in rel_data
                    ]
                elif rel.key in ['classes_proficiencies', 'classes_proficiency_choices']:
                    cls_dict[rel.key] = [
                        {
                            "id": item.id,
                            "proficiency_id": item.proficiency_id,
                            "proficiency_name": item.proficiency.name if item.proficiency else None,
                            "proficiency_type": item.proficiency.type if item.proficiency else None
                        }
                        for item in rel_data
                    ]
                elif rel.key == 'classes_saving_throws':
                    cls_dict[rel.key] = [
                        {
                            "id": item.id,
                            "ability_score_id": item.ability_score_id,
                            "ability_score_name": item.ability_score.name if item.ability_score else None,
                            "ability_score_description": item.ability_score.description if item.ability_score else None
                        }
                        for item in rel_data
                    ]
                elif rel.key == 'class_multi_classing_proficiencies':
                    cls_dict[rel.key] = [
                        {
                            "id": item.id,
                            "proficiency_id": item.proficiency_id,
                            "proficiency_name": item.proficiency.name if item.proficiency else None,
                            "proficiency_type": item.proficiency.type if item.proficiency else None
                        }
                        for item in rel_data
                    ]
                elif rel.key == 'class_multi_classing_prerequisites':
                    cls_dict[rel.key] = [
                        {
                            "id": item.id,
                            "ability_score_id": item.ability_score_id,
                            "minimum_score": item.minimum_score,
                            "ability_score_name": item.ability_score.name if item.ability_score else None,
                            "ability_score_description": item.ability_score.description if item.ability_score else None
                        }
                        for item in rel_data
                    ]
                else:
                    cls_dict[rel.key] = [
                        {col.name: getattr(item, col.name) for col in item.__table__.columns}
                        for item in rel_data
                    ]
            elif rel_data:
                cls_dict[rel.key] = {
                    col.name: getattr(rel_data, col.name) for col in rel_data.__table__.columns
                }

        return jsonify(cls_dict), 200

    finally:
        session.close()


# --------- ALIGNMENTS ---------
@alignments_bp.route("/api/alignments", methods=["GET"])
@swag_from({
    'tags': ['Dropdown'],
    'summary': 'Get all alignments',
    'description': 'Returns all alignment options.',
    'responses': {200: {'description': 'List of alignments'}}
})
def get_alignments():
    session = SessionLocal()
    try:
        alignments = session.query(Alignments).all()
        result = [{col.name: getattr(alignment, col.name) for col in Alignments.__table__.columns} for alignment in alignments]
        return jsonify(result), 200
    finally:
        session.close()


# --------- CHARACTER SIZES ---------
@sizes_bp.route("/api/character-sizes", methods=["GET"])
@swag_from({
    'tags': ['Dropdown'],
    'summary': 'Get all character sizes',
    'description': 'Returns all character sizes.',
    'responses': {200: {'description': 'List of character sizes'}}
})
def get_character_sizes():
    session = SessionLocal()
    try:
        sizes = session.query(CharacterSize).all()
        result = [{col.name: getattr(size, col.name) for col in CharacterSize.__table__.columns} for size in sizes]
        return jsonify(result), 200
    finally:
        session.close()


# --------- PROFICIENCIES ---------
@classes_bp.route("/api/proficiencies", methods=["GET"])
@swag_from({
    'tags': ['Dropdown'],
    'summary': 'Get all proficiencies',
    'description': 'Returns all proficiency options.',
    'responses': {200: {'description': 'List of proficiencies'}}
})
def get_proficiencies():
    session = SessionLocal()
    try:
        profs = session.query(Proficiencies).all()
        result = [{col.name: getattr(p, col.name) for col in Proficiencies.__table__.columns} for p in profs]
        return jsonify(result), 200
    finally:
        session.close()


# --------- ABILITY SCORES ---------
@classes_bp.route("/api/ability-scores", methods=["GET"])
@swag_from({
    'tags': ['Dropdown'],
    'summary': 'Get all ability scores',
    'description': 'Returns all ability scores.',
    'responses': {200: {'description': 'List of ability scores'}}
})
def get_ability_scores():
    session = SessionLocal()
    try:
        scores = session.query(AbilityScores).all()
        result = [{col.name: getattr(s, col.name) for col in AbilityScores.__table__.columns} for s in scores]
        return jsonify(result), 200
    finally:
        session.close()
    