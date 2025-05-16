from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean, Float, Table, UniqueConstraint, ForeignKeyConstraint
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from typing import List, Optional

class Base(DeclarativeBase):
    pass

# ===================== CLASSES =====================
class Classes(Base):
    __tablename__ = "classes"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    hit_die: Mapped[Optional[int]]
    url: Mapped[str] = mapped_column(String)

    subclass: Mapped[Optional['Subclasses']] = relationship("Subclasses", back_populates="class_", uselist=False)

    classes_proficiencies: Mapped[List['ClassesProficiencies']] = relationship("ClassesProficiencies", back_populates="class_")
    classes_saving_throws: Mapped[List['ClassesSavingThrows']] = relationship("ClassesSavingThrows", back_populates="class_")
    classes_proficiency_choices: Mapped[List['ClassesProficiencyChoices']] = relationship("ClassesProficiencyChoices", back_populates="class_")
    classes_starting_equipment_options: Mapped[List['ClassesStartingEquipmentOptions']] = relationship("ClassesStartingEquipmentOptions", back_populates="class_")

# ===================== SUBCLASSES =====================
class Subclasses(Base):
    __tablename__ = "subclasses"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)
    url: Mapped[str] = mapped_column(String)
    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))

    class_: Mapped['Classes'] = relationship("Classes", back_populates="subclass")

# ===================== PROFICIENCIES =====================
class Proficiencies(Base):
    __tablename__ = "proficiencies"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String)

# ===================== ABILITY SCORES =====================
class AbilityScores(Base):
    __tablename__ = "ability_scores"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

# ===================== EQUIPMENT =====================
class Equipment(Base):
    __tablename__ = "equipment"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

# ===================== CLASSES RELATIONSHIP TABLES =====================
class ClassesProficiencies(Base):
    __tablename__ = "classes_proficiencies"

    id: Mapped[int] = mapped_column(primary_key=True)
    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    proficiency_id: Mapped[int] = mapped_column(ForeignKey("proficiencies.id"))

    class_: Mapped['Classes'] = relationship("Classes", back_populates="classes_proficiencies")
    proficiency: Mapped['Proficiencies'] = relationship("Proficiencies")

class ClassesSavingThrows(Base):
    __tablename__ = "classes_saving_throws"

    id: Mapped[int] = mapped_column(primary_key=True)
    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    ability_score_id: Mapped[int] = mapped_column(ForeignKey("ability_scores.id"))

    class_: Mapped['Classes'] = relationship("Classes", back_populates="classes_saving_throws")
    ability_score: Mapped['AbilityScores'] = relationship("AbilityScores")

class ClassesProficiencyChoices(Base):
    __tablename__ = "classes_proficiency_choices"

    id: Mapped[int] = mapped_column(primary_key=True)
    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    proficiency_id: Mapped[int] = mapped_column(ForeignKey("proficiencies.id"))

    class_: Mapped['Classes'] = relationship("Classes", back_populates="classes_proficiency_choices")
    proficiency: Mapped['Proficiencies'] = relationship("Proficiencies")

class ClassesStartingEquipmentOptions(Base):
    __tablename__ = "classes_starting_equipment_options"

    id: Mapped[int] = mapped_column(primary_key=True)
    class_id: Mapped[int] = mapped_column(ForeignKey("classes.id"))
    equipment_id: Mapped[int] = mapped_column(ForeignKey("equipment.id"))

    class_: Mapped['Classes'] = relationship("Classes", back_populates="classes_starting_equipment_options")
    equipment: Mapped['Equipment'] = relationship("Equipment")

# ===================== MONSTERS =====================
class Monsters(Base):
    __tablename__ = "monsters"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

    monsters_special_abilities: Mapped[List['MonstersSpecialAbilities']] = relationship("MonstersSpecialAbilities", back_populates="monster")
    monster_actions: Mapped[List['MonsterActions']] = relationship("MonsterActions", back_populates="monster")
    monster_proficiencies: Mapped[List['MonsterProficiencies']] = relationship("MonsterProficiencies", back_populates="monster")
    monster_condition_immunities: Mapped[List['MonsterConditionImmunities']] = relationship("MonsterConditionImmunities", back_populates="monster")
    monster_legendary_actions: Mapped[List['MonsterLegendaryActions']] = relationship("MonsterLegendaryActions", back_populates="monster")
    monster_reactions: Mapped[List['MonsterReactions']] = relationship("MonsterReactions", back_populates="monster")

# ===================== MONSTERS RELATION TABLES =====================
class MonstersSpecialAbilities(Base):
    __tablename__ = "monsters_special_abilities"

    id: Mapped[int] = mapped_column(primary_key=True)
    monster_id: Mapped[int] = mapped_column(ForeignKey("monsters.id"))

    monster: Mapped['Monsters'] = relationship("Monsters", back_populates="monsters_special_abilities")
    monster_spells: Mapped[List['MonsterSpells']] = relationship("MonsterSpells", back_populates="monster_special_ability")

class MonsterSpells(Base):
    __tablename__ = "monster_spells"

    id: Mapped[int] = mapped_column(primary_key=True)
    monster_special_ability_id: Mapped[int] = mapped_column(ForeignKey("monsters_special_abilities.id"))
    spell_id: Mapped[int] = mapped_column(ForeignKey("spells.id"))

    monster_special_ability: Mapped['MonstersSpecialAbilities'] = relationship("MonstersSpecialAbilities", back_populates="monster_spells")
    spell: Mapped['Spells'] = relationship("Spells")

class Spells(Base):
    __tablename__ = "spells"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]

class MonsterActions(Base):
    __tablename__ = "monster_actions"

    id: Mapped[int] = mapped_column(primary_key=True)
    monster_id: Mapped[int] = mapped_column(ForeignKey("monsters.id"))
    name: Mapped[str]

    monster: Mapped['Monsters'] = relationship("Monsters", back_populates="monster_actions")

class MonsterProficiencies(Base):
    __tablename__ = "monster_proficiencies"

    id: Mapped[int] = mapped_column(primary_key=True)
    monster_id: Mapped[int] = mapped_column(ForeignKey("monsters.id"))

    monster: Mapped['Monsters'] = relationship("Monsters", back_populates="monster_proficiencies")

class MonsterConditionImmunities(Base):
    __tablename__ = "monster_condition_immunities"

    id: Mapped[int] = mapped_column(primary_key=True)
    monster_id: Mapped[int] = mapped_column(ForeignKey("monsters.id"))

    monster: Mapped['Monsters'] = relationship("Monsters", back_populates="monster_condition_immunities")

class MonsterLegendaryActions(Base):
    __tablename__ = "monster_legendary_actions"

    id: Mapped[int] = mapped_column(primary_key=True)
    monster_id: Mapped[int] = mapped_column(ForeignKey("monsters.id"))

    monster: Mapped['Monsters'] = relationship("Monsters", back_populates="monster_legendary_actions")

class MonsterReactions(Base):
    __tablename__ = "monster_reactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    monster_id: Mapped[int] = mapped_column(ForeignKey("monsters.id"))

    monster: Mapped['Monsters'] = relationship("Monsters", back_populates="monster_reactions")
