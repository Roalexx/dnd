from flask import Blueprint, request, jsonify, current_app
from flasgger import swag_from
import jwt
from sqlalchemy.exc import IntegrityError
from config import SessionLocal
from models.player import User
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
import re

auth_bp = Blueprint('auth', __name__, url_prefix='/api/users')

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

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

    # Validasyonlar
    if not username or not email or not password:
        return jsonify({'error': 'Tüm alanlar zorunludur'}), 400

    if not is_valid_email(email):
        return jsonify({'error': 'Geçerli bir e-posta adresi girin'}), 400

    if len(password) < 6:
        return jsonify({'error': 'Şifre en az 6 karakter olmalıdır'}), 400

    session = SessionLocal()
    try:
        hashed_pw = generate_password_hash(password)
        user = User(username=username, email=email, password_hash=hashed_pw)
        session.add(user)
        session.commit()
        return jsonify({'message': 'Kullanıcı oluşturuldu'}), 200
    except IntegrityError:
        session.rollback()
        return jsonify({'error': 'Kullanıcı zaten mevcut'}), 409
    except Exception as e:
        session.rollback()
        return jsonify({'error': str(e)}), 500
    finally:
        session.close()


@auth_bp.route('/login', methods=['POST'])
@swag_from({
    'tags': ['Auth'],
    'consumes': ['application/x-www-form-urlencoded'],
    'parameters': [
        {'name': 'email', 'in': 'formData', 'type': 'string', 'required': True},
        {'name': 'password', 'in': 'formData', 'type': 'string', 'required': True}
    ],
    'responses': {
        200: {
            'description': 'Giriş başarılı - Token döner',
            'examples': {
                'application/json': {
                    'access_token': 'eyJ0eXAiOiJKV1QiLCJh...'
                }
            }
        },
        401: {'description': 'Geçersiz giriş bilgileri'}
    }
})
def login():
    data = request.form
    session = SessionLocal()
    try:
        user = session.query(User).filter_by(email=data['email']).first()
        if user and check_password_hash(user.password_hash, data['password']):
            payload = {
                'user_id': user.id,
                'username': user.username,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
            }
            token = jwt.encode(payload, current_app.config['SECRET_KEY'], algorithm='HS256')
            return jsonify({'access_token': token}), 200

        return jsonify({'error': 'Geçersiz giriş bilgileri'}), 401
    finally:
        session.close()