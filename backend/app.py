from flask import Flask
from flasgger import Swagger
#from routes.classes import classes_bp
from routes.auth import auth_bp
from routes.characters import character_bp
from routes.character_detail import character_data_bp
from routes.drop_down import sizes_bp, alignments_bp, classes_bp, races_bp
from routes.equipments import equipment_bp
from routes.class_levels import levels_bp
from routes.char_info_for_battle import char_info_bp
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from flask_cors import CORS
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "fallback-secret-if-not-set")
app.config['JWT_SECRET_KEY'] = app.config['SECRET_KEY']
jwt = JWTManager(app)
app.config["SWAGGER"] = {
    "title": "DnD API",
    "uiversion": 3,
    "swagger": "2.0",
    "securityDefinitions": {
        "BearerAuth": {
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "JWT token. Örnek: Bearer <token>"
        }
    },
    "security": [
        {
            "BearerAuth": []
        }
    ]
}


CORS(app, supports_credentials=True)
swagger = Swagger(app)

app.register_blueprint(classes_bp)
app.register_blueprint(races_bp)
app.register_blueprint(alignments_bp)
app.register_blueprint(sizes_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(character_bp)
app.register_blueprint(character_data_bp)
app.register_blueprint(equipment_bp)
app.register_blueprint(levels_bp)
app.register_blueprint(char_info_bp)


if __name__ == "__main__":
    app.run(debug=True)

    