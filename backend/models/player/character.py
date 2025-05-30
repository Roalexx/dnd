from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from models import Base

class Character(Base):
    __tablename__ = "characters"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    dungeon_master_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    name = Column(String(100), nullable=False)

    class_id = Column(Integer, ForeignKey("classes.id"))
    subclass_id = Column(Integer, ForeignKey("subclasses.id"), nullable=True)
    race_id = Column(Integer, ForeignKey("races.id"))
    feat_id = Column(Integer, ForeignKey("feats.id"), nullable=True)
    
    alignment_id = Column(Integer, ForeignKey("alignments.id"))
    level = Column(Integer, default=1)
    experience = Column(Integer, default=0)

    strength = Column(Integer)
    dexterity = Column(Integer)
    constitution = Column(Integer)
    intelligence = Column(Integer)
    wisdom = Column(Integer)
    charisma = Column(Integer)

    hit_points = Column(Integer)
    armor_class = Column(Integer)
    speed = Column(Integer)

    gold = Column(Integer, default=0)
    silver = Column(Integer, default=0)
    copper = Column(Integer, default=0)

    personality = Column(Text)
    ideals = Column(Text)
    bonds = Column(Text)
    flaws = Column(Text)

    image_url = Column(String(255), nullable=True)
    notes = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)

    is_admin = Column(Boolean, nullable=True)

    alignment = relationship("Alignments", backref="characters")
    user = relationship("User", back_populates="characters", foreign_keys=[user_id])
    dungeon_master = relationship("User", back_populates="managed_characters", foreign_keys=[dungeon_master_id])

    # Alt ilişkiler
    spells = relationship("CharacterSpell", back_populates="character", cascade="all, delete-orphan")
    equipment = relationship("CharacterEquipment", back_populates="character", cascade="all, delete-orphan")
    skills = relationship("CharacterSkill", back_populates="character", cascade="all, delete-orphan")
    languages = relationship("CharacterLanguage", back_populates="character", cascade="all, delete-orphan")
    traits = relationship("CharacterTrait", back_populates="character", cascade="all, delete-orphan")
    saving_throws = relationship("CharacterSavingThrow", back_populates="character", cascade="all, delete-orphan")
    conditions = relationship("CharacterCondition", back_populates="character", cascade="all, delete-orphan")
    proficiencies = relationship("CharacterProficiency", back_populates="character", cascade="all, delete-orphan")
    features = relationship("CharacterFeature", back_populates="character", cascade="all, delete-orphan")
