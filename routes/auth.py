from flask import Blueprint, request, jsonify, current_app
from flasgger import swag_from
from flask_jwt_extended import create_access_token
from sqlalchemy.exc import IntegrityError
from config import SessionLocal
from models.player import User
from werkzeug.security import generate_password_hash, check_password_hash
import re

auth_bp = Blueprint('auth', __name__, url_prefix='/api/users')

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# ---------------------- REGISTER ----------------------
@auth_bp.route('/register', methods=['POST'])
@swag_from({
    'tags': ['Auth'],
    'consumes': ['application/x-www-form-urlencoded'],
    'parameters': [
        {'name': 'username', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'email', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'password', 'in': 'formData', 'type': 'string', 'required': True}
    ],
    'responses': {
        200: {'description': 'Kullanıcı başarıyla oluşturuldu'},
        400: {'description': 'Geçersiz istek'},
        409: {'description': 'Kullanıcı zaten mevcut'},
        500: {'description': 'Sunucu hatası'}
    }
})
def register():
    data = request.form
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Tüm alanlar zorunludur'}), 400

    if not is_valid_email(email):
        return jsonify({'error': 'Geçerli bir e-posta adresi girin'}), 400

    if len(password) < 6:
        return jsonify({'error': 'Şifre en az 6 karakter olmalıdır'}), 400

    session = SessionLocal()
    try:
        if session.query(User).filter_by(email=email).first():
            return jsonify({'error': 'Bu e-posta adresi zaten kullanılıyor'}), 409

        hashed_pw = generate_password_hash(password)
        user = User(username=username, email=email, password_hash=hashed_pw)
        session.add(user)
        session.commit()

        return jsonify({'message': 'Kullanıcı oluşturuldu'}), 200
    except IntegrityError:
        session.rollback()
        return jsonify({'error': 'Veritabanı hatası'}), 500
    finally:
        session.close()

# ---------------------- LOGIN ----------------------
@auth_bp.route('/login', methods=['POST'])
@swag_from({
    'tags': ['Auth'],
    'summary': 'Kullanıcı girişi',
    'description': 'Email ve şifre ile giriş yaparak JWT token döner',
    'requestBody': {
        'required': True,
        'content': {
            'application/json': {
                'schema': {
                    'type': 'object',
                    'properties': {
                        'email': {'type': 'string', 'example': 'ahmet@gmail.com'},
                        'password': {'type': 'string', 'example': 'ahmet'}
                    },
                    'required': ['email', 'password']
                }
            }
        }
    },
    'responses': {
        200: {
            'description': 'Giriş başarılı - JWT token döner',
            'schema': {
                'type': 'object',
                'properties': {
                    'access_token': {'type': 'string'}
                }
            }
        },
        400: {'description': 'Eksik bilgi'},
        401: {'description': 'Geçersiz giriş bilgileri'}
    }
})
def login():
    session = SessionLocal()
    try:
        data = request.get_json(silent=True)
        if not data or 'email' not in data or 'password' not in data:
            return jsonify({'error': 'Email ve şifre zorunludur'}), 400

        user = session.query(User).filter_by(email=data['email']).first()
        if user and check_password_hash(user.password_hash, data['password']):
            access_token = create_access_token(identity=str(user.id))
            print("LOGIN user.id (type):", user.id, type(user.id))
            print("identity (str):", str(user.id), type(str(user.id)))
            return jsonify({'access_token': access_token}), 200

        return jsonify({'error': 'Geçersiz giriş bilgileri'}), 401
    finally:
        session.close()
