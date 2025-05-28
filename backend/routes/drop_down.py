from flask import Blueprint, jsonify
from flasgger import swag_from
from sqlalchemy.orm import selectinload
from sqlalchemy.inspection import inspect
from config import SessionLocal
from models.models import Races, Classes, Alignments, CharacterSize

# --------- RACES ---------
races_bp = Blueprint("races", __name__)

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

# --------- CLASSES ---------
classes_bp = Blueprint("classes", __name__)

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

# --------- ALIGNMENTS ---------
alignments_bp = Blueprint("alignments", __name__)

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
sizes_bp = Blueprint("character_sizes", __name__)

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
