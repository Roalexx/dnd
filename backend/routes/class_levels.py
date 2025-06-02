from flask import Blueprint, jsonify
from flasgger import swag_from
from sqlalchemy.orm import Session
from config import SessionLocal
from models.models import Levels, Features

levels_bp = Blueprint('levels', __name__, url_prefix='/api')

@levels_bp.route("/class-levels/<int:class_id>/<int:level>", methods=["GET"])
@swag_from({
    'tags': ['Class Levels'],
    'summary': 'Get full level details with class name and feature list',
    'parameters': [
        {'name': 'class_id', 'in': 'path', 'type': 'integer', 'required': True},
        {'name': 'level', 'in': 'path', 'type': 'integer', 'required': True}
    ],
    'responses': {
        200: {
            'description': 'Full info including spells, cantrips and features'
        },
        404: {'description': 'Not found'}
    }
})
def get_class_level(class_id, level):
    session: Session = SessionLocal()
    try:
        level_entry = session.query(Levels).filter(
            Levels.class_id == class_id,
            Levels.level == level
        ).first()

        if not level_entry:
            return jsonify({"error": "Data not found"}), 404

        detail = level_entry.detail
        if not detail:
            return jsonify({"error": "Level detail not found"}), 404

        # Feature isimleri ve açıklamaları
        feature_list = [
            {
                "feature_id": feature.feature.id,
                "name": feature.feature.name,
                "desc": feature.feature.description
            }
            for feature in detail.level_detail_features if feature.feature
        ]

        return jsonify({
            "id": level_entry.id,
            "class_id": level_entry.class_id,
            "class_name": level_entry.class_.name if level_entry.class_ else None,
            "level": level_entry.level,
            "ability_score_bonuses": level_entry.ability_score_bonuses,
            "prof_bonus": level_entry.prof_bonus,
            "detail_id": level_entry.detail_id,

            "cantrips_known": detail.cantrips_known,
            "spells_known": detail.spells_known,
            "spell_slots": {
                "level_1": detail.spell_slots_level_1,
                "level_2": detail.spell_slots_level_2,
                "level_3": detail.spell_slots_level_3,
                "level_4": detail.spell_slots_level_4,
                "level_5": detail.spell_slots_level_5,
                "level_6": detail.spell_slots_level_6,
                "level_7": detail.spell_slots_level_7,
                "level_8": detail.spell_slots_level_8,
                "level_9": detail.spell_slots_level_9
            },
            "features": feature_list
        }), 200
    finally:
        session.close()
