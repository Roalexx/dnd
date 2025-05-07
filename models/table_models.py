from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Subclasses(Base):
    __tablename__ = "subclasses"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    features = relationship("SubclassesFeatures", backref="subclass", cascade="all, delete-orphan")
    spells = relationship("SpellsSubclasses", backref="subclass", cascade="all, delete-orphan")
    def __repr__(self): return f"<Subclass {self.name}>"

class Subraces(Base):
    __tablename__ = "subraces"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    ability_bonuses = relationship("SubracesAbilityBonuses", backref="subrace", cascade="all, delete-orphan")
    languages = relationship("SubracesLanguages", backref="subrace", cascade="all, delete-orphan")
    traits = relationship("SubracesTraits", backref="subrace", cascade="all, delete-orphan")
    def __repr__(self): return f"<Subrace {self.name}>"

class Features(Base):
    __tablename__ = "features"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    prerequisite_options = relationship("FeaturesPrerequisiteOptions", backref="feature", cascade="all, delete-orphan")
    def __repr__(self): return f"<Feature {self.name}>"

class Proficiencies(Base):
    __tablename__ = "proficiencies"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    def __repr__(self): return f"<Proficiency {self.name}>"

class Skills(Base):
    __tablename__ = "skills"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    def __repr__(self): return f"<Skill {self.name}>"

class Feats(Base):
    __tablename__ = "feats"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    prerequisites = relationship("FeatsPrerequisites", backref="feat", cascade="all, delete-orphan")
    descending_feats = relationship("FeatsDescendingFeats", backref="feat", cascade="all, delete-orphan")
    def __repr__(self): return f"<Feat {self.name}>"

class MagicItems(Base):
    __tablename__ = "magic_items"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    descending_magic_items = relationship("MagicItemsDescendingMagicItems", backref="magic_item", cascade="all, delete-orphan")
    equipment_categories = relationship("MagicItemsEquipmentCategories", backref="magic_item", cascade="all, delete-orphan")
    def __repr__(self): return f"<MagicItem {self.name}>"

class WeaponCategories(Base):
    __tablename__ = "weapon_categories"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    weapons = relationship("WeaponCategoriesWeapons", backref="weapon_category", cascade="all, delete-orphan")
    def __repr__(self): return f"<WeaponCategory {self.name}>"

class AbilityScores(Base):
    __tablename__ = "ability_scores"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    descriptions = relationship("AbilityScoresDescriptions", backref="ability_score", cascade="all, delete-orphan")
    skills = relationship("AbilityScoresSkills", backref="ability_score", cascade="all, delete-orphan")
    def __repr__(self): return f"<AbilityScore {self.name}>"

class Languages(Base):
    __tablename__ = "languages"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    backgrounds = relationship("BackgroundsLanguages", backref="language", cascade="all, delete-orphan")
    def __repr__(self): return f"<Language {self.name}>"

class Backgrounds(Base):
    __tablename__ = "backgrounds"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    starting_equipment_options = relationship("BackgroundsStartingEquipmentOptions", backref="background", cascade="all, delete-orphan")
    starting_equipments = relationship("BackgroundsStartingEquipments", backref="background", cascade="all, delete-orphan")
    starting_proficiencies = relationship("BackgroundsStartingProficiencies", backref="background", cascade="all, delete-orphan")
    def __repr__(self): return f"<Background {self.name}>"

class Conditions(Base):
    __tablename__ = "conditions"
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    descending_conditions = relationship("ConditionsDescendingConditions", backref="condition", cascade="all, delete-orphan")
    def __repr__(self): return f"<Condition {self.name}>"
