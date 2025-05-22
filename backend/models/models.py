from typing import List, Optional
from sqlalchemy import ARRAY, Boolean, Column, Double, ForeignKeyConstraint, Identity, Integer, PrimaryKeyConstraint, Sequence, String, Table, Text, UniqueConstraint, text
from sqlalchemy.orm import  Mapped, mapped_column, relationship
from models import Base

class AbilityScores(Base):
    __tablename__ = 'ability_scores'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='ability_scores_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[Optional[str]] = mapped_column(Text)
    full_name: Mapped[Optional[str]] = mapped_column(String(255))
    name: Mapped[Optional[str]] = mapped_column(String(255))
    url: Mapped[Optional[str]] = mapped_column(String(255))

    races: Mapped[List['Races']] = relationship('Races', back_populates='ability_score')
    subraces: Mapped[List['Subraces']] = relationship('Subraces', back_populates='ability_score')
    class_multi_classing_prerequisites: Mapped[List['ClassMultiClassingPrerequisites']] = relationship('ClassMultiClassingPrerequisites', back_populates='ability_score')
    classes_saving_throws: Mapped[List['ClassesSavingThrows']] = relationship('ClassesSavingThrows', back_populates='ability_score')
    feats: Mapped[List['Feats']] = relationship('Feats', back_populates='ability_scores')
    monster_legendary_actions: Mapped[List['MonsterLegendaryActions']] = relationship('MonsterLegendaryActions', back_populates='dc_type')
    monster_reactions: Mapped[List['MonsterReactions']] = relationship('MonsterReactions', back_populates='dc_type')
    monsters_special_abilities: Mapped[List['MonstersSpecialAbilities']] = relationship('MonstersSpecialAbilities', foreign_keys='[MonstersSpecialAbilities.dc_type_id]', back_populates='dc_type')
    monsters_special_abilities_: Mapped[List['MonstersSpecialAbilities']] = relationship('MonstersSpecialAbilities', foreign_keys='[MonstersSpecialAbilities.spellcasting_ability_score_id]', back_populates='spellcasting_ability_score')
    race_ability_bonus_options: Mapped[List['RaceAbilityBonusOptions']] = relationship('RaceAbilityBonusOptions', back_populates='ability_score')
    skills: Mapped[List['Skills']] = relationship('Skills', back_populates='ability_scores')
    spells: Mapped[List['Spells']] = relationship('Spells', back_populates='dc')
    proficiencies: Mapped[List['Proficiencies']] = relationship('Proficiencies', back_populates='reference_ability_score')


class Alignments(Base):
    __tablename__ = 'alignments'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='alignments_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[Optional[str]] = mapped_column(Text)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    url: Mapped[Optional[str]] = mapped_column(String(255))


class Classes(Base):
    __tablename__ = 'classes'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='classes_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    hit_die: Mapped[Optional[int]] = mapped_column(Integer)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    url: Mapped[Optional[str]] = mapped_column(String(255))
    class_levels: Mapped[Optional[int]] = mapped_column(Integer)
    multi_classing: Mapped[Optional[int]] = mapped_column(Integer)
    proficiency_choices: Mapped[Optional[int]] = mapped_column(Integer)
    proficiencies: Mapped[Optional[int]] = mapped_column(Integer)
    saving_throws: Mapped[Optional[int]] = mapped_column(Integer)
    starting_equipment: Mapped[Optional[int]] = mapped_column(Integer)
    starting_equipment_options: Mapped[Optional[int]] = mapped_column(Integer)
    spellcasting_level: Mapped[Optional[int]] = mapped_column(Integer)
    spellcasting_ability_id: Mapped[Optional[int]] = mapped_column(Integer)
    spellcasting_name: Mapped[Optional[str]] = mapped_column(String(255))
    spellcasting_description: Mapped[Optional[str]] = mapped_column(Text)
    subclass_id: Mapped[Optional[int]] = mapped_column(Integer)
    proficiency_choices_desc: Mapped[Optional[str]] = mapped_column(Text)
    proficiency_choices_choose: Mapped[Optional[int]] = mapped_column(Integer)
    starting_equipment_options_choose: Mapped[Optional[int]] = mapped_column(Integer)
    starting_equipment_options_desc: Mapped[Optional[str]] = mapped_column(Text)

    features: Mapped[List['Features']] = relationship('Features', back_populates='class_')
    class_multi_classing_prerequisites: Mapped[List['ClassMultiClassingPrerequisites']] = relationship('ClassMultiClassingPrerequisites', back_populates='class_')
    classes_saving_throws: Mapped[List['ClassesSavingThrows']] = relationship('ClassesSavingThrows', back_populates='class_')
    subclasses: Mapped[List['Subclasses']] = relationship('Subclasses', back_populates='class_')
    classes_starting_equipment: Mapped[List['ClassesStartingEquipment']] = relationship('ClassesStartingEquipment', back_populates='class_')
    classes_starting_equipment_options: Mapped[List['ClassesStartingEquipmentOptions']] = relationship('ClassesStartingEquipmentOptions', back_populates='class_')
    levels: Mapped[List['Levels']] = relationship('Levels', back_populates='class_')
    spells_classes: Mapped[List['SpellsClasses']] = relationship('SpellsClasses', back_populates='classes')
    subclasses_class: Mapped[List['SubclassesClass']] = relationship('SubclassesClass', back_populates='classes')
    class_multi_classing_proficiencies: Mapped[List['ClassMultiClassingProficiencies']] = relationship('ClassMultiClassingProficiencies', back_populates='class_')
    classes_levels: Mapped[List['ClassesLevels']] = relationship('ClassesLevels', back_populates='class_')
    classes_proficiencies: Mapped[List['ClassesProficiencies']] = relationship('ClassesProficiencies', back_populates='class_')
    classes_proficiency_choices: Mapped[List['ClassesProficiencyChoices']] = relationship('ClassesProficiencyChoices', back_populates='class_')


class Conditions(Base):
    __tablename__ = 'conditions'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='conditions_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[Optional[str]] = mapped_column(Text)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    url: Mapped[Optional[str]] = mapped_column(String(255))

    monster_condition_immunities: Mapped[List['MonsterConditionImmunities']] = relationship('MonsterConditionImmunities', back_populates='condition')


class DamageTypes(Base):
    __tablename__ = 'damage_types'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='damage_types_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[Optional[str]] = mapped_column(Text)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    url: Mapped[Optional[str]] = mapped_column(String(255))

    equipment: Mapped[List['Equipment']] = relationship('Equipment', foreign_keys='[Equipment.damage_type]', back_populates='damage_types')
    equipment_: Mapped[List['Equipment']] = relationship('Equipment', foreign_keys='[Equipment.two_handed_damage_type]', back_populates='damage_types_')
    monster_actions: Mapped[List['MonsterActions']] = relationship('MonsterActions', back_populates='damage_types')
    monster_legendary_actions: Mapped[List['MonsterLegendaryActions']] = relationship('MonsterLegendaryActions', back_populates='damage_type')
    monster_reactions: Mapped[List['MonsterReactions']] = relationship('MonsterReactions', back_populates='damage_type')
    monsters_special_abilities: Mapped[List['MonstersSpecialAbilities']] = relationship('MonstersSpecialAbilities', back_populates='damage_type')
    spells: Mapped[List['Spells']] = relationship('Spells', back_populates='damage_type')


class EquipmentCategories(Base):
    __tablename__ = 'equipment_categories'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='equipment_categories_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    equipments: Mapped[Optional[int]] = mapped_column(Integer, Sequence('equipments_id_seq'))
    name: Mapped[Optional[str]] = mapped_column(String(255))
    url: Mapped[Optional[str]] = mapped_column(String(255))

    equipment: Mapped[List['Equipment']] = relationship('Equipment', foreign_keys='[Equipment.equipment_category]', back_populates='equipment_categories')
    equipment_: Mapped[List['Equipment']] = relationship('Equipment', foreign_keys='[Equipment.gear_category]', back_populates='equipment_categories_')
    magic_items: Mapped[List['MagicItems']] = relationship('MagicItems', back_populates='equipment_categories')
    proficiencies: Mapped[List['Proficiencies']] = relationship('Proficiencies', back_populates='reference_equipment_category')


