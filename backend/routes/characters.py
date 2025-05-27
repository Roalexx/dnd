from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy.exc import IntegrityError
from config import SessionLocal
from models.player.character import Character 
from schemas.character_creation_schema import CharacterSchema
from flasgger import swag_from
from flask_cors import cross_origin

character_bp = Blueprint('character', __name__, url_prefix='/api/characters')

#-------------------Create-Character------------------------------------------
@character_bp.route('', methods=['POST'])
@jwt_required()
@swag_from({
    'tags': ['Characters'],
    'summary': 'Yeni karakter oluştur',
    'security': [{'BearerAuth': []}],
    'description': 'JWT token ile giriş yapan kullanıcı, karakterini oluşturabilir.',
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'name': {'type': 'string', 'example': 'Arthas'},
                        'class_id': {'type': 'integer', 'example': 1},
                        'subclass_id': {'type': 'integer', 'example': 2},
                        'race_id': {'type': 'integer', 'example': 3},
                        'feat_id': {'type': 'integer', 'example': None},
                        'alignment_id': {'type': 'integer', 'example': 4},
                        'level': {'type': 'integer', 'example': 3},
                        'experience': {'type': 'integer', 'example': 900},
                        'hit_points': {'type': 'integer', 'example': 28},
                        'armor_class': {'type': 'integer', 'example': 17},
                        'speed': {'type': 'integer', 'example': 30},
                        'character_size_id': {
                            'type': 'integer',
                            'example': 3,
                            'description': 'Boyut kimliği (örneğin Medium = 3)'
                        },
                        'ability_scores': {
                            'type': 'object',
                            'properties': {
                                'strength': {'type': 'integer', 'example': 16},
                                'dexterity': {'type': 'integer', 'example': 12},
                                'constitution': {'type': 'integer', 'example': 14},
                                'intelligence': {'type': 'integer', 'example': 10},
                                'wisdom': {'type': 'integer', 'example': 11},
                                'charisma': {'type': 'integer', 'example': 15}
                            }
                        },
                        'currency': {
                            'type': 'object',
                            'properties': {
                                'gold': {'type': 'integer', 'example': 20},
                                'silver': {'type': 'integer', 'example': 3},
                                'copper': {'type': 'integer', 'example': 5}
                            }
                        },
                        'text_blocks': {
                            'type': 'object',
                            'properties': {
                                'personality': {'type': 'string', 'example': 'Kind but reserved'},
                                'ideals': {'type': 'string', 'example': 'Protect the weak'},
                                'bonds': {'type': 'string', 'example': 'Sworn to defend the realm'},
                                'flaws': {'type': 'string', 'example': 'Impulsive'},
                                'notes': {'type': 'string', 'example': 'Carries a lucky charm'}
                            }
                        },
                        'image_url': {'type': 'string', 'example': 'https://example.com/image.png'}
                    },
                    'required': ['name', 'class_id', 'race_id', 'alignment_id', 'ability_scores', 'hit_points', 'armor_class', 'speed']
                }
            }
        }
    },
    'responses': {
        201: {
            'description': 'Karakter başarıyla oluşturuldu',
            'content': {
                'application/json': {
                    'schema': {
                        'type': 'object',
                        'properties': {
                            'message': {'type': 'string'},
                            'character_id': {'type': 'integer'}
                        }
                    }
                }
            }
        },
        400: {'description': 'Hatalı istek'},
        500: {'description': 'Sunucu hatası'}
    }
})
def create_character():
    session = SessionLocal()
    try:
        json_data = request.get_json()
        if not json_data:
            return jsonify({"error": "JSON body bekleniyor"}), 400

        user_id = get_jwt_identity()
        schema = CharacterSchema()
        data = schema.load(json_data)

        new_char = Character(
            user_id = int(get_jwt_identity()),
            name=data['name'],
            class_id=data['class_id'],
            subclass_id=data.get('subclass_id'),
            race_id=data['race_id'],
            feat_id=data.get('feat_id'),
            alignment_id=data.get('alignment_id'),
            character_size_id=data['character_size_id'],
            level=data.get('level', 1),
            experience=data.get('experience', 0),
            strength=data['ability_scores']['strength'],
            dexterity=data['ability_scores']['dexterity'],
            constitution=data['ability_scores']['constitution'],
            intelligence=data['ability_scores']['intelligence'],
            wisdom=data['ability_scores']['wisdom'],
            charisma=data['ability_scores']['charisma'],
            hit_points=data['hit_points'],
            armor_class=data['armor_class'],
            speed=data['speed'],
            gold=data['currency'].get('gold', 0),
            silver=data['currency'].get('silver', 0),
            copper=data['currency'].get('copper', 0),
            personality=data.get('text_blocks', {}).get('personality'),
            ideals=data.get('text_blocks', {}).get('ideals'),
            bonds=data.get('text_blocks', {}).get('bonds'),
            flaws=data.get('text_blocks', {}).get('flaws'),
            notes=data.get('text_blocks', {}).get('notes'),
            image_url=data.get('image_url')
        )

        session.add(new_char)
        session.commit()

        return jsonify({
            "message": "Karakter başarıyla oluşturuldu",
            "character_id": new_char.id
        }), 201

    except IntegrityError:
        session.rollback()
        return jsonify({"error": "Veritabanı hatası"}), 400
    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500
    finally:
        session.close()


