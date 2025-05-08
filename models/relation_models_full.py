from sqlalchemy import Column, Integer, ForeignKey
from models import Base

class AbilityScoresSkills(Base):
    __tablename__ = 'ability_scores_skills'
    id = Column(Integer, primary_key=True)
    ability_scores_id = Column(Integer, ForeignKey('ability_scores.id'))
    skills_id = Column(Integer, ForeignKey('skills.id'))
    def __repr__(self): return f"<AbilityScoresSkills {self.id}>"

class BackgroundsEquipment(Base):
    __tablename__ = 'backgrounds_equipment'
    id = Column(Integer, primary_key=True)
    backgrounds_id = Column(Integer, ForeignKey('backgrounds.id'))
    equipment_id = Column(Integer, ForeignKey('equipment.id'))
    def __repr__(self): return f"<BackgroundsEquipment {self.id}>"

class BackgroundsFromEquipmentCategory(Base):
    __tablename__ = 'backgrounds_from_equipment_category'
    id = Column(Integer, primary_key=True)
    backgrounds_id = Column(Integer, ForeignKey('backgrounds.id'))
    equipment_categories_id = Column(Integer, ForeignKey('equipment_categories.id'))
    def __repr__(self): return f"<BackgroundsFromEquipmentCategory {self.id}>"

class BackgroundsFromOptionsAlignments(Base):
    __tablename__ = 'backgrounds_from_options_alignments'
    id = Column(Integer, primary_key=True)
    backgrounds_id = Column(Integer, ForeignKey('backgrounds.id'))
    alignments_id = Column(Integer, ForeignKey('alignments.id'))
    def __repr__(self): return f"<BackgroundsFromOptionsAlignments {self.id}>"

class BackgroundsStartingProficiencies(Base):
    __tablename__ = 'backgrounds_starting_proficiencies'
    id = Column(Integer, primary_key=True)
    backgrounds_id = Column(Integer, ForeignKey('backgrounds.id'))
    proficiencies_id = Column(Integer, ForeignKey('proficiencies.id'))
    def __repr__(self): return f"<BackgroundsStartingProficiencies {self.id}>"

class ClassesEquipment(Base):
    __tablename__ = 'classes_equipment'
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer, ForeignKey('classes.id'))
    equipment_id = Column(Integer, ForeignKey('equipment.id'))
    def __repr__(self): return f"<ClassesEquipment {self.id}>"

class ClassesFromOptionsChoiceFromEquipmentCategory(Base):
    __tablename__ = 'classes_from_options_choice_from_equipment_category'
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer, ForeignKey('classes.id'))
    equipment_categories_id = Column(Integer, ForeignKey('equipment_categories.id'))
    def __repr__(self): return f"<ClassesFromOptionsChoiceFromEquipmentCategory {self.id}>"

class ClassesFromOptionsItem(Base):
    __tablename__ = 'classes_from_options_item'
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer, ForeignKey('classes.id'))
    proficiencies_id = Column(Integer, ForeignKey('proficiencies.id'))
    def __repr__(self): return f"<ClassesFromOptionsItem {self.id}>"

class ClassesFromOptionsOf(Base):
    __tablename__ = 'classes_from_options_of'
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer, ForeignKey('classes.id'))
    equipment_id = Column(Integer, ForeignKey('equipment.id'))
    def __repr__(self): return f"<ClassesFromOptionsOf {self.id}>"

class ClassesPrerequisitesAbilityScore(Base):
    __tablename__ = 'classes_prerequisites_ability_score'
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer, ForeignKey('classes.id'))
    ability_scores_id = Column(Integer, ForeignKey('ability_scores.id'))
    def __repr__(self): return f"<ClassesPrerequisitesAbilityScore {self.id}>"

class ClassesProficiencies(Base):
    __tablename__ = 'classes_proficiencies'
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer, ForeignKey('classes.id'))
    proficiencies_id = Column(Integer, ForeignKey('proficiencies.id'))
    def __repr__(self): return f"<ClassesProficiencies {self.id}>"

class ClassesSavingThrows(Base):
    __tablename__ = 'classes_saving_throws'
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer, ForeignKey('classes.id'))
    ability_scores_id = Column(Integer, ForeignKey('ability_scores.id'))
    def __repr__(self): return f"<ClassesSavingThrows {self.id}>"

class ClassesSubclasses(Base):
    __tablename__ = 'classes_subclasses'
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer, ForeignKey('classes.id'))
    subclasses_id = Column(Integer, ForeignKey('subclasses.id'))
    def __repr__(self): return f"<ClassesSubclasses {self.id}>"

class EquipmentDamageType(Base):
    __tablename__ = 'equipment_damage_type'
    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer, ForeignKey('equipment.id'))
    damage_types_id = Column(Integer, ForeignKey('damage_types.id'))
    def __repr__(self): return f"<EquipmentDamageType {self.id}>"

class EquipmentEquipmentCategory(Base):
    __tablename__ = 'equipment_equipment_category'
    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer, ForeignKey('equipment.id'))
    equipment_categories_id = Column(Integer, ForeignKey('equipment_categories.id'))
    def __repr__(self): return f"<EquipmentEquipmentCategory {self.id}>"

