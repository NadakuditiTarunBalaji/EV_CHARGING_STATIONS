from flask import Flask
from flask_cors import CORS
from models import db
from routes.routes import register_routes
import os

app = Flask(__name__)

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_PATH = os.path.join(BASE_DIR, "ev_saas.db")

app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_PATH}"
db.init_app(app)
CORS(app)

register_routes(app)

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)