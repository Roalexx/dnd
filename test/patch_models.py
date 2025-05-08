from sqlalchemy import Column, Integer, String, Boolean, Text
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

class Backgrounds(Base):
    __tablename__ = 'backgrounds'
    id = Column(Integer, primary_key=True)
    index = Column(String(255))
    language_options = Column(String(255))
    name = Column(String(255))
    starting_equipment = Column(String(255))
    starting_equipment_options = Column(String(255))
    starting_proficiencies = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<Backgrounds {self.id}>"

class Classes(Base):
    __tablename__ = 'classes'
    id = Column(Integer, primary_key=True)
    class_levels = Column(String(255))
    hit_die = Column(Integer)
    index = Column(String(255))
    multi_classing = Column(String(255))
    name = Column(String(255))
    proficiency_choices = Column(String(255))
    proficiencies = Column(String(255))
    saving_throws = Column(String(255))
    starting_equipment = Column(String(255))
    starting_equipment_options = Column(String(255))
    subclasses = Column(String(255))
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
    cost = Column(String(255))
    damage = Column(String(255))
    desc = Column(Text)
    equipment_category = Column(String(255))
    gear_category = Column(String(255))
    index = Column(String(255))
    name = Column(String(255))
    properties = Column(String(255))
    range = Column(String(255))
    special = Column(String(255))
    speed = Column(String(255))
    stealth_disadvantage = Column(Boolean)
    str_minimum = Column(Integer)
    throw_range = Column(String(255))
    tool_category = Column(String(255))
    two_handed_damage = Column(String(255))
    url = Column(String(255))
    vehicle_category = Column(String(255))
    weight = Column(String(255))
    weapon_category = Column(String(255))
    weapon_range = Column(String(255))
    weapon_range_type = Column(String(255))
    def __repr__(self): return f"<Equipment {self.id}>"

class EquipmentCategories(Base):
    __tablename__ = 'equipment_categories'
    id = Column(Integer, primary_key=True)
    equipment = Column(String(255))
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
    prerequisites = Column(String(255))
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
    prerequisites = Column(String(255))
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
    equipment_category = Column(String(255))
    index = Column(String(255))
    name = Column(String(255))
    rarity = Column(String(255))
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
    actions = Column(String(255))
    alignment = Column(String(255))
    armor_class = Column(String(255))
    challenge_rating = Column(String(255))
    charisma = Column(Integer)
    condition_immunities = Column(String(255))
    constitution = Column(Integer)
    damage_immunities = Column(String(255))
    damage_resistances = Column(String(255))
    damage_vulnerabilities = Column(String(255))
    dexterity = Column(Integer)
    forms = Column(String(255))
    hit_dice = Column(String(255))
    hit_points = Column(Integer)
    index = Column(String(255))
    intelligence = Column(Integer)
    languages = Column(String(255))
    legendary_actions = Column(String(255))
    legendary_desc = Column(Text)
    name = Column(String(255))
    proficiencies = Column(String(255))
    reactions = Column(String(255))
    senses = Column(String(255))
    size = Column(String(255))
    special_abilities = Column(String(255))
    speed = Column(String(255))
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
    references = Column(String(255))
    type = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<Proficiencies {self.id}>"

class Races(Base):
    __tablename__ = 'races'
    id = Column(Integer, primary_key=True)
    ability_bonuses = Column(String(255))
    alignment = Column(String(255))
    age = Column(String(255))
    index = Column(String(255))
    language_desc = Column(Text)
    language_options = Column(String(255))
    languages = Column(String(255))
    name = Column(String(255))
    size = Column(String(255))
    size_description = Column(Text)
    speed = Column(Integer)
    starting_proficiencies = Column(String(255))
    starting_proficiency_options = Column(String(255))
    subraces = Column(String(255))
    traits = Column(String(255))
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
    subsections = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<Rules {self.id}>"

class Skills(Base):
    __tablename__ = 'skills'
    id = Column(Integer, primary_key=True)
    desc = Column(Text)
    index = Column(String(255))
    name = Column(String(255))
    ability_score = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<Skills {self.id}>"

class Spells(Base):
    __tablename__ = 'spells'
    id = Column(Integer, primary_key=True)
    area_of_effect = Column(String(255))
    attack_type = Column(String(255))
    casting_time = Column(String(255))
    classes = Column(String(255))
    components = Column(String(255))
    concentration = Column(Boolean)
    damage = Column(String(255))
    dc = Column(String(255))
    desc = Column(Text)
    duration = Column(String(255))
    healing = Column(String(255))
    higher_level = Column(Text)
    index = Column(String(255))
    level = Column(Integer)
    material = Column(String(255))
    name = Column(String(255))
    range = Column(String(255))
    ritual = Column(Boolean)
    saving_throw = Column(String(255))
    school = Column(String(255))
    subclasses = Column(String(255))
    url = Column(String(255))
    usage = Column(String(255))
    def __repr__(self): return f"<Spells {self.id}>"

