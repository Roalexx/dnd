from sqlalchemy import Column, Integer, ForeignKey, Text
from models import Base

class ClassesStartingEquipmentOptions(Base):
    __tablename__ = 'classes_starting_equipment_options'
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer, ForeignKey("classes.id"))
    option_id = Column(Integer, ForeignKey("starting_equipment_option.id"))
    def __repr__(self): return f"<ClassesStartingEquipmentOptions {self.id}>"

class StartingEquipmentOptionItem(Base):
    __tablename__ = 'starting_equipment_option_item'
    id = Column(Integer, primary_key=True)
    option_id = Column(Integer, ForeignKey("starting_equipment_option.id"))
    starting_equipment_id = Column(Integer, ForeignKey("equipment.id"), nullable=True)  
    equipment_id = Column(Integer, ForeignKey("equipment.id"), nullable=True)
    equipment_category_id = Column(Integer, ForeignKey("equipment_categories.id"), nullable=True)
    quantity = Column(Integer, default=1)
    def __repr__(self): return f"<StartingEquipmentOptionItem {self.id}>"