class Features(Base):
    __tablename__ = 'features'
    __table_args__ = (
        ForeignKeyConstraint(['class_id'], ['classes.id'], ondelete='SET NULL', name='fk_feature_class'),
        ForeignKeyConstraint(['parent_id'], ['features.id'], ondelete='SET NULL', name='fk_feature_parent'),
        ForeignKeyConstraint(['prerequisites_id'], ['prerequisites.prerequisites_id'], ondelete='SET NULL', name='fk_features_to_prerequisites_prereq_id'),
        ForeignKeyConstraint(['subclass_id'], ['subclasses.id'], ondelete='SET NULL', name='fk_feature_subclass'),
        PrimaryKeyConstraint('id', name='features_pkey'),
        UniqueConstraint('feature_spesific_id', name='unique_feature_spesific_id'),
        UniqueConstraint('prerequisites_id', name='unique_prerequisites_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    class_id: Mapped[Optional[int]] = mapped_column(Integer)
    description: Mapped[Optional[str]] = mapped_column(Text)
    level: Mapped[Optional[int]] = mapped_column(Integer)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    parent_id: Mapped[Optional[int]] = mapped_column(Integer)
    prerequisites_id: Mapped[Optional[int]] = mapped_column(Integer)
    subclass_id: Mapped[Optional[int]] = mapped_column(Integer)
    url: Mapped[Optional[str]] = mapped_column(String(255))
    feature_spesific_id: Mapped[Optional[int]] = mapped_column(Integer)

    class_: Mapped[Optional['Classes']] = relationship('Classes', back_populates='features')
    parent: Mapped[Optional['Features']] = relationship('Features', remote_side=[id], back_populates='parent_reverse')
    parent_reverse: Mapped[List['Features']] = relationship('Features', remote_side=[parent_id], back_populates='parent')
    prerequisites: Mapped[Optional['Prerequisites']] = relationship('Prerequisites', foreign_keys=[prerequisites_id], back_populates='features')
    subclass: Mapped[Optional['Subclasses']] = relationship('Subclasses', back_populates='features')
    prerequisites_: Mapped[List['Prerequisites']] = relationship('Prerequisites', foreign_keys='[Prerequisites.feature_id]', back_populates='feature')
    prerequisites1: Mapped[List['Prerequisites']] = relationship('Prerequisites', foreign_keys='[Prerequisites.feature_id]', back_populates='feature_')
    prerequisites2: Mapped[Optional['Prerequisites']] = relationship('Prerequisites', uselist=False, foreign_keys='[Prerequisites.prerequisites_id]', back_populates='prerequisites')
    level_detail_features: Mapped[List['LevelDetailFeatures']] = relationship('LevelDetailFeatures', back_populates='feature')
    spells_subclasses: Mapped[List['SpellsSubclasses']] = relationship('SpellsSubclasses', back_populates='required_feature')


class Languages(Base):
    __tablename__ = 'languages'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='languages_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    script: Mapped[Optional[str]] = mapped_column(String(255))
    type: Mapped[Optional[str]] = mapped_column(String(255))
    url: Mapped[Optional[str]] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text)
    typical_speakers: Mapped[Optional[str]] = mapped_column(Text)

    race_language_options: Mapped[List['RaceLanguageOptions']] = relationship('RaceLanguageOptions', back_populates='language')
    race_languages: Mapped[List['RaceLanguages']] = relationship('RaceLanguages', back_populates='language')


class LevelDetail(Base):
    __tablename__ = 'level_detail'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='level_detail_pkey'),
        UniqueConstraint('features_id', name='level_detail_features_id_key')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    cantrips_known: Mapped[Optional[int]] = mapped_column(Integer)
    spells_known: Mapped[Optional[int]] = mapped_column(Integer)
    spell_slots_level_1: Mapped[Optional[int]] = mapped_column(Integer)
    spell_slots_level_2: Mapped[Optional[int]] = mapped_column(Integer)
    spell_slots_level_3: Mapped[Optional[int]] = mapped_column(Integer)
    spell_slots_level_4: Mapped[Optional[int]] = mapped_column(Integer)
    spell_slots_level_5: Mapped[Optional[int]] = mapped_column(Integer)
    spell_slots_level_6: Mapped[Optional[int]] = mapped_column(Integer)
    spell_slots_level_7: Mapped[Optional[int]] = mapped_column(Integer)
    spell_slots_level_8: Mapped[Optional[int]] = mapped_column(Integer)
    spell_slots_level_9: Mapped[Optional[int]] = mapped_column(Integer)
    rage_count: Mapped[Optional[int]] = mapped_column(Integer)
    rage_damage_bonus: Mapped[Optional[int]] = mapped_column(Integer)
    brutal_critical_dice: Mapped[Optional[int]] = mapped_column(Integer)
    bardic_inspiration_die: Mapped[Optional[int]] = mapped_column(Integer)
    song_of_rest_die: Mapped[Optional[int]] = mapped_column(Integer)
    magical_secrets_max_5: Mapped[Optional[int]] = mapped_column(Integer)
    magical_secrets_max_7: Mapped[Optional[int]] = mapped_column(Integer)
    magical_secrets_max_9: Mapped[Optional[int]] = mapped_column(Integer)
    wild_shape_max_cr: Mapped[Optional[int]] = mapped_column(Integer)
    wild_shape_swim: Mapped[Optional[bool]] = mapped_column(Boolean)
    wild_shape_fly: Mapped[Optional[bool]] = mapped_column(Boolean)
    extra_attacks: Mapped[Optional[int]] = mapped_column(Integer)
    action_surges: Mapped[Optional[int]] = mapped_column(Integer)
    indomitable_uses: Mapped[Optional[int]] = mapped_column(Integer)
    channel_divinity_charges: Mapped[Optional[int]] = mapped_column(Integer)
    destroy_undead_cr: Mapped[Optional[int]] = mapped_column(Integer)
    additional_magical_secrets_max_lvl: Mapped[Optional[int]] = mapped_column(Integer)
    features_id: Mapped[Optional[int]] = mapped_column(Integer)

    level_detail_features: Mapped[List['LevelDetailFeatures']] = relationship('LevelDetailFeatures', back_populates='level_detail')
    levels: Mapped[List['Levels']] = relationship('Levels', back_populates='detail')


class MagicSchools(Base):
    __tablename__ = 'magic_schools'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='magic_schools_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[Optional[str]] = mapped_column(Text)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    url: Mapped[Optional[str]] = mapped_column(String(255))

    spells: Mapped[List['Spells']] = relationship('Spells', back_populates='school')


class Monsters(Base):
    __tablename__ = 'monsters'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='monsters_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    size: Mapped[Optional[str]] = mapped_column(String(50))
    type: Mapped[Optional[str]] = mapped_column(String(50))
    subtype: Mapped[Optional[str]] = mapped_column(String(100))
    alignment: Mapped[Optional[str]] = mapped_column(String(100))
    armor_class_type: Mapped[Optional[str]] = mapped_column(String(100))
    armor_class_value: Mapped[Optional[int]] = mapped_column(Integer)
    hit_points: Mapped[Optional[int]] = mapped_column(Integer)
    hit_dice: Mapped[Optional[str]] = mapped_column(String(50))
    xp: Mapped[Optional[int]] = mapped_column(Integer)
    challenge_rating: Mapped[Optional[float]] = mapped_column(Double(53))
    strength: Mapped[Optional[int]] = mapped_column(Integer)
    dexterity: Mapped[Optional[int]] = mapped_column(Integer)
    constitution: Mapped[Optional[int]] = mapped_column(Integer)
    intelligence: Mapped[Optional[int]] = mapped_column(Integer)
    wisdom: Mapped[Optional[int]] = mapped_column(Integer)
    charisma: Mapped[Optional[int]] = mapped_column(Integer)
    languages: Mapped[Optional[str]] = mapped_column(Text)
    proficiency_bonus: Mapped[Optional[int]] = mapped_column(Integer)
    senses: Mapped[Optional[str]] = mapped_column(Text)
    speed: Mapped[Optional[str]] = mapped_column(Text)
    proficiencies_id: Mapped[Optional[int]] = mapped_column(Integer)
    condition_immunities_id: Mapped[Optional[int]] = mapped_column(Integer)
    actions_id: Mapped[Optional[int]] = mapped_column(Integer)
    legendary_actions_id: Mapped[Optional[int]] = mapped_column(Integer)
    special_abilities_id: Mapped[Optional[int]] = mapped_column(Integer)
    reactions_id: Mapped[Optional[int]] = mapped_column(Integer)
    damage_vulnerabilities: Mapped[Optional[str]] = mapped_column(Text)
    damage_resistances: Mapped[Optional[str]] = mapped_column(Text)
    damage_immunities: Mapped[Optional[str]] = mapped_column(Text)

    monster_actions: Mapped[List['MonsterActions']] = relationship('MonsterActions', back_populates='monster')
    monster_condition_immunities: Mapped[List['MonsterConditionImmunities']] = relationship('MonsterConditionImmunities', back_populates='monster')
    monster_legendary_actions: Mapped[List['MonsterLegendaryActions']] = relationship('MonsterLegendaryActions', back_populates='monster')
    monster_reactions: Mapped[List['MonsterReactions']] = relationship('MonsterReactions', back_populates='monster')
    monsters_special_abilities: Mapped[List['MonstersSpecialAbilities']] = relationship('MonstersSpecialAbilities', back_populates='monster')
    monster_proficiencies: Mapped[List['MonsterProficiencies']] = relationship('MonsterProficiencies', back_populates='monster')


class Prerequisites(Base):
    __tablename__ = 'prerequisites'
    __table_args__ = (
        ForeignKeyConstraint(['feature_id'], ['features.id'], ondelete='CASCADE', name='fk_prereq_to_features_id'),
        ForeignKeyConstraint(['feature_id'], ['features.id'], ondelete='CASCADE', name='fk_prerequisites_feature'),
        ForeignKeyConstraint(['prerequisites_id'], ['features.id'], ondelete='CASCADE', name='fk_prereq_to_features_reqid'),
        ForeignKeyConstraint(['spell_id'], ['spells.id'], ondelete='CASCADE', name='fk_prereq_to_spells'),
        PrimaryKeyConstraint('id', name='prerequisites_pkey'),
        UniqueConstraint('prerequisites_id', name='unique_prerequisites_prereq_id')
    )

    id: Mapped[int] = mapped_column(Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), primary_key=True)
    prerequisites_id: Mapped[Optional[int]] = mapped_column(Integer)
    spell_id: Mapped[Optional[int]] = mapped_column(Integer)
    feature_id: Mapped[Optional[int]] = mapped_column(Integer)

    features: Mapped[Optional['Features']] = relationship('Features', uselist=False, foreign_keys='[Features.prerequisites_id]', back_populates='prerequisites')
    feature: Mapped[Optional['Features']] = relationship('Features', foreign_keys=[feature_id], back_populates='prerequisites_')
    feature_: Mapped[Optional['Features']] = relationship('Features', foreign_keys=[feature_id], back_populates='prerequisites1')
    prerequisites: Mapped[Optional['Features']] = relationship('Features', foreign_keys=[prerequisites_id], back_populates='prerequisites2')
    spell: Mapped[Optional['Spells']] = relationship('Spells', back_populates='prerequisites')


