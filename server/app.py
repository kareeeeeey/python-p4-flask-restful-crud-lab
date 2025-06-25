from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from server.config import Config
from server.models import db
from server.routes import plant_bp

app = Flask(__name__)
app.config.from_object(Config)

CORS(app)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(plant_bp, url_prefix="/plants")

if __name__ == "__main__":
    app.run(port=5559, debug=True)
