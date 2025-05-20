from sqlalchemy import Column, Integer, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from models import Base

# 1. CharacterSkill
class CharacterSkill(Base):
    __tablename__ = "character_skills"

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id", ondelete="CASCADE"))
    skill_id = Column(Integer, ForeignKey("skills.id", ondelete="CASCADE"))
    is_proficient = Column(Boolean, default=False)

    character = relationship("Character", back_populates="skills")


# 2. CharacterLanguage (zaten vardı ama buraya dahil ettik)
class CharacterLanguage(Base):
    __tablename__ = "character_languages"

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id", ondelete="CASCADE"))
    language_id = Column(Integer, ForeignKey("languages.id", ondelete="CASCADE"))

    character = relationship("Character", back_populates="languages")


# 3. CharacterTrait
class CharacterTrait(Base):
    __tablename__ = "character_traits"

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id", ondelete="CASCADE"))
    trait_id = Column(Integer, ForeignKey("traits.id"))

    character = relationship("Character", back_populates="traits")


# 4. CharacterSavingThrow
class CharacterSavingThrow(Base):
    __tablename__ = "character_saving_throws"

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id", ondelete="CASCADE"))
    ability_score_id = Column(Integer, ForeignKey("ability_scores.id"))
    is_proficient = Column(Boolean, default=False)

    character = relationship("Character", back_populates="saving_throws")


# 5. CharacterCondition (opsiyonel)
class CharacterCondition(Base):
    __tablename__ = "character_conditions"

    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey("characters.id", ondelete="CASCADE"))
    condition_id = Column(Integer, ForeignKey("conditions.id"))
    is_active = Column(Boolean, default=True)

    character = relationship("Character", back_populates="conditions")