class EquipmentProperties(Base):
    __tablename__ = 'equipment_properties'
    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer, ForeignKey('equipment.id'))
    weapon_properties_id = Column(Integer, ForeignKey('weapon_properties.id'))
    def __repr__(self): return f"<EquipmentProperties {self.id}>"

class EquipmentCategoriesEquipment(Base):
    __tablename__ = 'equipment_categories_equipment'
    id = Column(Integer, primary_key=True)
    equipment_categories_id = Column(Integer, ForeignKey('equipment_categories.id'))
    equipment_id = Column(Integer, ForeignKey('equipment.id'))
    def __repr__(self): return f"<EquipmentCategoriesEquipment {self.id}>"

class FeatsAbilityScore(Base):
    __tablename__ = 'feats_ability_score'
    id = Column(Integer, primary_key=True)
    feats_id = Column(Integer, ForeignKey('feats.id'))
    ability_scores_id = Column(Integer, ForeignKey('ability_scores.id'))
    def __repr__(self): return f"<FeatsAbilityScore {self.id}>"

class FeaturesClass(Base):
    __tablename__ = 'features_class'
    id = Column(Integer, primary_key=True)
    features_id = Column(Integer, ForeignKey('features.id'))
    classes_id = Column(Integer, ForeignKey('classes.id'))
    def __repr__(self): return f"<FeaturesClass {self.id}>"

class LevelsClass(Base):
    __tablename__ = 'levels_class'
    id = Column(Integer, primary_key=True)
    levels_id = Column(Integer, ForeignKey('levels.id'))
    classes_id = Column(Integer, ForeignKey('classes.id'))
    def __repr__(self): return f"<LevelsClass {self.id}>"

class LevelsFeatures(Base):
    __tablename__ = 'levels_features'
    id = Column(Integer, primary_key=True)
    levels_id = Column(Integer, ForeignKey('levels.id'))
    features_id = Column(Integer, ForeignKey('features.id'))
    def __repr__(self): return f"<LevelsFeatures {self.id}>"

class MagicItemsEquipmentCategory(Base):
    __tablename__ = 'magic_items_equipment_category'
    id = Column(Integer, primary_key=True)
    magic_items_id = Column(Integer, ForeignKey('magic_items.id'))
    equipment_categories_id = Column(Integer, ForeignKey('equipment_categories.id'))
    def __repr__(self): return f"<MagicItemsEquipmentCategory {self.id}>"

class MonstersDamageDamageType(Base):
    __tablename__ = 'monsters_damage_damage_type'
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer, ForeignKey('monsters.id'))
    damage_types_id = Column(Integer, ForeignKey('damage_types.id'))
    def __repr__(self): return f"<MonstersDamageDamageType {self.id}>"

class MonstersDcDcType(Base):
    __tablename__ = 'monsters_dc_dc_type'
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer, ForeignKey('monsters.id'))
    ability_scores_id = Column(Integer, ForeignKey('ability_scores.id'))
    def __repr__(self): return f"<MonstersDcDcType {self.id}>"

class MonstersProficiency(Base):
    __tablename__ = 'monsters_proficiency'
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer, ForeignKey('monsters.id'))
    proficiencies_id = Column(Integer, ForeignKey('proficiencies.id'))
    def __repr__(self): return f"<MonstersProficiency {self.id}>"

class ProficienciesClasses(Base):
    __tablename__ = 'proficiencies_classes'
    id = Column(Integer, primary_key=True)
    proficiencies_id = Column(Integer, ForeignKey('proficiencies.id'))
    classes_id = Column(Integer, ForeignKey('classes.id'))
    def __repr__(self): return f"<ProficienciesClasses {self.id}>"

class RacesAbilityScore(Base):
    __tablename__ = 'races_ability_score'
    id = Column(Integer, primary_key=True)
    races_id = Column(Integer, ForeignKey('races.id'))
    ability_scores_id = Column(Integer, ForeignKey('ability_scores.id'))
    def __repr__(self): return f"<RacesAbilityScore {self.id}>"

class RacesFromOptionsItem(Base):
    __tablename__ = 'races_from_options_item'
    id = Column(Integer, primary_key=True)
    races_id = Column(Integer, ForeignKey('races.id'))
    proficiencies_id = Column(Integer, ForeignKey('proficiencies.id'))
    def __repr__(self): return f"<RacesFromOptionsItem {self.id}>"

class RacesLanguages(Base):
    __tablename__ = 'races_languages'
    id = Column(Integer, primary_key=True)
    races_id = Column(Integer, ForeignKey('races.id'))
    languages_id = Column(Integer, ForeignKey('languages.id'))
    def __repr__(self): return f"<RacesLanguages {self.id}>"

class RacesStartingProficiencies(Base):
    __tablename__ = 'races_starting_proficiencies'
    id = Column(Integer, primary_key=True)
    races_id = Column(Integer, ForeignKey('races.id'))
    proficiencies_id = Column(Integer, ForeignKey('proficiencies.id'))
    def __repr__(self): return f"<RacesStartingProficiencies {self.id}>"

