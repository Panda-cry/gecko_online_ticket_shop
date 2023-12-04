from flask.views import MethodView
from flask_smorest import Blueprint, abort
from application_layer.schemas.user_schema import UserSchema, LoginSchema, \
    TokenSchema
from application_layer.schemas.orders import OrderSchema
from database_layer import OrderModel, UserModel
from db import db
from web_bcrypt import app_bcrypt
from database_layer import UserModel
from datetime import timedelta
from sqlalchemy.exc import SQLAlchemyError
from flask_jwt_extended import create_access_token, create_refresh_token, \
    jwt_required

admin_blueprint = Blueprint("Admin", __name__,
                            description="Admin operations ")


@admin_blueprint.route('/api/users/orders')
class AdminResource(MethodView):

    @admin_blueprint.response(200,OrderSchema(many=True))
    def get(self):
        orders = OrderModel.query.all()
        return orders

@admin_blueprint.route('/api/users/<int:user_id>/verify')
class AdminVerify(MethodView):

    def get(self,user_id):
        user: UserModel = UserModel.query.get_or_404(user_id)
        user.is_verified = True
        db.session.commit()
        return {"message":"Verfied"},200