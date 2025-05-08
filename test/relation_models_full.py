from sqlalchemy import Column, Integer, ForeignKey
from models import Base


class BackgroundsStarting_proficiencies(Base):
    __tablename__ = 'backgrounds_starting_proficiencies'
    id = Column(Integer, primary_key=True)
    backgrounds_id = Column(Integer, ForeignKey('backgrounds.id'))
    proficiencies_id = Column(Integer, ForeignKey('proficiencies.id'))
    def __repr__(self): return f"<BackgroundsStarting_proficiencies {self.id}>"

class ClassesProficiencies(Base):
    __tablename__ = 'classes_proficiencies'
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer, ForeignKey('classes.id'))
    proficiencies_id = Column(Integer, ForeignKey('proficiencies.id'))
    def __repr__(self): return f"<ClassesProficiencies {self.id}>"

class ClassesSaving_throws(Base):
    __tablename__ = 'classes_saving_throws'
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer, ForeignKey('classes.id'))
    ability_scores_id = Column(Integer, ForeignKey('ability_scores.id'))
    def __repr__(self): return f"<ClassesSaving_throws {self.id}>"

class EquipmentProperties(Base):
    __tablename__ = 'equipment_properties'
    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer, ForeignKey('equipment.id'))
    weapon_properties_id = Column(Integer, ForeignKey('weapon_properties.id'))
    def __repr__(self): return f"<EquipmentProperties {self.id}>"

class FeaturesPrerequisites(Base):
    __tablename__ = 'features_prerequisites'
    id = Column(Integer, primary_key=True)
    features_id = Column(Integer, ForeignKey('features.id'))
    features_id_2 = Column(Integer, ForeignKey('features.id'))
    def __repr__(self): return f"<FeaturesPrerequisites {self.id}>"

class Magic_itemsEquipment_category(Base):
    __tablename__ = 'magic_items_equipment_category'
    id = Column(Integer, primary_key=True)
    magic_items_id = Column(Integer, ForeignKey('magic_items.id'))
    equipment_categories_id = Column(Integer, ForeignKey('equipment_categories.id'))
    def __repr__(self): return f"<Magic_itemsEquipment_category {self.id}>"

class MonstersDamage_immunities(Base):
    __tablename__ = 'monsters_damage_immunities'
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer, ForeignKey('monsters.id'))
    damage_types_id = Column(Integer, ForeignKey('damage_types.id'))
    def __repr__(self): return f"<MonstersDamage_immunities {self.id}>"

class MonstersDamage_resistances(Base):
    __tablename__ = 'monsters_damage_resistances'
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer, ForeignKey('monsters.id'))
    damage_types_id = Column(Integer, ForeignKey('damage_types.id'))
    def __repr__(self): return f"<MonstersDamage_resistances {self.id}>"

class MonstersDamage_vulnerabilities(Base):
    __tablename__ = 'monsters_damage_vulnerabilities'
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer, ForeignKey('monsters.id'))
    damage_types_id = Column(Integer, ForeignKey('damage_types.id'))
    def __repr__(self): return f"<MonstersDamage_vulnerabilities {self.id}>"

class MonstersProficiencies(Base):
    __tablename__ = 'monsters_proficiencies'
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer, ForeignKey('monsters.id'))
    proficiencies_id = Column(Integer, ForeignKey('proficiencies.id'))
    def __repr__(self): return f"<MonstersProficiencies {self.id}>"
class RacesLanguages(Base):
    __tablename__ = 'races_languages'
    id = Column(Integer, primary_key=True)
    races_id = Column(Integer, ForeignKey('races.id'))
    languages_id = Column(Integer, ForeignKey('languages.id'))
    def __repr__(self): return f"<RacesLanguages {self.id}>"

class RacesTraits(Base):
    __tablename__ = 'races_traits'
    id = Column(Integer, primary_key=True)
    races_id = Column(Integer, ForeignKey('races.id'))
    traits_id = Column(Integer, ForeignKey('traits.id'))
    def __repr__(self): return f"<RacesTraits {self.id}>"

class SpellsClasses(Base):
    __tablename__ = 'spells_classes'
    id = Column(Integer, primary_key=True)
    spells_id = Column(Integer, ForeignKey('spells.id'))
    classes_id = Column(Integer, ForeignKey('classes.id'))
    def __repr__(self): return f"<SpellsClasses {self.id}>"

class SpellsSubclasses(Base):
    __tablename__ = 'spells_subclasses'
    id = Column(Integer, primary_key=True)
    spells_id = Column(Integer, ForeignKey('spells.id'))
    subclasses_id = Column(Integer, ForeignKey('subclasses.id'))
    def __repr__(self): return f"<SpellsSubclasses {self.id}>"

class SubracesRacial_traits(Base):
    __tablename__ = 'subraces_racial_traits'
    id = Column(Integer, primary_key=True)
    subraces_id = Column(Integer, ForeignKey('subraces.id'))
    traits_id = Column(Integer, ForeignKey('traits.id'))
    def __repr__(self): return f"<SubracesRacial_traits {self.id}>"

class TraitsProficiencies(Base):
    __tablename__ = 'traits_proficiencies'
    id = Column(Integer, primary_key=True)
    traits_id = Column(Integer, ForeignKey('traits.id'))
    proficiencies_id = Column(Integer, ForeignKey('proficiencies.id'))
    def __repr__(self): return f"<TraitsProficiencies {self.id}>"

class RacesStarting_proficiencies(Base):
    __tablename__ = 'races_starting_proficiencies'
    id = Column(Integer, primary_key=True)
    races_id = Column(Integer, ForeignKey('races.id'))
    proficiencies_id = Column(Integer, ForeignKey('proficiencies.id'))
    def __repr__(self): return f"<RacesStarting_proficiencies {self.id}>"

class SubracesStarting_proficiencies(Base):
    __tablename__ = 'subraces_starting_proficiencies'
    id = Column(Integer, primary_key=True)
    subraces_id = Column(Integer, ForeignKey('subraces.id'))
    proficiencies_id = Column(Integer, ForeignKey('proficiencies.id'))
    def __repr__(self): return f"<SubracesStarting_proficiencies {self.id}>"

class FeatsPrerequisites(Base):
    __tablename__ = 'feats_prerequisites'
    id = Column(Integer, primary_key=True)
    feats_id = Column(Integer, ForeignKey('feats.id'))
    prerequisites_id = Column(Integer, ForeignKey('features.id'))  # Assuming prerequisites are features
    def __repr__(self): return f"<FeatsPrerequisites {self.id}>"

class MagicItemsDescendingItems(Base):
    __tablename__ = 'magic_items_descending_items'
    id = Column(Integer, primary_key=True)
    magic_items_id = Column(Integer, ForeignKey('magic_items.id'))
    descending_magic_items_id = Column(Integer, ForeignKey('magic_items.id'))
    def __repr__(self): return f"<MagicItemsDescendingItems {self.id}>"
