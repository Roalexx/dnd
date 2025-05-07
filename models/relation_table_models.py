from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AbilityScoresDescriptions(Base):
    __tablename__ = "ability_scores_descriptions"
    id = Column(Integer, primary_key=True)
    ability_scores_id = Column(Integer)
    descriptions_id = Column(Integer)

class AbilityScoresSkills(Base):
    __tablename__ = "ability_scores_skills"
    id = Column(Integer, primary_key=True)
    ability_scores_id = Column(Integer)
    skills_id = Column(Integer)

class BackgroundsStartingEquipmentOptions(Base):
    __tablename__ = "backgrounds_starting_equipment_options"
    id = Column(Integer, primary_key=True)
    backgrounds_id = Column(Integer)
    starting_equipment_options_id = Column(Integer)

class BackgroundsStartingEquipments(Base):
    __tablename__ = "backgrounds_starting_equipments"
    id = Column(Integer, primary_key=True)
    backgrounds_id = Column(Integer)
    starting_equipments_id = Column(Integer)

class BackgroundsStartingProficiencies(Base):
    __tablename__ = "backgrounds_starting_proficiencies"
    id = Column(Integer, primary_key=True)
    backgrounds_id = Column(Integer)
    starting_proficiencies_id = Column(Integer)

class ClassesFeatures(Base):
    __tablename__ = "classes_features"
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer)
    features_id = Column(Integer)

class ClassesProficiencies(Base):
    __tablename__ = "classes_proficiencies"
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer)
    proficiencies_id = Column(Integer)

class ClassesProficiencyChoices(Base):
    __tablename__ = "classes_proficiency_choices"
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer)
    proficiency_choices_id = Column(Integer)

class ClassesSavingThrows(Base):
    __tablename__ = "classes_saving_throws"
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer)
    saving_throws_id = Column(Integer)

class ClassesStartingEquipmentOptions(Base):
    __tablename__ = "classes_starting_equipment_options"
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer)
    starting_equipment_options_id = Column(Integer)

class ClassesStartingEquipments(Base):
    __tablename__ = "classes_starting_equipments"
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer)
    starting_equipments_id = Column(Integer)

class ConditionsDescendingConditions(Base):
    __tablename__ = "conditions_descending_conditions"
    id = Column(Integer, primary_key=True)
    conditions_id = Column(Integer)
    descending_conditions_id = Column(Integer)

class EquipmentProperties(Base):
    __tablename__ = "equipment_properties"
    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer)
    properties_id = Column(Integer)

class EquipmentWeaponRange(Base):
    __tablename__ = "equipment_weapon_range"
    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer)
    weapon_range_id = Column(Integer)

class FeaturesPrerequisiteOptions(Base):
    __tablename__ = "features_prerequisite_options"
    id = Column(Integer, primary_key=True)
    features_id = Column(Integer)
    prerequisite_options_id = Column(Integer)

class FeatsPrerequisites(Base):
    __tablename__ = "feats_prerequisites"
    id = Column(Integer, primary_key=True)
    feats_id = Column(Integer)
    prerequisites_id = Column(Integer)

class MonstersDamageTypes(Base):
    __tablename__ = "monsters_damage_types"
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer)
    damage_types_id = Column(Integer)

class MonstersProficiencies(Base):
    __tablename__ = "monsters_proficiencies"
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer)
    proficiencies_id = Column(Integer)

class MonstersSenses(Base):
    __tablename__ = "monsters_senses"
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer)
    senses_id = Column(Integer)

class MonstersSpeed(Base):
    __tablename__ = "monsters_speed"
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer)
    speed_id = Column(Integer)

class RacesAbilityBonuses(Base):
    __tablename__ = "races_ability_bonuses"
    id = Column(Integer, primary_key=True)
    races_id = Column(Integer)
    ability_bonuses_id = Column(Integer)

class RacesLanguages(Base):
    __tablename__ = "races_languages"
    id = Column(Integer, primary_key=True)
    races_id = Column(Integer)
    languages_id = Column(Integer)

class RacesTraits(Base):
    __tablename__ = "races_traits"
    id = Column(Integer, primary_key=True)
    races_id = Column(Integer)
    traits_id = Column(Integer)

class SpellsAreasOfEffect(Base):
    __tablename__ = "spells_areas_of_effect"
    id = Column(Integer, primary_key=True)
    spells_id = Column(Integer)
    areas_of_effect_id = Column(Integer)

class SpellsClasses(Base):
    __tablename__ = "spells_classes"
    id = Column(Integer, primary_key=True)
    spells_id = Column(Integer)
    classes_id = Column(Integer)

class SpellsComponents(Base):
    __tablename__ = "spells_components"
    id = Column(Integer, primary_key=True)
    spells_id = Column(Integer)
    components_id = Column(Integer)

class SpellsDamageTypes(Base):
    __tablename__ = "spells_damage_types"
    id = Column(Integer, primary_key=True)
    spells_id = Column(Integer)
    damage_types_id = Column(Integer)

class SpellsHealing(Base):
    __tablename__ = "spells_healing"
    id = Column(Integer, primary_key=True)
    spells_id = Column(Integer)
    healing_id = Column(Integer)

class SpellsSchool(Base):
    __tablename__ = "spells_school"
    id = Column(Integer, primary_key=True)
    spells_id = Column(Integer)
    school_id = Column(Integer)

class SpellsSubclasses(Base):
    __tablename__ = "spells_subclasses"
    id = Column(Integer, primary_key=True)
    spells_id = Column(Integer)
    subclasses_id = Column(Integer)