class Subclasses(Base):
    __tablename__ = 'subclasses'
    id = Column(Integer, primary_key=True)
    class_ = Column(String(255))
    index = Column(String(255))
    name = Column(String(255))
    spells = Column(String(255))
    subclass_flavor = Column(String(255))
    subclass_levels = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<Subclasses {self.id}>"

class Subraces(Base):
    __tablename__ = 'subraces'
    id = Column(Integer, primary_key=True)
    index = Column(String(255))
    language_options = Column(String(255))
    name = Column(String(255))
    race = Column(String(255))
    racial_traits = Column(String(255))
    starting_proficiencies = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<Subraces {self.id}>"

class Traits(Base):
    __tablename__ = 'traits'
    id = Column(Integer, primary_key=True)
    desc = Column(Text)
    index = Column(String(255))
    name = Column(String(255))
    proficiencies = Column(String(255))
    races = Column(String(255))
    subraces = Column(String(255))
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

class Damage(Base):
    __tablename__ = 'damage'
    id = Column(Integer, primary_key=True)
    damage_dice = Column(String(255))
    damage_type = Column(String(255))
    def __repr__(self): return f"<Damage {self.id}>"

class GearCategory(Base):
    __tablename__ = 'gear_category'
    id = Column(Integer, primary_key=True)
    index = Column(String(255))
    name = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<GearCategory {self.id}>"

class StartingProficiencies(Base):
    __tablename__ = 'starting_proficiencies'
    id = Column(Integer, primary_key=True)
    index = Column(String(255))
    name = Column(String(255))
    type = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<StartingProficiencies {self.id}>"

class StartingEquipmentOptions(Base):
    __tablename__ = 'starting_equipment_options'
    id = Column(Integer, primary_key=True)
    desc = Column(Text)
    choose = Column(Integer)
    from_ = Column(String(255))
    url = Column(String(255))
    def __repr__(self): return f"<StartingEquipmentOptions {self.id}>"

class ThrowRange(Base):
    __tablename__ = 'throw_range'
    id = Column(Integer, primary_key=True)
    normal = Column(Integer)
    long = Column(Integer)
    def __repr__(self): return f"<ThrowRange {self.id}>"

class TwoHandedDamage(Base):
    __tablename__ = 'two_handed_damage'
    id = Column(Integer, primary_key=True)
    damage_dice = Column(String(255))
    damage_type = Column(String(255))
    def __repr__(self): return f"<TwoHandedDamage {self.id}>"

class Range(Base):
    __tablename__ = 'range'
    id = Column(Integer, primary_key=True)
    long = Column(Integer)
    normal = Column(Integer)
    def __repr__(self): return f"<Range {self.id}>"

class Speed(Base):
    __tablename__ = 'speed'
    id = Column(Integer, primary_key=True)
    burrow = Column(String(255))
    climb = Column(String(255))
    fly = Column(String(255))
    hover = Column(Boolean)
    swim = Column(String(255))
    walk = Column(String(255))
    def __repr__(self): return f"<Speed {self.id}>"

class Weight(Base):
    __tablename__ = 'weight'
    id = Column(Integer, primary_key=True)
    weight = Column(Integer)
    def __repr__(self): return f"<Weight {self.id}>"

class Multiclassing(Base):
    __tablename__ = 'multiclassing'
    id = Column(Integer, primary_key=True)
    prerequisites = Column(String(255))
    proficiency_choices = Column(String(255))
    proficiencies = Column(String(255))
    def __repr__(self): return f"<Multiclassing {self.id}>"

class Reactions(Base):
    __tablename__ = 'reactions'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    desc = Column(Text)
    def __repr__(self): return f"<Reactions {self.id}>"

class LegendaryActions(Base):
    __tablename__ = 'legendary_actions'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    desc = Column(Text)
    def __repr__(self): return f"<LegendaryActions {self.id}>"

class Actions(Base):
    __tablename__ = 'actions'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    desc = Column(Text)
    def __repr__(self): return f"<Actions {self.id}>"

class SpecialAbilities(Base):
    __tablename__ = 'special_abilities'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    desc = Column(Text)
    def __repr__(self): return f"<SpecialAbilities {self.id}>"

class SpecialAbilitiesDesc(Base):
    __tablename__ = 'special_abilities_desc'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    desc = Column(Text)
    def __repr__(self): return f"<SpecialAbilitiesDesc {self.id}>"

class SensesDetail(Base):
    __tablename__ = 'senses_detail'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    desc = Column(Text)
    def __repr__(self): return f"<SensesDetail {self.id}>"
