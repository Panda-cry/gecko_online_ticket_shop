import os
from flask import Flask
from flask_smorest import Api
from db import db
from web_bcrypt import app_bcrypt
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_cors import  CORS
import logging
# from application_layer.user_auth import auth_blueprint
from presentation_layer import auth_blueprint, admin_blueprint,user_blueprint,seller_blueprint
load_dotenv()


UPLOAD_FOLDER = os.getenv("IMAGE_LOCATION")
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)


def create_app():
    app = Flask(__name__)

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config["PROPAGETE_EXCEPTIONS"] = os.getenv('PROPAGETE_EXCEPTIONS')
    app.config["API_TITLE"] = os.getenv("API_TITLE")
    app.config["API_VERSION"] = os.getenv("API_VERSION")
    app.config["OPENAPI_VERSION"] = os.getenv("OPENAPI_VERSION")
    app.config["OPENAPI_URL_PREFIX"] = os.getenv("OPENAPI_URL_PREFIX")
    app.config["OPENAPI_SWAGGER_UI_PATH"] = os.getenv(
        "OPENAPI_SWAGGER_UI_PATH")
    app.config[
        "OPENAPI_SWAGGER_UI_URL"] = os.getenv("OPENAPI_SWAGGER_UI_URL")
    app.config[
        "SQLALCHEMY_DATABASE_URI"] = os.getenv("SQLALCHEMY_DATABASE_URI")
    app.config[
        'SQLALCHEMY_TRACK_MODIFICATIONS'] = os.getenv(
        "SQLALCHEMY_TRACK_MODIFICATIONS")  # Ovo se često postavlja na False da bi se izbegli upozorenja
    app.config['JWT_SECRET_KEY'] = os.getenv("JWT_SECRET_KEY")
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1000 * 1000
    db.init_app(app)

    api = Api(app)

    app_bcrypt.init_app(app)
    migrate = Migrate(app, db)
    jwt_manager = JWTManager(app)
    with app.app_context():
        import database_layer

        db.create_all()

    api.register_blueprint(auth_blueprint)
    api.register_blueprint(admin_blueprint)
    api.register_blueprint(user_blueprint)
    api.register_blueprint(seller_blueprint)
    CORS(app)
    return app

