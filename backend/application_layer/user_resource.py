from flask.views import MethodView
from flask_smorest import Blueprint, abort
from application_layer.schemas.user_schema import UserPatchSchema, \
    UserPutSchema, UserSchemaDTO
from application_layer.schemas.orders_schema import OrderSchema
from database_layer.order import OrderStatus
from db import db
from web_bcrypt import app_bcrypt
from database_layer import UserModel, ArticleModel, OrderModel
from flask_jwt_extended import get_jwt_identity
from application_layer.token_utils import check_role
user_blueprint = Blueprint("user", __name__,
                           description="User operations ")


@user_blueprint.route("/api/users")
class UserView(MethodView):

    @check_role(["USER"])
    @user_blueprint.response(200, UserSchemaDTO)
    def get(self):
        user_id = get_jwt_identity()
        user = UserModel.query.get_or_404(user_id)
        return user

    @check_role(["USER"])
    @user_blueprint.arguments(UserPutSchema)
    @user_blueprint.response(201, UserSchemaDTO)
    def put(self, update_user):
        user_id = get_jwt_identity()
        user: UserModel = UserModel.query.get_or_404(user_id)

        user.email = update_user.get('email')

        user.password = app_bcrypt.generate_password_hash(
            update_user.get('password')).decode("utf-8")
        user.username = update_user.get('username')

        db.session.commit()

        return user

    @check_role(["USER"])
    @user_blueprint.arguments(UserPatchSchema)
    @user_blueprint.response(201, UserSchemaDTO)
    def patch(self, update_user):
        user_id = get_jwt_identity()
        user: UserModel = UserModel.query.get_or_404(user_id)

        user.email = update_user.get('email', user.email)
        if update_user.get('password'):
            user.password = app_bcrypt.generate_password_hash(
                update_user.get('password')).decode("utf-8")
        user.username = update_user.get('username', user.username)

        db.session.commit()

        return user


@user_blueprint.route('/api/users/orders')
class UserOrderView(MethodView):

    @check_role(["USER"])
    @user_blueprint.response(200,OrderSchema(many=True))
    def get(self):
        user_id = get_jwt_identity()
        user: UserModel = UserModel.query.get_or_404(user_id)

        orders = OrderModel.query.filter(OrderModel.user_id == user.id
                                        ,OrderModel.order_status == OrderStatus.DELIVERED)

        return orders

    @check_role(["USER", "SELLER"])
    @user_blueprint.arguments(OrderSchema)
    @user_blueprint.response(201, OrderSchema)
    def post(self, order_data):
        user_id = get_jwt_identity()
        user = UserModel.query.get_or_404(user_id)
        article: ArticleModel = ArticleModel.query.get_or_404(
            order_data.get('article_id'))

        if article.amount - int(order_data.get('amount')) <= 0:
            abort(404,message="We don't have that much resources")

        order_data.pop('article_id')
        order: OrderModel = OrderModel(**order_data)

        order.user = user
        order.articles.append(article)
        article.amount -= order_data.get('amount')
        db.session.add(order)
        db.session.commit()
        return order


@user_blueprint.route('/api/users/orders/price_sum')
class UserPriceView(MethodView):

    @check_role(["USER"])
    def get(self):
        user_id = get_jwt_identity()
        user: UserModel = UserModel.query.get_or_404(user_id)
        _sum = 0
        for order in user.orders:
            _sum += order.amount * order.articles[0].price

        #Delivery fee
        _sum += 200
        return {"Sum is :": _sum}, 200
