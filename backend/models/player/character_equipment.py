from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class CharacterEquipment(Base):
    __tablename__ = "character_equipment"

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id", ondelete="CASCADE"))
    equipment_id = Column(Integer, ForeignKey("equipment.id"))
    quantity = Column(Integer, default=1)

    character = relationship("Character", back_populates="equipment")
