from functools import wraps
from flask import request, jsonify, current_app
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({'message': 'Token gerekli'}), 401

        token = auth_header.split(" ")[1]

        try:
            decoded = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            request.user = decoded
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token süresi dolmuş'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Geçersiz token'}), 401

        return f(*args, **kwargs)
    return decorated
