from sqlalchemy import Column, Integer, String, Boolean, Text, ForeignKey
from sqlalchemy.orm import relationship
from models import Base

class AbilityScores(Base):
    __tablename__ = 'ability_scores'
    id = Column(Integer, primary_key=True)
    desc = Column(Text)
    full_name = Column(String(255))
    index = Column(String(255))
    name = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<AbilityScores {self.id}>"

class Alignments(Base):
    __tablename__ = 'alignments'
    id = Column(Integer, primary_key=True)
    abbreviation = Column(String(255))
    desc = Column(Text)
    index = Column(String(255))
    name = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<Alignments {self.id}>"


class Classes(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    class_levels = Column(Text)
    hit_die = Column(Integer)
    index = Column(String(255))
    multi_classing = Column(Text)
    name = Column(String(255))
    proficiency_choices = Column(Text)
    proficiencies = Column(Text)
    saving_throws = Column(Text)
    starting_equipment = Column(Text)
    starting_equipment_options = Column(Text)
    subclasses = Column(Text)
    url = Column(String(255))
    def __repr__(self): return f"<Classes {self.id}>"

class Conditions(Base):
    __tablename__ = 'conditions'
    id = Column(Integer, primary_key=True)
    desc = Column(Text)
    index = Column(String(255))
    name = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<Conditions {self.id}>"

class DamageTypes(Base):
    __tablename__ = 'damage_types'
    id = Column(Integer, primary_key=True)
    desc = Column(Text)
    index = Column(String(255))
    name = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<DamageTypes {self.id}>"

class Equipment(Base):
    __tablename__ = 'equipment'
    id = Column(Integer, primary_key=True)
    category_range = Column(String(255))
    cost = Column(Text)
    damage = Column(Text)
    desc = Column(Text)
    equipment_category = Column(Text)
    gear_category = Column(Text)
    index = Column(String(255))
    name = Column(String(255))
    properties = Column(Text)
    range = Column(Text)
    special = Column(Text)
    speed = Column(Text)
    stealth_disadvantage = Column(Boolean)
    str_minimum = Column(Integer)
    throw_range = Column(Text)
    tool_category = Column(String(255))
    two_handed_damage = Column(Text)
    url = Column(String(255))
    vehicle_category = Column(String(255))
    weight = Column(String(255))
    weapon_category = Column(String(255))
    weapon_range = Column(String(255))
    weapon_range_type = Column(String(255))
    def __repr__(self): return f"<Equipment {self.id}>"

class StartingEquipmentOption(Base):
    __tablename__ = 'starting_equipment_option'
    id = Column(Integer, primary_key=True)
    desc = Column(Text)
    choose = Column(Integer)
    def __repr__(self): return f"<StartingEquipmentOption {self.id}>"

class ClassesStartingEquipment(Base):
    __tablename__ = 'classes_starting_equipment'
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer, ForeignKey("classes.id"))
    starting_equipment_id = Column(Integer, ForeignKey("equipment.id"))
    def __repr__(self): return f"<ClassesStartingEquipment {self.id}>"

class EquipmentCategories(Base):
    __tablename__ = 'equipment_categories'
    id = Column(Integer, primary_key=True)
    equipment = Column(Text)
    index = Column(String(255))
    name = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<EquipmentCategories {self.id}>"

class Feats(Base):
    __tablename__ = 'feats'
    id = Column(Integer, primary_key=True)
    desc = Column(Text)
    index = Column(String(255))
    name = Column(String(255))
    prerequisites = Column(Text)
    url = Column(String(255))
    def __repr__(self): return f"<Feats {self.id}>"

class Features(Base):
    __tablename__ = 'features'
    id = Column(Integer, primary_key=True)
    class_ = Column(String(255))
    desc = Column(Text)
    index = Column(String(255))
    level = Column(Integer)
    name = Column(String(255))
    parent = Column(String(255))
    prerequisites = Column(Text)
    subclass = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<Features {self.id}>"

class Languages(Base):
    __tablename__ = 'languages'
    id = Column(Integer, primary_key=True)
    index = Column(String(255))
    name = Column(String(255))
    script = Column(String(255))
    type = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<Languages {self.id}>"

class MagicItems(Base):
    __tablename__ = 'magic_items'
    id = Column(Integer, primary_key=True)
    desc = Column(Text)
    equipment_category = Column(Text)
    index = Column(String(255))
    name = Column(String(255))
    rarity = Column(Text)
    url = Column(String(255))
    def __repr__(self): return f"<MagicItems {self.id}>"

class MagicSchools(Base):
    __tablename__ = 'magic_schools'
    id = Column(Integer, primary_key=True)
    desc = Column(Text)
    index = Column(String(255))
    name = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<MagicSchools {self.id}>"

