from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models import Base

class CharacterSpell(Base):
    __tablename__ = "character_spells"

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id", ondelete="CASCADE"))
    spell_id = Column(Integer, ForeignKey("spells.id"))
    is_prepared = Column(Boolean, default=False)
    is_known = Column(Boolean, default=True)

    character = relationship("Character", back_populates="spells")
