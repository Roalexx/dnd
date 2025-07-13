from marshmallow import Schema, fields, validate

class AbilityScoresSchema(Schema):
    strength = fields.Int(required=True, validate=validate.Range(min=1))
    dexterity = fields.Int(required=True, validate=validate.Range(min=1))
    constitution = fields.Int(required=True, validate=validate.Range(min=1))
    intelligence = fields.Int(required=True, validate=validate.Range(min=1))
    wisdom = fields.Int(required=True, validate=validate.Range(min=1))
    charisma = fields.Int(required=True, validate=validate.Range(min=1))

class CharacterSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))

    class_id = fields.Int(required=True)
    subclass_id = fields.Int(allow_none=True)
    race_id = fields.Int(required=True)
    alignment_id = fields.Int(required=True)
    character_size_id = fields.Int(required=True)

    feat_id = fields.Int(allow_none=True)

    level = fields.Int(load_default=1, validate=validate.Range(min=1))
    experience = fields.Int(load_default=0, validate=validate.Range(min=0))

    ability_scores = fields.Nested(AbilityScoresSchema)

    hit_points = fields.Int(required=True)
    armor_class = fields.Int(required=True)
    speed = fields.Int(required=True)

    gold = fields.Int(load_default=0)
    silver = fields.Int(load_default=0)
    copper = fields.Int(load_default=0)

    text_blocks = fields.Dict()           # personality / ideals / bonds / flaws
    notes = fields.Str(allow_none=True)
    image_url = fields.Url(allow_none=True)

    dungeon_master_id = fields.Int(allow_none=True)

    is_admin = fields.Bool(dump_only=True)
    created_at = fields.DateTime(dump_only=True)