class Monsters(Base):
    __tablename__ = 'monsters'
    id = Column(Integer, primary_key=True)
    actions = Column(Text)
    alignment = Column(String(255))
    armor_class = Column(Text)
    challenge_rating = Column(String(255))
    charisma = Column(Integer)
    condition_immunities = Column(Text)
    constitution = Column(Integer)
    damage_immunities = Column(Text)
    damage_resistances = Column(Text)
    damage_vulnerabilities = Column(Text)
    dexterity = Column(Integer)
    forms = Column(Text)
    hit_dice = Column(String(255))
    hit_points = Column(Integer)
    index = Column(String(255))
    intelligence = Column(Integer)
    languages = Column(String(255))
    legendary_actions = Column(Text)
    legendary_desc = Column(Text)
    name = Column(String(255))
    proficiencies = Column(Text)
    reactions = Column(Text)
    senses = Column(Text)
    size = Column(String(255))
    special_abilities = Column(Text)
    speed = Column(Text)
    strength = Column(Integer)
    subtype = Column(String(255))
    type = Column(String(255))
    url = Column(String(255))
    wisdom = Column(Integer)
    xp = Column(Integer)
    def __repr__(self): return f"<Monsters {self.id}>"

class Proficiencies(Base):
    __tablename__ = 'proficiencies'
    id = Column(Integer, primary_key=True)
    index = Column(String(255))
    name = Column(String(255))
    references = Column(Text)
    type = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<Proficiencies {self.id}>"

class Races(Base):
    __tablename__ = 'races'
    id = Column(Integer, primary_key=True)
    ability_bonuses = Column(Text)
    alignment = Column(String(255))
    age = Column(String(255))
    index = Column(String(255))
    language_desc = Column(Text)
    language_options = Column(Text)
    languages = Column(Text)
    name = Column(String(255))
    size = Column(String(255))
    size_description = Column(Text)
    speed = Column(Integer)
    starting_proficiencies = Column(Text)
    starting_proficiency_options = Column(Text)
    subraces = Column(Text)
    traits = Column(Text)
    url = Column(String(255))
    def __repr__(self): return f"<Races {self.id}>"

class RuleSections(Base):
    __tablename__ = 'rule_sections'
    id = Column(Integer, primary_key=True)
    index = Column(String(255))
    name = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<RuleSections {self.id}>"

class Rules(Base):
    __tablename__ = 'rules'
    id = Column(Integer, primary_key=True)
    desc = Column(Text)
    index = Column(String(255))
    name = Column(String(255))
    subsections = Column(Text)
    url = Column(String(255))
    def __repr__(self): return f"<Rules {self.id}>"
class Skills(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    desc = Column(Text)
    index = Column(String(255))
    name = Column(String(255))
    ability_score = Column(Text)
    url = Column(String(255))
    def __repr__(self): return f"<Skills {self.id}>"

class Spells(Base):
    __tablename__ = 'spells'
    id = Column(Integer, primary_key=True)
    area_of_effect = Column(Text)
    attack_type = Column(String(255))
    casting_time = Column(String(255))
    classes = Column(Text)
    components = Column(Text)
    concentration = Column(Boolean)
    damage = Column(Text)
    dc = Column(Text)
    desc = Column(Text)
    duration = Column(String(255))
    healing = Column(Text)
    higher_level = Column(Text)
    index = Column(String(255))
    level = Column(Integer)
    material = Column(String(255))
    name = Column(String(255))
    range = Column(String(255))
    ritual = Column(Boolean)
    saving_throw = Column(String(255))
    school = Column(Text)
    subclasses = Column(Text)
    url = Column(String(255))
    usage = Column(Text)
    def __repr__(self): return f"<Spells {self.id}>"

class Subclasses(Base):
    __tablename__ = 'subclasses'
    id = Column(Integer, primary_key=True)
    class_ = Column(String(255))
    index = Column(String(255))
    name = Column(String(255))
    spells = Column(Text)
    subclass_flavor = Column(String(255))
    subclass_levels = Column(Text)
    url = Column(String(255))
    def __repr__(self): return f"<Subclasses {self.id}>"

class Subraces(Base):
    __tablename__ = 'subraces'
    id = Column(Integer, primary_key=True)
    index = Column(String(255))
    language_options = Column(Text)
    name = Column(String(255))
    race = Column(Text)
    racial_traits = Column(Text)
    starting_proficiencies = Column(Text)
    url = Column(String(255))
    def __repr__(self): return f"<Subraces {self.id}>"

class Traits(Base):
    __tablename__ = 'traits'
    id = Column(Integer, primary_key=True)
    desc = Column(Text)
    index = Column(String(255))
    name = Column(String(255))
    proficiencies = Column(Text)
    races = Column(Text)
    subraces = Column(Text)
    url = Column(String(255))
    def __repr__(self): return f"<Traits {self.id}>"

class WeaponProperties(Base):
    __tablename__ = 'weapon_properties'
    id = Column(Integer, primary_key=True)
    desc = Column(Text)
    index = Column(String(255))
    name = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<WeaponProperties {self.id}>"

class Levels(Base):
    __tablename__ = 'levels'
    id = Column(Integer, primary_key=True)
    index = Column(String(255))
    class_ = Column(String(255))
    level = Column(Integer)
    ability_score_bonuses = Column(Integer)
    prof_bonus = Column(Integer)
    features = Column(Text)
    spellcasting = Column(Text)
    subclass = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<Levels {self.id}>"
