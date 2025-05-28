from flask import Blueprint, jsonify
from flasgger import swag_from
from config import SessionLocal
from models.models import Equipment

equipment_bp = Blueprint("equipment", __name__, url_prefix="/api/equipment")

@equipment_bp.route("/<int:equipment_id>", methods=["GET"])
@swag_from({
    'tags': ['Equipment'],
    'summary': 'Get equipment by ID',
    'parameters': [
        {
            'name': 'equipment_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID of the equipment'
        }
    ],
    'responses': {
        200: {
            'description': 'Equipment found',
            'examples': {
                'application/json': {
                    "id": 27,
                    "name": "Shield",
                    "category": "Armor",
                    "weight": 6
                }
            }
        },
        404: {'description': 'Equipment not found'}
    }
})
def get_equipment_by_id(equipment_id):
    session = SessionLocal()
    try:
        equipment = session.query(Equipment).filter_by(id=equipment_id).first()
        if not equipment:
            return jsonify({"error": "Equipment not found"}), 404

        data = {col.name: getattr(equipment, col.name) for col in Equipment.__table__.columns}
        return jsonify(data), 200
    finally:
        session.close()