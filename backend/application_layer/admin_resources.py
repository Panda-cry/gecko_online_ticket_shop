from flask.views import MethodView
from flask_smorest import Blueprint, abort
from application_layer.schemas.user_schema import UserSchema, LoginSchema, \
    TokenSchema
from db import db
from web_bcrypt import app_bcrypt
from database_layer import UserModel
from datetime import timedelta
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import create_access_token, create_refresh_token, \
    jwt_required

admin_blueprint = Blueprint("Admin", __name__,
                            description="Admin operations ")


@admin_blueprint.route('/admin')
class AdminResource(MethodView):

    @jwt_required()
    def get(self):
        print("lets goo")
        pass