#--------------------My-Character----------------------------------------------
@character_bp.route('/my-characters', methods=['GET'])
@jwt_required()
@swag_from({
    'tags': ['Characters'],
    'summary': 'Kullanıcının sahip olduğu ve yönettiği karakterleri getirir',
    'security': [{'BearerAuth': []}],
    'description': 'JWT token ile giriş yapmış kullanıcının hem sahibi olduğu karakterler hem de dungeon master olarak yönettiği karakterler döner.',
    'responses': {
        200: {
            'description': 'Karakter listesi başarıyla getirildi',
            'examples': {
                'application/json': {
                    "owned_characters": [
                        {
                            "id": 1,
                            "name": "Thorin",
                            "level": 3,
                            "class": 2,
                            "race": 1
                        }
                    ],
                    "dm_characters": [
                        {
                            "id": 5,
                            "name": "Luna",
                            "level": 7,
                            "class": 4,
                            "race": 3
                        }
                    ]
                }
            }
        },
        401: {'description': 'Yetkisiz'}
    }
})
def get_my_characters():
    user_id = get_jwt_identity()
    session = SessionLocal()

    try:
        owned = session.query(Character).filter_by(user_id=user_id).all()
        dm = session.query(Character).filter_by(dungeon_master_id=user_id).all()

        def serialize(char):
            return {
                "id": char.id,
                "name": char.name,
                "level": char.level,
                "experience": char.experience,
                "class_id": char.class_id,
                "subclass_id": char.subclass_id,
                "race_id": char.race_id,
                "feat_id": char.feat_id,
                "alignment_id": char.alignment_id,
                "strength": char.strength,
                "dexterity": char.dexterity,
                "constitution": char.constitution,
                "intelligence": char.intelligence,
                "wisdom": char.wisdom,
                "charisma": char.charisma,
                "hit_points": char.hit_points,
                "armor_class": char.armor_class,
                "speed": char.speed,
                "gold": char.gold,
                "silver": char.silver,
                "copper": char.copper,
                "personality": char.personality,
                "ideals": char.ideals,
                "bonds": char.bonds,
                "flaws": char.flaws,
                "image_url": char.image_url,
                "notes": char.notes,
                "created_at": char.created_at.isoformat() if char.created_at else None,
                "is_admin": char.is_admin,
                "user_id": char.user_id,
                "dungeon_master_id": char.dungeon_master_id
            }


        return jsonify({
            "owned_characters": [serialize(c) for c in owned],
            "dm_characters": [serialize(c) for c in dm]
        }), 200

    finally:
        session.close()

#--------------------Get-By-ID--------------------------------------------------
@character_bp.route('/<int:character_id>', methods=['GET'])
@jwt_required()
@swag_from({
    'tags': ['Characters'],
    'summary': 'Karakter detaylarını getirir',
    'description': 'Belirli bir karakterin detaylarını döner. Sadece karakter sahibi veya Dungeon Master erişebilir.',
    'parameters': [
        {
            'name': 'character_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'Karakter ID'
        }
    ],
    'security': [{'BearerAuth': []}],
    'responses': {
        200: {
            'description': 'Karakter başarıyla bulundu',
            'examples': {
                'application/json': {
                    "id": 1,
                    "name": "Thorin",
                    "class_id": 2,
                    "race_id": 1,
                    "level": 3,
                    "hit_points": 20,
                    "armor_class": 15,
                    "speed": 30,
                    "ability_scores": {
                        "strength": 16,
                        "dexterity": 12,
                        "constitution": 14,
                        "intelligence": 10,
                        "wisdom": 13,
                        "charisma": 8
                    },
                    "currency": {
                        "gold": 10,
                        "silver": 5,
                        "copper": 2
                    },
                    "spells": [{"id": 1, "name": "Firebolt", "level": 0}],
                    "equipment": [{"id": 2, "name": "Longsword", "quantity": 1, "category": "Weapon"}]
                    # ... diğer alanlar ...
                }
            }
        },
        403: {'description': 'Erişim reddedildi'},
        404: {'description': 'Karakter bulunamadı'}
    }
})
def get_character_detail(character_id):
    session = SessionLocal()
    user_id = get_jwt_identity()

    try:
        character = session.query(Character).filter_by(id=character_id).first()

        if not character:
            return jsonify({'error': 'Karakter bulunamadı'}), 404

        if int(character.user_id) != int(user_id) and int(character.dungeon_master_id or -1) != int(user_id):
            return jsonify({'error': 'Bu karaktere erişim izniniz yok'}), 403

        character_data = CharacterSchema().dump(character)
        return jsonify(character_data), 200

    finally:
        session.close()

