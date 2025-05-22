from flask import Blueprint, jsonify
from flasgger import swag_from
from sqlalchemy.orm import joinedload, selectinload
from config import SessionLocal
from models.models import Classes
from sqlalchemy.inspection import inspect

classes_bp = Blueprint("classes", __name__)

@classes_bp.route("/classes", methods=["GET"])
@swag_from({
    'tags': ['Classes'],
    'summary': 'Get all classes with relationships',
    'description': 'Returns all fields and foreign key relationships for all classes.',
    'responses': {
        200: {
            'description': 'Full class list with related tables'
        }
    }
})
def get_classes():
    session = SessionLocal()
    try:
        classes = session.query(Classes).options(
            selectinload(Classes.features),
            selectinload(Classes.subclasses),
            selectinload(Classes.levels)
        ).all()

        result = []
        for cls in classes:
            class_dict = {
                column.name: getattr(cls, column.name)
                for column in Classes.__table__.columns
            }

            for rel in Classes.__mapper__.relationships:
                rel_data = getattr(cls, rel.key)
                if isinstance(rel_data, list): 
                    class_dict[rel.key] = [
                        {
                            column.name: getattr(item, column.name)
                            for column in item.__table__.columns
                        } for item in rel_data
                    ]
                elif rel_data:  
                    class_dict[rel.key] = {
                        column.name: getattr(rel_data, column.name)
                        for column in rel_data.__table__.columns
                    }

            result.append(class_dict)

        return jsonify(result), 200
    finally:
        session.close()

@classes_bp.route("/classes/<int:class_id>", methods=["GET"])
@swag_from({
    'tags': ['Classes'],
    'summary': 'Get single class by ID with full relationships including join-table foreign keys',
    'description': 'Returns a class with all its fields and related data. Also expands join tables by resolving their foreign keys.',
    'parameters': [
        {
            'name': 'class_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the class'
        }
    ],
    'responses': {
        200: {'description': 'Class with full data'},
        404: {'description': 'Class not found'}
    }
})
def get_class_by_id(class_id):
    session = SessionLocal()
    try:
        cls = session.query(Classes).options(
            selectinload(Classes.features),
            selectinload(Classes.subclasses),
            selectinload(Classes.levels),
            selectinload(Classes.class_multi_classing_proficiencies),
            selectinload(Classes.classes_proficiencies),
            selectinload(Classes.classes_proficiency_choices),
            selectinload(Classes.spells_classes)
        ).filter(Classes.id == class_id).first()

        if not cls:
            return jsonify({"error": "Class not found"}), 404

        class_dict = {
            column.name: getattr(cls, column.name)
            for column in Classes.__table__.columns
        }

        for rel in Classes.__mapper__.relationships:
            rel_data = getattr(cls, rel.key)

            if isinstance(rel_data, list):
                rel_list = []
                for item in rel_data:
                    if not hasattr(item, '__table__'):
                        continue

                    item_dict = {
                        column.name: getattr(item, column.name)
                        for column in item.__table__.columns
                    }

                    for sub_rel in inspect(item.__class__).relationships:
                        sub_data = getattr(item, sub_rel.key)
                        if sub_data and hasattr(sub_data, '__table__'):
                            item_dict[sub_rel.key] = {
                                column.name: getattr(sub_data, column.name)
                                for column in sub_data.__table__.columns
                            }

                    rel_list.append(item_dict)
                class_dict[rel.key] = rel_list

            elif rel_data and hasattr(rel_data, '__table__'):
                class_dict[rel.key] = {
                    column.name: getattr(rel_data, column.name)
                    for column in rel_data.__table__.columns
                }

        return jsonify(class_dict), 200

    finally:
        session.close()