class RacesSubraces(Base):
    __tablename__ = 'races_subraces'
    id = Column(Integer, primary_key=True)
    races_id = Column(Integer, ForeignKey('races.id'))
    subraces_id = Column(Integer, ForeignKey('subraces.id'))
    def __repr__(self): return f"<RacesSubraces {self.id}>"

class RacesTraits(Base):
    __tablename__ = 'races_traits'
    id = Column(Integer, primary_key=True)
    races_id = Column(Integer, ForeignKey('races.id'))
    traits_id = Column(Integer, ForeignKey('traits.id'))
    def __repr__(self): return f"<RacesTraits {self.id}>"

class RulesSubsections(Base):
    __tablename__ = 'rules_subsections'
    id = Column(Integer, primary_key=True)
    rules_id = Column(Integer, ForeignKey('rules.id'))
    rule_sections_id = Column(Integer, ForeignKey('rule_sections.id'))
    def __repr__(self): return f"<RulesSubsections {self.id}>"

class SkillsAbilityScore(Base):
    __tablename__ = 'skills_ability_score'
    id = Column(Integer, primary_key=True)
    skills_id = Column(Integer, ForeignKey('skills.id'))
    ability_scores_id = Column(Integer, ForeignKey('ability_scores.id'))
    def __repr__(self): return f"<SkillsAbilityScore {self.id}>"

class SpellsClasses(Base):
    __tablename__ = 'spells_classes'
    id = Column(Integer, primary_key=True)
    spells_id = Column(Integer, ForeignKey('spells.id'))
    classes_id = Column(Integer, ForeignKey('classes.id'))
    def __repr__(self): return f"<SpellsClasses {self.id}>"

class SpellsDamageType(Base):
    __tablename__ = 'spells_damage_type'
    id = Column(Integer, primary_key=True)
    spells_id = Column(Integer, ForeignKey('spells.id'))
    damage_types_id = Column(Integer, ForeignKey('damage_types.id'))
    def __repr__(self): return f"<SpellsDamageType {self.id}>"

class SpellsSchool(Base):
    __tablename__ = 'spells_school'
    id = Column(Integer, primary_key=True)
    spells_id = Column(Integer, ForeignKey('spells.id'))
    magic_schools_id = Column(Integer, ForeignKey('magic_schools.id'))
    def __repr__(self): return f"<SpellsSchool {self.id}>"

class SpellsSubclasses(Base):
    __tablename__ = 'spells_subclasses'
    id = Column(Integer, primary_key=True)
    spells_id = Column(Integer, ForeignKey('spells.id'))
    subclasses_id = Column(Integer, ForeignKey('subclasses.id'))
    def __repr__(self): return f"<SpellsSubclasses {self.id}>"

class SubclassesClass(Base):
    __tablename__ = 'subclasses_class'
    id = Column(Integer, primary_key=True)
    subclasses_id = Column(Integer, ForeignKey('subclasses.id'))
    classes_id = Column(Integer, ForeignKey('classes.id'))
    def __repr__(self): return f"<SubclassesClass {self.id}>"

class SubracesAbilityScore(Base):
    __tablename__ = 'subraces_ability_score'
    id = Column(Integer, primary_key=True)
    subraces_id = Column(Integer, ForeignKey('subraces.id'))
    ability_scores_id = Column(Integer, ForeignKey('ability_scores.id'))
    def __repr__(self): return f"<SubracesAbilityScore {self.id}>"

class SubracesRace(Base):
    __tablename__ = 'subraces_race'
    id = Column(Integer, primary_key=True)
    subraces_id = Column(Integer, ForeignKey('subraces.id'))
    races_id = Column(Integer, ForeignKey('races.id'))
    def __repr__(self): return f"<SubracesRace {self.id}>"

class SubracesRacialTraits(Base):
    __tablename__ = 'subraces_racial_traits'
    id = Column(Integer, primary_key=True)
    subraces_id = Column(Integer, ForeignKey('subraces.id'))
    traits_id = Column(Integer, ForeignKey('traits.id'))
    def __repr__(self): return f"<SubracesRacialTraits {self.id}>"

class TraitsRaces(Base):
    __tablename__ = 'traits_races'
    id = Column(Integer, primary_key=True)
    traits_id = Column(Integer, ForeignKey('traits.id'))
    races_id = Column(Integer, ForeignKey('races.id'))
    def __repr__(self): return f"<TraitsRaces {self.id}>"



class SpellsConditions(Base):
    __tablename__ = 'spells_conditions'
    id = Column(Integer, primary_key=True)
    spells_id = Column(Integer, ForeignKey('spells.id'))
    conditions_id = Column(Integer, ForeignKey('conditions.id'))
    def __repr__(self): return f"<SpellsConditions {self.id}>"

class MonstersConditionImmunities(Base):
    __tablename__ = 'monsters_condition_immunities'
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer, ForeignKey('monsters.id'))
    conditions_id = Column(Integer, ForeignKey('conditions.id'))
    def __repr__(self): return f"<MonstersConditionImmunities {self.id}>"
