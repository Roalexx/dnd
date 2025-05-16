from flask import Flask
from flasgger import Swagger
from routes.classes import classes_bp
from routes.monsters import monsters_bp

app = Flask(__name__)
swagger = Swagger(app)

app.register_blueprint(classes_bp)
app.register_blueprint(monsters_bp)

if __name__ == "__main__":
    app.run(debug=True)