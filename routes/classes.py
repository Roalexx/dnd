from flask import Blueprint, jsonify
from flasgger import swag_from
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from config import SessionLocal
from sqlalchemy.orm import selectinload
from models.models import (
    Classes,
    ClassesProficiencies,
    ClassesSavingThrows,
    ClassesProficiencyChoices,
    ClassesStartingEquipmentOptions,
)

classes_bp = Blueprint("classes", __name__)

@classes_bp.route("/classes", methods=["GET"])
@swag_from({
    "tags": ["Classes"],
    "summary": "Get all classes with full relations",
    "description": "Fetch all classes and their related proficiencies, saving throws, subclasses, and more.",
    "responses": {
        200: {
            "description": "A list of all classes"
        }
    }
})
def get_classes():
    session = SessionLocal()
    classes = session.query(Classes).options(
        selectinload(Classes.classes_proficiencies).selectinload(ClassesProficiencies.proficiency),
        selectinload(Classes.classes_saving_throws).selectinload(ClassesSavingThrows.ability_score),
        selectinload(Classes.classes_proficiency_choices).selectinload(ClassesProficiencyChoices.proficiency),
        selectinload(Classes.classes_starting_equipment_options).selectinload(ClassesStartingEquipmentOptions.equipment),
        selectinload(Classes.subclass)
    ).all()

    result = []
    for c in classes:
        result.append({
            "id": c.id,
            "name": c.name,
            "hit_die": c.hit_die,
            "subclass": c.subclass.name if c.subclass else None,
            "proficiencies": [p.proficiency.name for p in c.classes_proficiencies],
            "saving_throws": [s.ability_score.name for s in c.classes_saving_throws],
            "proficiency_choices": [p.proficiency.name for p in c.classes_proficiency_choices],
            "starting_equipment_options": [e.equipment.name for e in c.classes_starting_equipment_options]
        })

    return jsonify(result)
