from sqlalchemy import (
    Column, Integer, String, Text, ForeignKey,
    DateTime, Boolean, CheckConstraint, func
)
from sqlalchemy.orm import relationship
from datetime import datetime
from models import Base


class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)

    # foreign keys
    user_id = Column(Integer, ForeignKey("users.id"))
    dungeon_master_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    subclass_id = Column(Integer, ForeignKey("subclasses.id"), nullable=True)
    race_id = Column(Integer, ForeignKey("races.id"))
    feat_id = Column(Integer, ForeignKey("feats.id"), nullable=True)
    alignment_id = Column(Integer, ForeignKey("alignments.id"))
    character_size_id = Column(Integer, ForeignKey("character_sizes.id"), nullable=False)

    # core fields
    name = Column(String(100), nullable=False)
    level = Column(Integer, nullable=False, server_default="1")
    experience = Column(Integer, nullable=False, server_default="0")

    strength = Column(Integer, nullable=False)
    dexterity = Column(Integer, nullable=False)
    constitution = Column(Integer, nullable=False)
    intelligence = Column(Integer, nullable=False)
    wisdom = Column(Integer, nullable=False)
    charisma = Column(Integer, nullable=False)

    hit_points = Column(Integer, nullable=False)
    armor_class = Column(Integer, nullable=False)
    speed = Column(Integer, nullable=False)

    gold = Column(Integer, nullable=False, server_default="0")
    silver = Column(Integer, nullable=False, server_default="0")
    copper = Column(Integer, nullable=False, server_default="0")

    personality = Column(Text)
    ideals = Column(Text)
    bonds = Column(Text)
    flaws = Column(Text)
    notes = Column(Text)

    image_url = Column(String(255))
    created_at = Column(DateTime, nullable=False, server_default=func.now())

    is_admin = Column(Boolean, nullable=False, server_default="false")

    # relationships
    alignment = relationship("Alignments", backref="characters")
    user = relationship("User", back_populates="characters", foreign_keys=[user_id])
    dungeon_master = relationship("User", back_populates="managed_characters",
                                  foreign_keys=[dungeon_master_id])

    spells = relationship("CharacterSpell", back_populates="character", cascade="all, delete-orphan")
    equipment = relationship("CharacterEquipment", back_populates="character", cascade="all, delete-orphan")
    skills = relationship("CharacterSkill", back_populates="character", cascade="all, delete-orphan")
    languages = relationship("CharacterLanguage", back_populates="character", cascade="all, delete-orphan")
    traits = relationship("CharacterTrait", back_populates="character", cascade="all, delete-orphan")
    saving_throws = relationship("CharacterSavingThrow", back_populates="character", cascade="all, delete-orphan")
    conditions = relationship("CharacterCondition", back_populates="character", cascade="all, delete-orphan")
    proficiencies = relationship("CharacterProficiency", back_populates="character", cascade="all, delete-orphan")
    features = relationship("CharacterFeature", back_populates="character", cascade="all, delete-orphan")

    __table_args__ = (
        CheckConstraint(level >= 1, name="ck_character_level_positive"),
    )
