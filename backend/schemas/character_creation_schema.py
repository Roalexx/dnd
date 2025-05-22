from marshmallow import Schema, fields

# -------- Temel Alt Şemalar --------

class AbilityScoreSchema(Schema):
    strength = fields.Integer(required=True)
    dexterity = fields.Integer(required=True)
    constitution = fields.Integer(required=True)
    intelligence = fields.Integer(required=True)
    wisdom = fields.Integer(required=True)
    charisma = fields.Integer(required=True)

class CurrencySchema(Schema):
    gold = fields.Integer(load_default=0)
    silver = fields.Integer(load_default=0)
    copper = fields.Integer(load_default=0)

class TextBlockSchema(Schema):
    personality = fields.String(allow_none=True)
    ideals = fields.String(allow_none=True)
    bonds = fields.String(allow_none=True)
    flaws = fields.String(allow_none=True)
    notes = fields.String(allow_none=True)

# -------- Alt İlişkiler --------

class CharacterSpellSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    level = fields.Integer(allow_none=True)

class CharacterEquipmentSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    quantity = fields.Integer(allow_none=True)
    category = fields.String(allow_none=True)

class CharacterLanguageSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)

class CharacterSkillSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    ability_score = fields.String(allow_none=True)

class CharacterTraitSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(allow_none=True)

class CharacterSavingThrowSchema(Schema):
    id = fields.Integer(required=True)
    ability_score = fields.String(required=True)
    value = fields.Integer(required=True)

class CharacterConditionSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    description = fields.String(allow_none=True)

# -------- Ana Karakter Şeması --------

class CharacterSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True)

    class_id = fields.Integer(required=True)
    subclass_id = fields.Integer(allow_none=True)
    race_id = fields.Integer(required=True)
    feat_id = fields.Integer(allow_none=True)
    alignment_id = fields.Integer(required=True) 

    level = fields.Integer(load_default=1)
    experience = fields.Integer(load_default=0)

    ability_scores = fields.Nested(AbilityScoreSchema, required=True)
    hit_points = fields.Integer(required=True)
    armor_class = fields.Integer(required=True)
    character_size_id = fields.Integer(required=True)
    speed = fields.Integer(required=True)

    currency = fields.Nested(CurrencySchema, load_default={})
    background = fields.String(allow_none=True)
    text_blocks = fields.Nested(TextBlockSchema, allow_none=True)

    image_url = fields.String(allow_none=True)
    created_at = fields.DateTime(dump_only=True)

    spells = fields.List(fields.Nested(CharacterSpellSchema), dump_only=True)
    equipment = fields.List(fields.Nested(CharacterEquipmentSchema), dump_only=True)
    languages = fields.List(fields.Nested(CharacterLanguageSchema), dump_only=True)
    skills = fields.List(fields.Nested(CharacterSkillSchema), dump_only=True)
    traits = fields.List(fields.Nested(CharacterTraitSchema), dump_only=True)
    saving_throws = fields.List(fields.Nested(CharacterSavingThrowSchema), dump_only=True)
    conditions = fields.List(fields.Nested(CharacterConditionSchema), dump_only=True)