class SpellsUsage(Base):
    __tablename__ = "spells_usage"
    id = Column(Integer, primary_key=True)
    spells_id = Column(Integer)
    usage_id = Column(Integer)

class SubclassesFeatures(Base):
    __tablename__ = "subclasses_features"
    id = Column(Integer, primary_key=True)
    subclasses_id = Column(Integer)
    features_id = Column(Integer)

class SubracesAbilityBonuses(Base):
    __tablename__ = "subraces_ability_bonuses"
    id = Column(Integer, primary_key=True)
    subraces_id = Column(Integer)
    ability_bonuses_id = Column(Integer)

class SubracesLanguages(Base):
    __tablename__ = "subraces_languages"
    id = Column(Integer, primary_key=True)
    subraces_id = Column(Integer)
    languages_id = Column(Integer)

class SubracesTraits(Base):
    __tablename__ = "subraces_traits"
    id = Column(Integer, primary_key=True)
    subraces_id = Column(Integer)
    traits_id = Column(Integer)

class TraitsDescendingTraits(Base):
    __tablename__ = "traits_descending_traits"
    id = Column(Integer, primary_key=True)
    traits_id = Column(Integer)
    descending_traits_id = Column(Integer)

class WeaponCategoriesWeapons(Base):
    __tablename__ = "weapon_categories_weapons"
    id = Column(Integer, primary_key=True)
    weapon_categories_id = Column(Integer)
    weapons_id = Column(Integer)

class MagicItemsDescendingMagicItems(Base):
    __tablename__ = "magic_items_descending_magic_items"
    id = Column(Integer, primary_key=True)
    magic_items_id = Column(Integer)
    descending_magic_items_id = Column(Integer)

class MagicItemsEquipmentCategories(Base):
    __tablename__ = "magic_items_equipment_categories"
    id = Column(Integer, primary_key=True)
    magic_items_id = Column(Integer)
    equipment_categories_id = Column(Integer)

class FeatsDescendingFeats(Base):
    __tablename__ = "feats_descending_feats"
    id = Column(Integer, primary_key=True)
    feats_id = Column(Integer)
    descending_feats_id = Column(Integer)

class ClassesSubclasses(Base):
    __tablename__ = "classes_subclasses"
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer)
    subclasses_id = Column(Integer)

class SpellsDescendingSpells(Base):
    __tablename__ = "spells_descending_spells"
    id = Column(Integer, primary_key=True)
    spells_id = Column(Integer)
    descending_spells_id = Column(Integer)

class ClassesMulticlassing(Base):
    __tablename__ = "classes_multiclassing"
    id = Column(Integer, primary_key=True)
    classes_id = Column(Integer)
    multiclassing_id = Column(Integer)

class MonstersSpecialAbilities(Base):
    __tablename__ = "monsters_special_abilities"
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer)
    special_abilities_id = Column(Integer)

class MonstersProficiencyChoices(Base):
    __tablename__ = "monsters_proficiency_choices"
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer)
    proficiency_choices_id = Column(Integer)

class EquipmentEquipmentCategory(Base):
    __tablename__ = "equipment_equipment_category"
    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer)
    equipment_category_id = Column(Integer)

class EquipmentGearCategory(Base):
    __tablename__ = "equipment_gear_category"
    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer)
    gear_category_id = Column(Integer)

class EquipmentDamage(Base):
    __tablename__ = "equipment_damage"
    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer)
    damage_id = Column(Integer)

class EquipmentThrowRange(Base):
    __tablename__ = "equipment_throw_range"
    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer)
    throw_range_id = Column(Integer)

class EquipmentTwoHandedDamage(Base):
    __tablename__ = "equipment_two_handed_damage"
    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer)
    two_handed_damage_id = Column(Integer)

class EquipmentRange(Base):
    __tablename__ = "equipment_range"
    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer)
    range_id = Column(Integer)

class EquipmentWeight(Base):
    __tablename__ = "equipment_weight"
    id = Column(Integer, primary_key=True)
    equipment_id = Column(Integer)
    weight_id = Column(Integer)

class MonstersConditionImmunities(Base):
    __tablename__ = "monsters_condition_immunities"
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer)
    condition_immunities_id = Column(Integer)

class MonstersDamageImmunities(Base):
    __tablename__ = "monsters_damage_immunities"
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer)
    damage_immunities_id = Column(Integer)

class MonstersDamageResistances(Base):
    __tablename__ = "monsters_damage_resistances"
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer)
    damage_resistances_id = Column(Integer)

class MonstersDamageVulnerabilities(Base):
    __tablename__ = "monsters_damage_vulnerabilities"
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer)
    damage_vulnerabilities_id = Column(Integer)

class MonstersLanguages(Base):
    __tablename__ = "monsters_languages"
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer)
    languages_id = Column(Integer)

class MonstersReactions(Base):
    __tablename__ = "monsters_reactions"
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer)
    reactions_id = Column(Integer)

class MonstersLegendaryActions(Base):
    __tablename__ = "monsters_legendary_actions"
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer)
    legendary_actions_id = Column(Integer)

class MonstersActions(Base):
    __tablename__ = "monsters_actions"
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer)
    actions_id = Column(Integer)

class MonstersSpecialAbilitiesDesc(Base):
    __tablename__ = "monsters_special_abilities_desc"
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer)
    special_abilities_desc_id = Column(Integer)

class MonstersSavingThrows(Base):
    __tablename__ = "monsters_saving_throws"
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer)
    saving_throws_id = Column(Integer)

class MonstersSensesDetail(Base):
    __tablename__ = "monsters_senses_detail"
    id = Column(Integer, primary_key=True)
    monsters_id = Column(Integer)
    senses_detail_id = Column(Integer)
