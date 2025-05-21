from flask import Flask
from flasgger import Swagger
from routes.classes import classes_bp
from routes.auth import auth_bp
from routes.characters import character_bp
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "fallback-secret-if-not-set")
app.config['JWT_SECRET_KEY'] = app.config['SECRET_KEY']
jwt = JWTManager(app)
app.config['SWAGGER'] = {
    'title': 'DnD API',
    'uiversion': 3,
    'openapi': '3.0.2',
    'components': {
        'securitySchemes': {
            'BearerAuth': {
                'type': 'http',
                'scheme': 'bearer',
                'bearerFormat': 'JWT'
            }
        }
    },
    'security': [
        {
            'BearerAuth': []
        }
    ]
}

swagger = Swagger(app)

app.register_blueprint(classes_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(character_bp)



if __name__ == "__main__":
    app.run(debug=True)