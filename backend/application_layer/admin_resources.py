from flask.views import MethodView
from flask_smorest import Blueprint
from application_layer.schemas.orders_schema import OrderSchema
from application_layer.schemas.user_schema import UserSchemaDTO
from database_layer import OrderModel, UserModel
from db import db
from application_layer.token_utils import check_role
from flask_jwt_extended import jwt_required
admin_blueprint = Blueprint("Admin", __name__,
                            description="Admin operations ")


@admin_blueprint.route('/api/admin/orders')
class AdminResource(MethodView):

    @check_role(["ADMIN"])
    @admin_blueprint.response(200, OrderSchema(many=True))
    def get(self):
        orders = OrderModel.query.all()
        return orders


@admin_blueprint.route('/api/admin/users')
class AdminUserResource(MethodView):

    @check_role(["ADMIN"])
    @admin_blueprint.response(200, UserSchemaDTO(many=True))
    def get(self):
        users = UserModel.query.filter(UserModel.user_type == "SELLER")
        return users


@admin_blueprint.route('/api/admin/users/all')
class AdminUserResource(MethodView):

    @check_role(["ADMIN"])
    @admin_blueprint.response(200, UserSchemaDTO(many=True))
    def get(self):
        users = UserModel.query.all()
        return users


@admin_blueprint.route('/api/users/<int:user_id>/verify')
class AdminVerify(MethodView):

    @check_role(["ADMIN"])
    def get(self, user_id):
        user: UserModel = UserModel.query.get_or_404(user_id)
        user.is_verified = True
        db.session.commit()
        return {"message": "Verified"}, 200

    @check_role(["ADMIN"])
    @jwt_required(fresh=True)
    def delete(self, user_id):
        user: UserModel = UserModel.query.get_or_404(user_id)
        db.session.delete(user)
        db.session.commit()
        return {"message": "Deleted"}, 200
