from flask import Blueprint, jsonify
from flasgger import swag_from
from config import SessionLocal
from models.models import ClassesLevels

levels_bp = Blueprint("levels", __name__, url_prefix="/api")

@levels_bp.route("/class-levels/<int:class_id>/<int:level>", methods=["GET"])
@swag_from({
    'tags': ['Class Levels'],
    'summary': 'Get spell/cantrip info for class at level',
    'parameters': [
        {'name': 'class_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'level', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {
            'description': 'Level info for class',
            'examples': {
                'application/json': {
                    "spells_known": 4,
                    "cantrips_known": 2
                }
            }
        },
        404: {'description': 'Not found'}
    }
})
def get_class_level(class_id, level):
    session = SessionLocal()
    try:
        result = session.query(ClassesLevels).filter(
            ClassesLevels.class_id == class_id,
            ClassesLevels.level_id == level
        ).first()

        if not result:
            return jsonify({"error": "Data not found"}), 404

        return jsonify({
            "spells_known": result.spells_known,
            "cantrips_known": result.cantrips_known
        }), 200
    finally:
        session.close()