class Races(Base):
    __tablename__ = 'races'
    __table_args__ = (
        ForeignKeyConstraint(['ability_score_id'], ['ability_scores.id'], ondelete='SET NULL', name='fk_races_to_ability_scores'),
        ForeignKeyConstraint(['subrace_id'], ['subraces.id'], ondelete='SET NULL', name='fk_races_to_subraces'),
        PrimaryKeyConstraint('id', name='races_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    alignment: Mapped[Optional[str]] = mapped_column(Text)
    age: Mapped[Optional[str]] = mapped_column(Text)
    language_desc: Mapped[Optional[str]] = mapped_column(Text)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    size: Mapped[Optional[str]] = mapped_column(String(255))
    size_description: Mapped[Optional[str]] = mapped_column(Text)
    speed: Mapped[Optional[int]] = mapped_column(Integer)
    url: Mapped[Optional[str]] = mapped_column(String(255))
    ability_bonus: Mapped[Optional[int]] = mapped_column(Integer)
    ability_score_id: Mapped[Optional[int]] = mapped_column(Integer)
    ability_bonus_choose: Mapped[Optional[int]] = mapped_column(Integer)
    ability_bonus_option_id: Mapped[Optional[int]] = mapped_column(Integer)
    starting_proficiency_id: Mapped[Optional[int]] = mapped_column(Integer)
    starting_proficiency_option_id: Mapped[Optional[int]] = mapped_column(Integer)
    language_id: Mapped[Optional[int]] = mapped_column(Integer)
    subrace_id: Mapped[Optional[int]] = mapped_column(Integer)
    trait_id: Mapped[Optional[int]] = mapped_column(Integer)

    ability_score: Mapped[Optional['AbilityScores']] = relationship('AbilityScores', back_populates='races')
    subrace: Mapped[Optional['Subraces']] = relationship('Subraces', foreign_keys=[subrace_id], back_populates='races')
    subraces: Mapped[List['Subraces']] = relationship('Subraces', foreign_keys='[Subraces.race_id]', back_populates='race')
    race_ability_bonus_options: Mapped[List['RaceAbilityBonusOptions']] = relationship('RaceAbilityBonusOptions', back_populates='race')
    race_language_options: Mapped[List['RaceLanguageOptions']] = relationship('RaceLanguageOptions', back_populates='race')
    race_languages: Mapped[List['RaceLanguages']] = relationship('RaceLanguages', back_populates='race')
    race_subraces: Mapped[List['RaceSubraces']] = relationship('RaceSubraces', back_populates='race')
    race_proficiencies: Mapped[List['RaceProficiencies']] = relationship('RaceProficiencies', back_populates='race')
    race_proficiency_options: Mapped[List['RaceProficiencyOptions']] = relationship('RaceProficiencyOptions', back_populates='race')
    race_traits: Mapped[List['RaceTraits']] = relationship('RaceTraits', back_populates='race')
    traits_races: Mapped[List['TraitsRaces']] = relationship('TraitsRaces', back_populates='races')
    race_speeds: Mapped[List['RaceSpeedDefault']] = relationship('RaceSpeedDefault', back_populates='race')



class RuleSections(Base):
    __tablename__ = 'rule_sections'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='rule_sections_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    url: Mapped[Optional[str]] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text)

    rules_subsections: Mapped[List['RulesSubsections']] = relationship('RulesSubsections', back_populates='rule_sections')


class Rules(Base):
    __tablename__ = 'rules'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='rules_pkey'),
        UniqueConstraint('subsections', name='unique_subsections')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[Optional[str]] = mapped_column(Text)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    subsections: Mapped[Optional[int]] = mapped_column(Integer)
    url: Mapped[Optional[str]] = mapped_column(String(255))

    rules_subsections: Mapped[List['RulesSubsections']] = relationship('RulesSubsections', back_populates='rules')


class Subraces(Base):
    __tablename__ = 'subraces'
    __table_args__ = (
        ForeignKeyConstraint(['ability_score_id'], ['ability_scores.id'], ondelete='SET NULL', name='fk_subraces_to_ability_scores'),
        ForeignKeyConstraint(['race_id'], ['races.id'], ondelete='SET NULL', name='fk_subraces_to_races'),
        PrimaryKeyConstraint('id', name='subraces_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    url: Mapped[Optional[str]] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text)
    race_id: Mapped[Optional[int]] = mapped_column(Integer)
    ability_score_id: Mapped[Optional[int]] = mapped_column(Integer)
    languages: Mapped[Optional[list]] = mapped_column(ARRAY(Text()))
    proficiency_id: Mapped[Optional[int]] = mapped_column(Integer)
    trait_id: Mapped[Optional[int]] = mapped_column(Integer)

    races: Mapped[List['Races']] = relationship('Races', foreign_keys='[Races.subrace_id]', back_populates='subrace')
    ability_score: Mapped[Optional['AbilityScores']] = relationship('AbilityScores', back_populates='subraces')
    race: Mapped[Optional['Races']] = relationship('Races', foreign_keys=[race_id], back_populates='subraces')
    race_subraces: Mapped[List['RaceSubraces']] = relationship('RaceSubraces', back_populates='subrace')
    subrace_proficiencies: Mapped[List['SubraceProficiencies']] = relationship('SubraceProficiencies', back_populates='subrace')
    traits: Mapped[List['Traits']] = relationship('Traits', back_populates='subrace')
    subrace_traits: Mapped[List['SubraceTraits']] = relationship('SubraceTraits', back_populates='subrace')


class WeaponProperties(Base):
    __tablename__ = 'weapon_properties'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='weapon_properties_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[Optional[str]] = mapped_column(Text)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    url: Mapped[Optional[str]] = mapped_column(String(255))

    equipment_properties: Mapped[List['EquipmentProperties']] = relationship('EquipmentProperties', back_populates='weapon_properties')


class ClassMultiClassingPrerequisites(Base):
    __tablename__ = 'class_multi_classing_prerequisites'
    __table_args__ = (
        ForeignKeyConstraint(['ability_score_id'], ['ability_scores.id'], ondelete='CASCADE', name='class_multi_classing_prerequisites_ability_score_id_fkey'),
        ForeignKeyConstraint(['class_id'], ['classes.id'], ondelete='CASCADE', name='class_multi_classing_prerequisites_class_id_fkey'),
        PrimaryKeyConstraint('id', name='class_multi_classing_prerequisites_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    minimum_score: Mapped[int] = mapped_column(Integer)
    class_id: Mapped[Optional[int]] = mapped_column(Integer)
    ability_score_id: Mapped[Optional[int]] = mapped_column(Integer)

    ability_score: Mapped[Optional['AbilityScores']] = relationship('AbilityScores', back_populates='class_multi_classing_prerequisites')
    class_: Mapped[Optional['Classes']] = relationship('Classes', back_populates='class_multi_classing_prerequisites')


class ClassesSavingThrows(Base):
    __tablename__ = 'classes_saving_throws'
    __table_args__ = (
        ForeignKeyConstraint(['ability_score_id'], ['ability_scores.id'], ondelete='CASCADE', name='classes_saving_throws_ability_score_id_fkey'),
        ForeignKeyConstraint(['class_id'], ['classes.id'], ondelete='CASCADE', name='classes_saving_throws_class_id_fkey'),
        PrimaryKeyConstraint('id', name='classes_saving_throws_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    class_id: Mapped[Optional[int]] = mapped_column(Integer)
    ability_score_id: Mapped[Optional[int]] = mapped_column(Integer)

    ability_score: Mapped[Optional['AbilityScores']] = relationship('AbilityScores', back_populates='classes_saving_throws')
    class_: Mapped[Optional['Classes']] = relationship('Classes', back_populates='classes_saving_throws')


class Equipment(Base):
    __tablename__ = 'equipment'
    __table_args__ = (
        ForeignKeyConstraint(['damage_type'], ['damage_types.id'], name='fk_equipment_damage_type'),
        ForeignKeyConstraint(['equipment_category'], ['equipment_categories.id'], name='fk_equipment_equipment_category'),
        ForeignKeyConstraint(['gear_category'], ['equipment_categories.id'], name='fk_equipment_gear_category'),
        ForeignKeyConstraint(['two_handed_damage_type'], ['damage_types.id'], name='fk_equipment_two_handed_damage_type'),
        PrimaryKeyConstraint('id', name='equipment_pkey'),
        UniqueConstraint('properties', name='unique_properties')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    category_range: Mapped[Optional[str]] = mapped_column(String(255))
    damage_dice: Mapped[Optional[str]] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text)
    equipment_category: Mapped[Optional[int]] = mapped_column(Integer)
    gear_category: Mapped[Optional[int]] = mapped_column(Integer)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    properties: Mapped[Optional[int]] = mapped_column(Integer)
    range_normal: Mapped[Optional[int]] = mapped_column(Integer)
    special: Mapped[Optional[str]] = mapped_column(Text)
    speed_quantity: Mapped[Optional[int]] = mapped_column(Integer)
    stealth_disadvantage: Mapped[Optional[bool]] = mapped_column(Boolean)
    str_minimum: Mapped[Optional[int]] = mapped_column(Integer)
    throw_range_normal: Mapped[Optional[int]] = mapped_column(Integer)
    tool_category: Mapped[Optional[str]] = mapped_column(String(255))
    two_handed_damage_dice: Mapped[Optional[str]] = mapped_column(String(255))
    url: Mapped[Optional[str]] = mapped_column(String(255))
    vehicle_category: Mapped[Optional[str]] = mapped_column(String(255))
    weight: Mapped[Optional[int]] = mapped_column(Integer)
    weapon_category: Mapped[Optional[str]] = mapped_column(String(255))
    weapon_range: Mapped[Optional[str]] = mapped_column(String(255))
    cost_quantity: Mapped[Optional[int]] = mapped_column(Integer)
    cost_unit: Mapped[Optional[str]] = mapped_column(String(255))
    damage_type: Mapped[Optional[int]] = mapped_column(Integer)
    range_long: Mapped[Optional[int]] = mapped_column(Integer)
    speed_unit: Mapped[Optional[str]] = mapped_column(String(255))
    two_handed_damage_type: Mapped[Optional[int]] = mapped_column(Integer)
    throw_range_long: Mapped[Optional[int]] = mapped_column(Integer)

    damage_types: Mapped[Optional['DamageTypes']] = relationship('DamageTypes', foreign_keys=[damage_type], back_populates='equipment')
    equipment_categories: Mapped[Optional['EquipmentCategories']] = relationship('EquipmentCategories', foreign_keys=[equipment_category], back_populates='equipment')
    equipment_categories_: Mapped[Optional['EquipmentCategories']] = relationship('EquipmentCategories', foreign_keys=[gear_category], back_populates='equipment_')
    damage_types_: Mapped[Optional['DamageTypes']] = relationship('DamageTypes', foreign_keys=[two_handed_damage_type], back_populates='equipment_')
    classes_starting_equipment: Mapped[List['ClassesStartingEquipment']] = relationship('ClassesStartingEquipment', back_populates='equipment')
    classes_starting_equipment_options: Mapped[List['ClassesStartingEquipmentOptions']] = relationship('ClassesStartingEquipmentOptions', back_populates='equipment')
    equipment_properties: Mapped[List['EquipmentProperties']] = relationship('EquipmentProperties', back_populates='equipment')
    proficiencies: Mapped[List['Proficiencies']] = relationship('Proficiencies', back_populates='reference_equipment')


class Feats(Base):
    __tablename__ = 'feats'
    __table_args__ = (
        ForeignKeyConstraint(['ability_score'], ['ability_scores.id'], name='fk_feats_ability_score'),
        PrimaryKeyConstraint('id', name='feats_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[Optional[str]] = mapped_column(Text)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    ability_score: Mapped[Optional[int]] = mapped_column(Integer)
    url: Mapped[Optional[str]] = mapped_column(String(255))
    minimum_score: Mapped[Optional[int]] = mapped_column(Integer)

    ability_scores: Mapped[Optional['AbilityScores']] = relationship('AbilityScores', back_populates='feats')


t_feature_specific = Table(
    'feature_specific', Base.metadata,
    Column('id', Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), nullable=False),
    Column('feature_specific_id', Integer),
    Column('description', Text),
    Column('enemy_type_options', Text),
    Column('choose', Integer),
    Column('terrain_type_options', Text),
    Column('invocation_id', Integer),
    Column('subfeature_id', Integer),
    Column('expertise_id', Integer),
    ForeignKeyConstraint(['feature_specific_id'], ['features.feature_spesific_id'], ondelete='CASCADE', name='fk_feature_specific_to_features'),
    UniqueConstraint('expertise_id', name='unique_expertise_id'),
    UniqueConstraint('feature_specific_id', name='unique_feature_specific_id'),
    UniqueConstraint('invocation_id', name='unique_invocation_id'),
    UniqueConstraint('invocation_id', name='unique_invocation_id_feature_specific'),
    UniqueConstraint('subfeature_id', name='unique_subfeature_id')
)


class LevelDetailFeatures(Base):
    __tablename__ = 'level_detail_features'
    __table_args__ = (
        ForeignKeyConstraint(['feature_id'], ['features.id'], ondelete='CASCADE', name='level_detail_features_feature_id_fkey'),
        ForeignKeyConstraint(['level_detail_id'], ['level_detail.features_id'], ondelete='CASCADE', name='level_detail_features_level_detail_id_fkey'),
        PrimaryKeyConstraint('id', name='level_detail_features_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    level_detail_id: Mapped[int] = mapped_column(Integer)
    feature_id: Mapped[int] = mapped_column(Integer)

    feature: Mapped['Features'] = relationship('Features', back_populates='level_detail_features')
    level_detail: Mapped['LevelDetail'] = relationship('LevelDetail', back_populates='level_detail_features')


class MagicItems(Base):
    __tablename__ = 'magic_items'
    __table_args__ = (
        ForeignKeyConstraint(['equipment_category'], ['equipment_categories.id'], name='fk_equipment_category'),
        PrimaryKeyConstraint('id', name='magic_items_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[Optional[str]] = mapped_column(Text)
    equipment_category: Mapped[Optional[int]] = mapped_column(Integer)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    rarity: Mapped[Optional[str]] = mapped_column(String(255))
    url: Mapped[Optional[str]] = mapped_column(String(255))

    equipment_categories: Mapped[Optional['EquipmentCategories']] = relationship('EquipmentCategories', back_populates='magic_items')


class MonsterActions(Base):
    __tablename__ = 'monster_actions'
    __table_args__ = (
        ForeignKeyConstraint(['damage_type'], ['damage_types.id'], ondelete='SET NULL', name='monster_actions_damage_type_fkey'),
        ForeignKeyConstraint(['monster_id'], ['monsters.id'], ondelete='CASCADE', name='monster_actions_monster_id_fkey'),
        PrimaryKeyConstraint('id', name='monster_actions_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    monster_id: Mapped[Optional[int]] = mapped_column(Integer)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text)
    damage_type: Mapped[Optional[int]] = mapped_column(Integer)
    damage_dice: Mapped[Optional[str]] = mapped_column(String(50))

    damage_types: Mapped[Optional['DamageTypes']] = relationship('DamageTypes', back_populates='monster_actions')
    monster: Mapped[Optional['Monsters']] = relationship('Monsters', back_populates='monster_actions')


class MonsterConditionImmunities(Base):
    __tablename__ = 'monster_condition_immunities'
    __table_args__ = (
        ForeignKeyConstraint(['condition_id'], ['conditions.id'], ondelete='SET NULL', name='monster_condition_immunities_condition_id_fkey'),
        ForeignKeyConstraint(['monster_id'], ['monsters.id'], ondelete='CASCADE', name='monster_condition_immunities_monster_id_fkey'),
        PrimaryKeyConstraint('id', name='monster_condition_immunities_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    monster_id: Mapped[Optional[int]] = mapped_column(Integer)
    condition_id: Mapped[Optional[int]] = mapped_column(Integer)

    condition: Mapped[Optional['Conditions']] = relationship('Conditions', back_populates='monster_condition_immunities')
    monster: Mapped[Optional['Monsters']] = relationship('Monsters', back_populates='monster_condition_immunities')


class MonsterLegendaryActions(Base):
    __tablename__ = 'monster_legendary_actions'
    __table_args__ = (
        ForeignKeyConstraint(['damage_type_id'], ['damage_types.id'], ondelete='SET NULL', name='monster_legendary_actions_damage_type_id_fkey'),
        ForeignKeyConstraint(['dc_type_id'], ['ability_scores.id'], ondelete='SET NULL', name='monster_legendary_actions_dc_type_id_fkey'),
        ForeignKeyConstraint(['monster_id'], ['monsters.id'], ondelete='CASCADE', name='monster_legendary_actions_monster_id_fkey'),
        PrimaryKeyConstraint('id', name='monster_legendary_actions_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    monster_id: Mapped[Optional[int]] = mapped_column(Integer)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text)
    dc_type_id: Mapped[Optional[int]] = mapped_column(Integer)
    dc_value: Mapped[Optional[int]] = mapped_column(Integer)
    success_type: Mapped[Optional[str]] = mapped_column(String(50))
    damage_type_id: Mapped[Optional[int]] = mapped_column(Integer)
    damage_dice: Mapped[Optional[str]] = mapped_column(String(50))

    damage_type: Mapped[Optional['DamageTypes']] = relationship('DamageTypes', back_populates='monster_legendary_actions')
    dc_type: Mapped[Optional['AbilityScores']] = relationship('AbilityScores', back_populates='monster_legendary_actions')
    monster: Mapped[Optional['Monsters']] = relationship('Monsters', back_populates='monster_legendary_actions')


class MonsterReactions(Base):
    __tablename__ = 'monster_reactions'
    __table_args__ = (
        ForeignKeyConstraint(['damage_type_id'], ['damage_types.id'], ondelete='SET NULL', name='monster_reactions_damage_type_id_fkey'),
        ForeignKeyConstraint(['dc_type_id'], ['ability_scores.id'], ondelete='SET NULL', name='monster_reactions_dc_type_id_fkey'),
        ForeignKeyConstraint(['monster_id'], ['monsters.id'], ondelete='CASCADE', name='monster_reactions_monster_id_fkey'),
        PrimaryKeyConstraint('id', name='monster_reactions_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    monster_id: Mapped[Optional[int]] = mapped_column(Integer)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text)
    attack_bonus: Mapped[Optional[int]] = mapped_column(Integer)
    damage_type_id: Mapped[Optional[int]] = mapped_column(Integer)
    damage_dice: Mapped[Optional[str]] = mapped_column(String(50))
    dc_type_id: Mapped[Optional[int]] = mapped_column(Integer)
    dc_value: Mapped[Optional[int]] = mapped_column(Integer)
    success_type: Mapped[Optional[str]] = mapped_column(String(50))

    damage_type: Mapped[Optional['DamageTypes']] = relationship('DamageTypes', back_populates='monster_reactions')
    dc_type: Mapped[Optional['AbilityScores']] = relationship('AbilityScores', back_populates='monster_reactions')
    monster: Mapped[Optional['Monsters']] = relationship('Monsters', back_populates='monster_reactions')


class MonstersSpecialAbilities(Base):
    __tablename__ = 'monsters_special_abilities'
    __table_args__ = (
        ForeignKeyConstraint(['damage_type_id'], ['damage_types.id'], ondelete='SET NULL', name='monsters_special_abilities_damage_type_id_fkey'),
        ForeignKeyConstraint(['dc_type_id'], ['ability_scores.id'], ondelete='SET NULL', name='monsters_special_abilities_dc_type_id_fkey'),
        ForeignKeyConstraint(['monster_id'], ['monsters.id'], ondelete='CASCADE', name='monsters_special_abilities_monster_id_fkey'),
        ForeignKeyConstraint(['spellcasting_ability_score_id'], ['ability_scores.id'], ondelete='SET NULL', name='monsters_special_abilities_spellcasting_ability_score_id_fkey'),
        PrimaryKeyConstraint('id', name='monsters_special_abilities_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    monster_id: Mapped[Optional[int]] = mapped_column(Integer)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text)
    damage_type_id: Mapped[Optional[int]] = mapped_column(Integer)
    damage_dice: Mapped[Optional[str]] = mapped_column(String(50))
    dc_type_id: Mapped[Optional[int]] = mapped_column(Integer)
    dc_value: Mapped[Optional[int]] = mapped_column(Integer)
    success_type: Mapped[Optional[str]] = mapped_column(String(50))
    spellcasting_level: Mapped[Optional[int]] = mapped_column(Integer)
    spellcasting_ability_score_id: Mapped[Optional[int]] = mapped_column(Integer)
    spellcasting_modifier: Mapped[Optional[int]] = mapped_column(Integer)
    spellcasting_components_required: Mapped[Optional[str]] = mapped_column(Text)
    spellcasting_school: Mapped[Optional[str]] = mapped_column(String(50))
    spellcasting_slots: Mapped[Optional[str]] = mapped_column(Text)

    damage_type: Mapped[Optional['DamageTypes']] = relationship('DamageTypes', back_populates='monsters_special_abilities')
    dc_type: Mapped[Optional['AbilityScores']] = relationship('AbilityScores', foreign_keys=[dc_type_id], back_populates='monsters_special_abilities')
    monster: Mapped[Optional['Monsters']] = relationship('Monsters', back_populates='monsters_special_abilities')
    spellcasting_ability_score: Mapped[Optional['AbilityScores']] = relationship('AbilityScores', foreign_keys=[spellcasting_ability_score_id], back_populates='monsters_special_abilities_')
    monster_spells: Mapped[List['MonsterSpells']] = relationship('MonsterSpells', back_populates='monster_special_ability')


class RaceAbilityBonusOptions(Base):
    __tablename__ = 'race_ability_bonus_options'
    __table_args__ = (
        ForeignKeyConstraint(['ability_score_id'], ['ability_scores.id'], ondelete='CASCADE', name='fk_rabo_ability'),
        ForeignKeyConstraint(['race_id'], ['races.id'], ondelete='CASCADE', name='fk_rabo_race'),
        PrimaryKeyConstraint('id', name='race_ability_bonus_options_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    race_id: Mapped[int] = mapped_column(Integer)
    ability_score_id: Mapped[int] = mapped_column(Integer)

    ability_score: Mapped['AbilityScores'] = relationship('AbilityScores', back_populates='race_ability_bonus_options')
    race: Mapped['Races'] = relationship('Races', back_populates='race_ability_bonus_options')


class RaceLanguageOptions(Base):
    __tablename__ = 'race_language_options'
    __table_args__ = (
        ForeignKeyConstraint(['language_id'], ['languages.id'], ondelete='CASCADE', name='fk_rlo_lang'),
        ForeignKeyConstraint(['race_id'], ['races.id'], ondelete='CASCADE', name='fk_rlo_race'),
        PrimaryKeyConstraint('id', name='race_language_options_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    race_id: Mapped[int] = mapped_column(Integer)
    language_id: Mapped[int] = mapped_column(Integer)

    language: Mapped['Languages'] = relationship('Languages', back_populates='race_language_options')
    race: Mapped['Races'] = relationship('Races', back_populates='race_language_options')


class RaceLanguages(Base):
    __tablename__ = 'race_languages'
    __table_args__ = (
        ForeignKeyConstraint(['language_id'], ['languages.id'], ondelete='CASCADE', name='fk_rl_lang'),
        ForeignKeyConstraint(['race_id'], ['races.id'], ondelete='CASCADE', name='fk_rl_race'),
        PrimaryKeyConstraint('id', name='race_languages_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    race_id: Mapped[int] = mapped_column(Integer)
    language_id: Mapped[int] = mapped_column(Integer)

    language: Mapped['Languages'] = relationship('Languages', back_populates='race_languages')
    race: Mapped['Races'] = relationship('Races', back_populates='race_languages')


class RaceSubraces(Base):
    __tablename__ = 'race_subraces'
    __table_args__ = (
        ForeignKeyConstraint(['race_id'], ['races.id'], ondelete='CASCADE', name='fk_rs_race'),
        ForeignKeyConstraint(['subrace_id'], ['subraces.id'], ondelete='CASCADE', name='fk_rs_subrace'),
        PrimaryKeyConstraint('id', name='race_subraces_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    race_id: Mapped[int] = mapped_column(Integer)
    subrace_id: Mapped[int] = mapped_column(Integer)

    race: Mapped['Races'] = relationship('Races', back_populates='race_subraces')
    subrace: Mapped['Subraces'] = relationship('Subraces', back_populates='race_subraces')


class RulesSubsections(Base):
    __tablename__ = 'rules_subsections'
    __table_args__ = (
        ForeignKeyConstraint(['rule_sections_id'], ['rule_sections.id'], name='rules_subsections_rule_sections_id_fkey'),
        ForeignKeyConstraint(['rules_id'], ['rules.subsections'], ondelete='CASCADE', name='fk_rules_subsections_subsections'),
        PrimaryKeyConstraint('id', name='rules_subsections_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    rules_id: Mapped[Optional[int]] = mapped_column(Integer)
    rule_sections_id: Mapped[Optional[int]] = mapped_column(Integer)

    rule_sections: Mapped[Optional['RuleSections']] = relationship('RuleSections', back_populates='rules_subsections')
    rules: Mapped[Optional['Rules']] = relationship('Rules', back_populates='rules_subsections')


class Skills(Base):
    __tablename__ = 'skills'
    __table_args__ = (
        ForeignKeyConstraint(['ability_score'], ['ability_scores.id'], ondelete='SET NULL', name='fk_ability_score'),
        PrimaryKeyConstraint('id', name='skills_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[Optional[str]] = mapped_column(Text)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    ability_score: Mapped[Optional[int]] = mapped_column(Integer)
    url: Mapped[Optional[str]] = mapped_column(String(255))

    ability_scores: Mapped[Optional['AbilityScores']] = relationship('AbilityScores', back_populates='skills')
    proficiencies: Mapped[List['Proficiencies']] = relationship('Proficiencies', back_populates='reference_skill')


class Spells(Base):
    __tablename__ = 'spells'
    __table_args__ = (
        ForeignKeyConstraint(['damage_type_id'], ['damage_types.id'], ondelete='SET NULL', name='spells_damage_type_id_fkey'),
        ForeignKeyConstraint(['dc_id'], ['ability_scores.id'], ondelete='SET NULL', name='spells_dc_id_fkey'),
        ForeignKeyConstraint(['school_id'], ['magic_schools.id'], ondelete='SET NULL', name='spells_school_id_fkey'),
        PrimaryKeyConstraint('id', name='spells_pkey'),
        UniqueConstraint('classes_id', name='unique_classes_id'),
        UniqueConstraint('subclasses_id', name='unique_subclasses_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    attack_type: Mapped[Optional[str]] = mapped_column(String(255))
    casting_time: Mapped[Optional[str]] = mapped_column(String(255))
    components: Mapped[Optional[str]] = mapped_column(Text)
    concentration: Mapped[Optional[bool]] = mapped_column(Boolean)
    description: Mapped[Optional[str]] = mapped_column(Text)
    duration: Mapped[Optional[str]] = mapped_column(String(255))
    higher_level: Mapped[Optional[str]] = mapped_column(Text)
    level: Mapped[Optional[int]] = mapped_column(Integer)
    material: Mapped[Optional[str]] = mapped_column(Text)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    range: Mapped[Optional[str]] = mapped_column(String(255))
    ritual: Mapped[Optional[bool]] = mapped_column(Boolean)
    saving_throw: Mapped[Optional[str]] = mapped_column(String(255))
    url: Mapped[Optional[str]] = mapped_column(String(255))
    area_of_effect_size: Mapped[Optional[int]] = mapped_column(Integer)
    classes_id: Mapped[Optional[int]] = mapped_column(Integer)
    subclasses_id: Mapped[Optional[int]] = mapped_column(Integer)
    school_id: Mapped[Optional[int]] = mapped_column(Integer)
    dc_id: Mapped[Optional[int]] = mapped_column(Integer)
    damage_type_id: Mapped[Optional[int]] = mapped_column(Integer)
    damage_at_slot_level: Mapped[Optional[str]] = mapped_column(Text)
    heal_at_slot_level: Mapped[Optional[str]] = mapped_column(Text)
    area_of_effect_type: Mapped[Optional[str]] = mapped_column(String(255))

    prerequisites: Mapped[List['Prerequisites']] = relationship('Prerequisites', back_populates='spell')
    damage_type: Mapped[Optional['DamageTypes']] = relationship('DamageTypes', back_populates='spells')
    dc: Mapped[Optional['AbilityScores']] = relationship('AbilityScores', back_populates='spells')
    school: Mapped[Optional['MagicSchools']] = relationship('MagicSchools', back_populates='spells')
    monster_spells: Mapped[List['MonsterSpells']] = relationship('MonsterSpells', back_populates='spell')
    spells_classes: Mapped[List['SpellsClasses']] = relationship('SpellsClasses', back_populates='spells')
    spells_subclasses: Mapped[List['SpellsSubclasses']] = relationship('SpellsSubclasses', back_populates='spells')
    trait_options: Mapped[List['TraitOptions']] = relationship('TraitOptions', back_populates='spell')


class Subclasses(Base):
    __tablename__ = 'subclasses'
    __table_args__ = (
        ForeignKeyConstraint(['class_id'], ['classes.id'], ondelete='SET NULL', name='subclasses_class_id_fkey'),
        PrimaryKeyConstraint('id', name='subclasses_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    class_id: Mapped[Optional[int]] = mapped_column(Integer)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    spells_id: Mapped[Optional[int]] = mapped_column(Integer)
    url: Mapped[Optional[str]] = mapped_column(String(255))
    description: Mapped[Optional[str]] = mapped_column(Text)
    subclass_flavor: Mapped[Optional[str]] = mapped_column(String(255))

    features: Mapped[List['Features']] = relationship('Features', back_populates='subclass')
    class_: Mapped[Optional['Classes']] = relationship('Classes', back_populates='subclasses')
    levels: Mapped[List['Levels']] = relationship('Levels', back_populates='subclass')
    subclasses_class: Mapped[List['SubclassesClass']] = relationship('SubclassesClass', back_populates='subclasses')
    spells_subclasses: Mapped[List['SpellsSubclasses']] = relationship('SpellsSubclasses', back_populates='subclasses')


class ClassesStartingEquipment(Base):
    __tablename__ = 'classes_starting_equipment'
    __table_args__ = (
        ForeignKeyConstraint(['class_id'], ['classes.id'], ondelete='CASCADE', name='classes_starting_equipment_class_id_fkey'),
        ForeignKeyConstraint(['equipment_id'], ['equipment.id'], ondelete='CASCADE', name='classes_starting_equipment_equipment_id_fkey'),
        PrimaryKeyConstraint('id', name='classes_starting_equipment_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    quantity: Mapped[int] = mapped_column(Integer)
    class_id: Mapped[Optional[int]] = mapped_column(Integer)
    equipment_id: Mapped[Optional[int]] = mapped_column(Integer)

    class_: Mapped[Optional['Classes']] = relationship('Classes', back_populates='classes_starting_equipment')
    equipment: Mapped[Optional['Equipment']] = relationship('Equipment', back_populates='classes_starting_equipment')


class ClassesStartingEquipmentOptions(Base):
    __tablename__ = 'classes_starting_equipment_options'
    __table_args__ = (
        ForeignKeyConstraint(['class_id'], ['classes.id'], ondelete='CASCADE', name='classes_starting_equipment_options_class_id_fkey'),
        ForeignKeyConstraint(['equipment_id'], ['equipment.id'], ondelete='CASCADE', name='classes_starting_equipment_options_equipment_id_fkey'),
        PrimaryKeyConstraint('id', name='classes_starting_equipment_options_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    class_id: Mapped[Optional[int]] = mapped_column(Integer)
    equipment_id: Mapped[Optional[int]] = mapped_column(Integer)

    class_: Mapped[Optional['Classes']] = relationship('Classes', back_populates='classes_starting_equipment_options')
    equipment: Mapped[Optional['Equipment']] = relationship('Equipment', back_populates='classes_starting_equipment_options')


class EquipmentProperties(Base):
    __tablename__ = 'equipment_properties'
    __table_args__ = (
        ForeignKeyConstraint(['equipment_property_key'], ['equipment.id'], name='equipment_properties_equipment_id_fkey'),
        ForeignKeyConstraint(['weapon_properties_id'], ['weapon_properties.id'], name='equipment_properties_weapon_properties_id_fkey'),
        PrimaryKeyConstraint('id', name='equipment_properties_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    equipment_property_key: Mapped[Optional[int]] = mapped_column(Integer)
    weapon_properties_id: Mapped[Optional[int]] = mapped_column(Integer)

    equipment: Mapped[Optional['Equipment']] = relationship('Equipment', back_populates='equipment_properties')
    weapon_properties: Mapped[Optional['WeaponProperties']] = relationship('WeaponProperties', back_populates='equipment_properties')


t_invocations = Table(
    'invocations', Base.metadata,
    Column('id', Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), nullable=False),
    Column('invocation_id', Integer),
    Column('feature_id', Integer),
    ForeignKeyConstraint(['feature_id'], ['features.id'], ondelete='CASCADE', name='fk_invocation_feature'),
    ForeignKeyConstraint(['invocation_id'], ['feature_specific.invocation_id'], name='fk_invocation_feature_specific')
)


class Levels(Base):
    __tablename__ = 'levels'
    __table_args__ = (
        ForeignKeyConstraint(['class_id'], ['classes.id'], ondelete='CASCADE', name='levels_class_id_fkey'),
        ForeignKeyConstraint(['detail_id'], ['level_detail.id'], ondelete='CASCADE', name='fk_levels_detail'),
        ForeignKeyConstraint(['subclass_id'], ['subclasses.id'], ondelete='SET NULL', name='levels_subclass_id_fkey'),
        PrimaryKeyConstraint('id', name='levels_pkey'),
        UniqueConstraint('url', name='levels_url_key')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    level: Mapped[int] = mapped_column(Integer)
    class_id: Mapped[int] = mapped_column(Integer)
    ability_score_bonuses: Mapped[int] = mapped_column(Integer, server_default=text('0'))
    prof_bonus: Mapped[int] = mapped_column(Integer, server_default=text('0'))
    url: Mapped[str] = mapped_column(Text)
    subclass_id: Mapped[Optional[int]] = mapped_column(Integer)
    detail_id: Mapped[Optional[int]] = mapped_column(Integer)

    class_: Mapped['Classes'] = relationship('Classes', back_populates='levels')
    detail: Mapped[Optional['LevelDetail']] = relationship('LevelDetail', back_populates='levels')
    subclass: Mapped[Optional['Subclasses']] = relationship('Subclasses', back_populates='levels')
    classes_levels: Mapped[List['ClassesLevels']] = relationship('ClassesLevels', back_populates='level')
    spells_subclasses: Mapped[List['SpellsSubclasses']] = relationship('SpellsSubclasses', back_populates='required_level')


class MonsterSpells(Base):
    __tablename__ = 'monster_spells'
    __table_args__ = (
        ForeignKeyConstraint(['monster_special_ability_id'], ['monsters_special_abilities.id'], ondelete='CASCADE', name='monster_spells_monster_special_ability_id_fkey'),
        ForeignKeyConstraint(['spell_id'], ['spells.id'], ondelete='CASCADE', name='monster_spells_spell_id_fkey'),
        PrimaryKeyConstraint('id', name='monster_spells_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    monster_special_ability_id: Mapped[Optional[int]] = mapped_column(Integer)
    spell_id: Mapped[Optional[int]] = mapped_column(Integer)

    monster_special_ability: Mapped[Optional['MonstersSpecialAbilities']] = relationship('MonstersSpecialAbilities', back_populates='monster_spells')
    spell: Mapped[Optional['Spells']] = relationship('Spells', back_populates='monster_spells')


class Proficiencies(Base):
    __tablename__ = 'proficiencies'
    __table_args__ = (
        ForeignKeyConstraint(['reference_ability_score_id'], ['ability_scores.id'], ondelete='SET NULL', name='fk_proficiencies_ability_score'),
        ForeignKeyConstraint(['reference_equipment_category_id'], ['equipment_categories.id'], ondelete='SET NULL', name='fk_proficiencies_equipment_category'),
        ForeignKeyConstraint(['reference_equipment_id'], ['equipment.id'], ondelete='SET NULL', name='fk_proficiencies_equipment'),
        ForeignKeyConstraint(['reference_skill_id'], ['skills.id'], ondelete='SET NULL', name='fk_proficiencies_skill'),
        PrimaryKeyConstraint('id', name='proficiencies_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    type: Mapped[Optional[str]] = mapped_column(String(255))
    url: Mapped[Optional[str]] = mapped_column(String(255))
    reference_equipment_id: Mapped[Optional[int]] = mapped_column(Integer)
    reference_equipment_category_id: Mapped[Optional[int]] = mapped_column(Integer)
    reference_skill_id: Mapped[Optional[int]] = mapped_column(Integer)
    reference_ability_score_id: Mapped[Optional[int]] = mapped_column(Integer)

    reference_ability_score: Mapped[Optional['AbilityScores']] = relationship('AbilityScores', back_populates='proficiencies')
    reference_equipment_category: Mapped[Optional['EquipmentCategories']] = relationship('EquipmentCategories', back_populates='proficiencies')
    reference_equipment: Mapped[Optional['Equipment']] = relationship('Equipment', back_populates='proficiencies')
    reference_skill: Mapped[Optional['Skills']] = relationship('Skills', back_populates='proficiencies')
    class_multi_classing_proficiencies: Mapped[List['ClassMultiClassingProficiencies']] = relationship('ClassMultiClassingProficiencies', back_populates='proficiency')
    classes_proficiencies: Mapped[List['ClassesProficiencies']] = relationship('ClassesProficiencies', back_populates='proficiency')
    classes_proficiency_choices: Mapped[List['ClassesProficiencyChoices']] = relationship('ClassesProficiencyChoices', back_populates='proficiency')
    monster_proficiencies: Mapped[List['MonsterProficiencies']] = relationship('MonsterProficiencies', back_populates='proficiency')
    race_proficiencies: Mapped[List['RaceProficiencies']] = relationship('RaceProficiencies', back_populates='proficiency')
    race_proficiency_options: Mapped[List['RaceProficiencyOptions']] = relationship('RaceProficiencyOptions', back_populates='proficiency')
    subrace_proficiencies: Mapped[List['SubraceProficiencies']] = relationship('SubraceProficiencies', back_populates='proficiency')
    traits: Mapped[List['Traits']] = relationship('Traits', back_populates='proficiencies_')
    trait_options: Mapped[List['TraitOptions']] = relationship('TraitOptions', back_populates='proficiency')
    traits_proficiencies: Mapped[List['TraitsProficiencies']] = relationship('TraitsProficiencies', back_populates='proficiency')


class SpellsClasses(Base):
    __tablename__ = 'spells_classes'
    __table_args__ = (
        ForeignKeyConstraint(['classes_id'], ['classes.id'], name='spells_classes_classes_id_fkey'),
        ForeignKeyConstraint(['spells_id'], ['spells.classes_id'], ondelete='CASCADE', name='spells_classes_spells_id_fkey'),
        PrimaryKeyConstraint('id', name='spells_classes_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    spells_id: Mapped[Optional[int]] = mapped_column(Integer)
    classes_id: Mapped[Optional[int]] = mapped_column(Integer)

    classes: Mapped[Optional['Classes']] = relationship('Classes', back_populates='spells_classes')
    spells: Mapped[Optional['Spells']] = relationship('Spells', back_populates='spells_classes')


class SubclassesClass(Base):
    __tablename__ = 'subclasses_class'
    __table_args__ = (
        ForeignKeyConstraint(['classes_id'], ['classes.id'], name='subclasses_class_classes_id_fkey'),
        ForeignKeyConstraint(['subclasses_id'], ['subclasses.id'], name='subclasses_class_subclasses_id_fkey'),
        PrimaryKeyConstraint('id', name='subclasses_class_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    subclasses_id: Mapped[Optional[int]] = mapped_column(Integer)
    classes_id: Mapped[Optional[int]] = mapped_column(Integer)

    classes: Mapped[Optional['Classes']] = relationship('Classes', back_populates='subclasses_class')
    subclasses: Mapped[Optional['Subclasses']] = relationship('Subclasses', back_populates='subclasses_class')


t_subfeatures = Table(
    'subfeatures', Base.metadata,
    Column('id', Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), nullable=False),
    Column('subfeature_id', Integer),
    Column('feature_id', Integer),
    ForeignKeyConstraint(['feature_id'], ['features.id'], ondelete='CASCADE', name='fk_subfeatures_feature'),
    ForeignKeyConstraint(['subfeature_id'], ['feature_specific.subfeature_id'], ondelete='CASCADE', name='fk_subfeatures_feature_specific')
)


class ClassMultiClassingProficiencies(Base):
    __tablename__ = 'class_multi_classing_proficiencies'
    __table_args__ = (
        ForeignKeyConstraint(['class_id'], ['classes.id'], ondelete='CASCADE', name='class_multi_classing_proficiencies_class_id_fkey'),
        ForeignKeyConstraint(['proficiency_id'], ['proficiencies.id'], ondelete='CASCADE', name='class_multi_classing_proficiencies_proficiency_id_fkey'),
        PrimaryKeyConstraint('id', name='class_multi_classing_proficiencies_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    class_id: Mapped[Optional[int]] = mapped_column(Integer)
    proficiency_id: Mapped[Optional[int]] = mapped_column(Integer)

    class_: Mapped[Optional['Classes']] = relationship('Classes', back_populates='class_multi_classing_proficiencies')
    proficiency: Mapped[Optional['Proficiencies']] = relationship('Proficiencies', back_populates='class_multi_classing_proficiencies')


class ClassesLevels(Base):
    __tablename__ = 'classes_levels'
    __table_args__ = (
        ForeignKeyConstraint(['class_id'], ['classes.id'], ondelete='CASCADE', name='classes_levels_class_id_fkey'),
        ForeignKeyConstraint(['level_id'], ['levels.id'], ondelete='CASCADE', name='classes_levels_level_id_fkey'),
        PrimaryKeyConstraint('id', name='classes_levels_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    class_id: Mapped[Optional[int]] = mapped_column(Integer)
    level_id: Mapped[Optional[int]] = mapped_column(Integer)

    class_: Mapped[Optional['Classes']] = relationship('Classes', back_populates='classes_levels')
    level: Mapped[Optional['Levels']] = relationship('Levels', back_populates='classes_levels')


class ClassesProficiencies(Base):
    __tablename__ = 'classes_proficiencies'
    __table_args__ = (
        ForeignKeyConstraint(['class_id'], ['classes.id'], ondelete='CASCADE', name='classes_proficiencies_class_id_fkey'),
        ForeignKeyConstraint(['proficiency_id'], ['proficiencies.id'], ondelete='CASCADE', name='classes_proficiencies_proficiency_id_fkey'),
        PrimaryKeyConstraint('id', name='classes_proficiencies_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    class_id: Mapped[Optional[int]] = mapped_column(Integer)
    proficiency_id: Mapped[Optional[int]] = mapped_column(Integer)

    class_: Mapped[Optional['Classes']] = relationship('Classes', back_populates='classes_proficiencies')
    proficiency: Mapped[Optional['Proficiencies']] = relationship('Proficiencies', back_populates='classes_proficiencies')


class ClassesProficiencyChoices(Base):
    __tablename__ = 'classes_proficiency_choices'
    __table_args__ = (
        ForeignKeyConstraint(['class_id'], ['classes.id'], ondelete='CASCADE', name='classes_proficiency_choices_class_id_fkey'),
        ForeignKeyConstraint(['proficiency_id'], ['proficiencies.id'], ondelete='CASCADE', name='classes_proficiency_choices_proficiency_id_fkey'),
        PrimaryKeyConstraint('id', name='classes_proficiency_choices_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    class_id: Mapped[Optional[int]] = mapped_column(Integer)
    proficiency_id: Mapped[Optional[int]] = mapped_column(Integer)

    class_: Mapped[Optional['Classes']] = relationship('Classes', back_populates='classes_proficiency_choices')
    proficiency: Mapped[Optional['Proficiencies']] = relationship('Proficiencies', back_populates='classes_proficiency_choices')


t_expertises = Table(
    'expertises', Base.metadata,
    Column('id', Integer, Identity(always=True, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), nullable=False),
    Column('expertise_id', Integer),
    Column('proficiency_id', Integer),
    ForeignKeyConstraint(['expertise_id'], ['feature_specific.expertise_id'], ondelete='CASCADE', name='fk_expertises_feature_specific'),
    ForeignKeyConstraint(['proficiency_id'], ['proficiencies.id'], ondelete='CASCADE', name='fk_expertises_proficiency')
)


class MonsterProficiencies(Base):
    __tablename__ = 'monster_proficiencies'
    __table_args__ = (
        ForeignKeyConstraint(['monster_id'], ['monsters.id'], ondelete='CASCADE', name='fk_monster_proficiencies_to_monsters'),
        ForeignKeyConstraint(['proficiency_id'], ['proficiencies.id'], ondelete='SET NULL', name='monster_proficiencies_proficiency_id_fkey'),
        PrimaryKeyConstraint('id', name='monster_proficiencies_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    monster_id: Mapped[Optional[int]] = mapped_column(Integer)
    proficiency_id: Mapped[Optional[int]] = mapped_column(Integer)
    proficiency_value: Mapped[Optional[int]] = mapped_column(Integer)

    monster: Mapped[Optional['Monsters']] = relationship('Monsters', back_populates='monster_proficiencies')
    proficiency: Mapped[Optional['Proficiencies']] = relationship('Proficiencies', back_populates='monster_proficiencies')


class RaceProficiencies(Base):
    __tablename__ = 'race_proficiencies'
    __table_args__ = (
        ForeignKeyConstraint(['proficiency_id'], ['proficiencies.id'], ondelete='CASCADE', name='fk_rp_proficiency'),
        ForeignKeyConstraint(['race_id'], ['races.id'], ondelete='CASCADE', name='fk_rp_race'),
        PrimaryKeyConstraint('id', name='race_proficiencies_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    race_id: Mapped[int] = mapped_column(Integer)
    proficiency_id: Mapped[int] = mapped_column(Integer)

    proficiency: Mapped['Proficiencies'] = relationship('Proficiencies', back_populates='race_proficiencies')
    race: Mapped['Races'] = relationship('Races', back_populates='race_proficiencies')


class RaceProficiencyOptions(Base):
    __tablename__ = 'race_proficiency_options'
    __table_args__ = (
        ForeignKeyConstraint(['proficiency_id'], ['proficiencies.id'], ondelete='CASCADE', name='fk_rpo_proficiency'),
        ForeignKeyConstraint(['race_id'], ['races.id'], ondelete='CASCADE', name='fk_rpo_race'),
        PrimaryKeyConstraint('id', name='race_proficiency_options_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    race_id: Mapped[int] = mapped_column(Integer)
    proficiency_id: Mapped[int] = mapped_column(Integer)

    proficiency: Mapped['Proficiencies'] = relationship('Proficiencies', back_populates='race_proficiency_options')
    race: Mapped['Races'] = relationship('Races', back_populates='race_proficiency_options')


class SpellsSubclasses(Base):
    __tablename__ = 'spells_subclasses'
    __table_args__ = (
        ForeignKeyConstraint(['required_feature_id'], ['features.id'], ondelete='SET NULL', name='spells_subclasses_required_feature_id_fkey'),
        ForeignKeyConstraint(['required_level_id'], ['levels.id'], ondelete='SET NULL', name='spells_subclasses_required_level_id_fkey'),
        ForeignKeyConstraint(['spells_id'], ['spells.classes_id'], ondelete='CASCADE', name='spells_subclasses_spells_id_fkey'),
        ForeignKeyConstraint(['subclasses_id'], ['subclasses.id'], name='spells_subclasses_subclasses_id_fkey'),
        PrimaryKeyConstraint('id', name='spells_subclasses_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    spells_id: Mapped[Optional[int]] = mapped_column(Integer)
    subclasses_id: Mapped[Optional[int]] = mapped_column(Integer)
    required_level_id: Mapped[Optional[int]] = mapped_column(Integer)
    required_feature_id: Mapped[Optional[int]] = mapped_column(Integer)

    required_feature: Mapped[Optional['Features']] = relationship('Features', back_populates='spells_subclasses')
    required_level: Mapped[Optional['Levels']] = relationship('Levels', back_populates='spells_subclasses')
    spells: Mapped[Optional['Spells']] = relationship('Spells', back_populates='spells_subclasses')
    subclasses: Mapped[Optional['Subclasses']] = relationship('Subclasses', back_populates='spells_subclasses')


class SubraceProficiencies(Base):
    __tablename__ = 'subrace_proficiencies'
    __table_args__ = (
        ForeignKeyConstraint(['proficiency_id'], ['proficiencies.id'], ondelete='CASCADE', name='fk_subrace_proficiencies_to_proficiencies'),
        ForeignKeyConstraint(['subrace_id'], ['subraces.id'], ondelete='CASCADE', name='fk_subrace_proficiencies_to_subraces'),
        PrimaryKeyConstraint('id', name='subrace_proficiencies_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    subrace_id: Mapped[int] = mapped_column(Integer)
    proficiency_id: Mapped[int] = mapped_column(Integer)

    proficiency: Mapped['Proficiencies'] = relationship('Proficiencies', back_populates='subrace_proficiencies')
    subrace: Mapped['Subraces'] = relationship('Subraces', back_populates='subrace_proficiencies')


class Traits(Base):
    __tablename__ = 'traits'
    __table_args__ = (
        ForeignKeyConstraint(['parent'], ['traits.id'], ondelete='SET NULL', name='fk_traits_parent'),
        ForeignKeyConstraint(['proficiencies'], ['proficiencies.id'], ondelete='SET NULL', name='fk_traits_proficiency'),
        ForeignKeyConstraint(['subrace_id'], ['subraces.id'], ondelete='SET NULL', name='fk_traits_subrace'),
        PrimaryKeyConstraint('id', name='traits_pkey'),
        UniqueConstraint('trait_proficiency_id', name='unique_trait_proficiency_id')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    description: Mapped[Optional[str]] = mapped_column(Text)
    name: Mapped[Optional[str]] = mapped_column(String(255))
    proficiencies: Mapped[Optional[int]] = mapped_column(Integer, comment='trait_proficiencies table identity')
    races: Mapped[Optional[int]] = mapped_column(Integer, comment='trait_races table identity')
    subrace_id: Mapped[Optional[int]] = mapped_column(Integer)
    url: Mapped[Optional[str]] = mapped_column(String(255))
    parent: Mapped[Optional[int]] = mapped_column(Integer)
    extra_language: Mapped[Optional[int]] = mapped_column(Integer)
    trait_proficiency_id: Mapped[Optional[int]] = mapped_column(Integer, comment='traits_options table identity')

    traits: Mapped[Optional['Traits']] = relationship('Traits', remote_side=[id], back_populates='traits_reverse')
    traits_reverse: Mapped[List['Traits']] = relationship('Traits', remote_side=[parent], back_populates='traits')
    proficiencies_: Mapped[Optional['Proficiencies']] = relationship('Proficiencies', back_populates='traits')
    subrace: Mapped[Optional['Subraces']] = relationship('Subraces', back_populates='traits')
    race_traits: Mapped[List['RaceTraits']] = relationship('RaceTraits', back_populates='trait')
    subrace_traits: Mapped[List['SubraceTraits']] = relationship('SubraceTraits', back_populates='trait')
    trait_options: Mapped[List['TraitOptions']] = relationship('TraitOptions', foreign_keys='[TraitOptions.option_id]', back_populates='option')
    trait_options_: Mapped[List['TraitOptions']] = relationship('TraitOptions', foreign_keys='[TraitOptions.subtrait_id]', back_populates='subtrait')
    traits_proficiencies: Mapped[List['TraitsProficiencies']] = relationship('TraitsProficiencies', back_populates='trait')
    traits_races: Mapped[List['TraitsRaces']] = relationship('TraitsRaces', back_populates='traits')


class RaceTraits(Base):
    __tablename__ = 'race_traits'
    __table_args__ = (
        ForeignKeyConstraint(['race_id'], ['races.id'], ondelete='CASCADE', name='fk_rt_race'),
        ForeignKeyConstraint(['trait_id'], ['traits.id'], ondelete='CASCADE', name='fk_rt_trait'),
        PrimaryKeyConstraint('id', name='race_traits_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    race_id: Mapped[int] = mapped_column(Integer)
    trait_id: Mapped[int] = mapped_column(Integer)

    race: Mapped['Races'] = relationship('Races', back_populates='race_traits')
    trait: Mapped['Traits'] = relationship('Traits', back_populates='race_traits')


class SubraceTraits(Base):
    __tablename__ = 'subrace_traits'
    __table_args__ = (
        ForeignKeyConstraint(['subrace_id'], ['subraces.id'], ondelete='CASCADE', name='fk_subrace_traits_to_subraces'),
        ForeignKeyConstraint(['trait_id'], ['traits.id'], ondelete='CASCADE', name='fk_subrace_traits_to_traits'),
        PrimaryKeyConstraint('id', name='subrace_traits_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    subrace_id: Mapped[int] = mapped_column(Integer)
    trait_id: Mapped[int] = mapped_column(Integer)

    subrace: Mapped['Subraces'] = relationship('Subraces', back_populates='subrace_traits')
    trait: Mapped['Traits'] = relationship('Traits', back_populates='subrace_traits')


class TraitOptions(Base):
    __tablename__ = 'trait_options'
    __table_args__ = (
        ForeignKeyConstraint(['option_id'], ['traits.trait_proficiency_id'], ondelete='SET NULL', name='trait_options_option_id_fkey'),
        ForeignKeyConstraint(['proficiency_id'], ['proficiencies.id'], ondelete='SET NULL', name='trait_options_proficiency_id_fkey'),
        ForeignKeyConstraint(['spell_id'], ['spells.id'], ondelete='SET NULL', name='trait_options_spell_id_fkey'),
        ForeignKeyConstraint(['subtrait_id'], ['traits.id'], ondelete='SET NULL', name='trait_options_subtrait_id_fkey'),
        PrimaryKeyConstraint('id', name='trait_options_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    choose: Mapped[Optional[int]] = mapped_column(Integer)
    type: Mapped[Optional[str]] = mapped_column(String(50))
    option_id: Mapped[Optional[int]] = mapped_column(Integer)
    subtrait_id: Mapped[Optional[int]] = mapped_column(Integer)
    spell_id: Mapped[Optional[int]] = mapped_column(Integer)
    proficiency_id: Mapped[Optional[int]] = mapped_column(Integer)

    option: Mapped[Optional['Traits']] = relationship('Traits', foreign_keys=[option_id], back_populates='trait_options')
    proficiency: Mapped[Optional['Proficiencies']] = relationship('Proficiencies', back_populates='trait_options')
    spell: Mapped[Optional['Spells']] = relationship('Spells', back_populates='trait_options')
    subtrait: Mapped[Optional['Traits']] = relationship('Traits', foreign_keys=[subtrait_id], back_populates='trait_options_')


class TraitsProficiencies(Base):
    __tablename__ = 'traits_proficiencies'
    __table_args__ = (
        ForeignKeyConstraint(['proficiency_id'], ['proficiencies.id'], ondelete='CASCADE', name='traits_proficiencies_proficiency_id_fkey'),
        ForeignKeyConstraint(['trait_id'], ['traits.id'], ondelete='CASCADE', name='traits_proficiencies_trait_id_fkey'),
        PrimaryKeyConstraint('id', name='traits_proficiencies_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    trait_id: Mapped[Optional[int]] = mapped_column(Integer)
    proficiency_id: Mapped[Optional[int]] = mapped_column(Integer)

    proficiency: Mapped[Optional['Proficiencies']] = relationship('Proficiencies', back_populates='traits_proficiencies')
    trait: Mapped[Optional['Traits']] = relationship('Traits', back_populates='traits_proficiencies')


class TraitsRaces(Base):
    __tablename__ = 'traits_races'
    __table_args__ = (
        ForeignKeyConstraint(['races_id'], ['races.id'], name='traits_races_races_id_fkey'),
        ForeignKeyConstraint(['traits_id'], ['traits.id'], name='traits_races_traits_id_fkey'),
        PrimaryKeyConstraint('id', name='traits_races_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    traits_id: Mapped[Optional[int]] = mapped_column(Integer)
    races_id: Mapped[Optional[int]] = mapped_column(Integer)

    races: Mapped[Optional['Races']] = relationship('Races', back_populates='traits_races')
    traits: Mapped[Optional['Traits']] = relationship('Traits', back_populates='traits_races')


class RaceSpeedDefault(Base):
    __tablename__ = 'race_speed_defaults'
    __table_args__ = (
        ForeignKeyConstraint(['race_id'], ['races.id'], ondelete='CASCADE', name='rsd_race_id_fkey'),
        ForeignKeyConstraint(['size_id'], ['character_sizes.id'], ondelete='CASCADE', name='rsd_size_id_fkey'),
        PrimaryKeyConstraint('id', name='race_speed_defaults_pkey')
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    race_id: Mapped[int] = mapped_column(Integer, nullable=False)
    size_id: Mapped[int] = mapped_column(Integer, nullable=False)
    base_speed: Mapped[int] = mapped_column(Integer, nullable=False)

    race: Mapped[Optional['Races']] = relationship('Races', back_populates='race_speeds')
    size: Mapped[Optional['CharacterSize']] = relationship('CharacterSize', back_populates='race_speeds')

class CharacterSize(Base):
    __tablename__ = 'character_sizes'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='character_sizes_pkey'),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(Text)

    race_speeds: Mapped[List['RaceSpeedDefault']] = relationship('RaceSpeedDefault', back_populates='size')

