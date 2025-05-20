from flask import Flask
from flasgger import Swagger
from routes.classes import classes_bp
from routes.auth import auth_bp
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "fallback-secret-if-not-set")
swagger = Swagger(app)

app.register_blueprint(classes_bp)
app.register_blueprint(auth_bp)


if __name__ == "__main__":
    app.run(debug=True)