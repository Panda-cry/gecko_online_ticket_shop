from flask.views import MethodView
from flask_smorest import Blueprint, abort
from application_layer.schemas.user_schema import UserSchema, UserPatchSchema, \
    UserPutSchema
from application_layer.schemas.orders import OrderSchema
from database_layer.order import OrderStatus
from db import db
from web_bcrypt import app_bcrypt
from database_layer import UserModel, ArticleModel, OrderModel
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token

user_blueprint = Blueprint("user", __name__,
                           description="User operations ")


@user_blueprint.route("/api/users/<int:user_id>")
class UserView(MethodView):

    @user_blueprint.response(200, UserSchema)
    def get(self, user_id):
        user = UserModel.query.get_or_404(user_id)
        return user

    @user_blueprint.arguments(UserPutSchema)
    @user_blueprint.response(201, UserSchema)
    def put(self, update_user, user_id):
        user: UserModel = UserModel.query.get_or_404(user_id)

        user.email = update_user.get('email')

        user.password = app_bcrypt.generate_password_hash(
            update_user.get('password')).decode()
        user.username = update_user.get('username')

        db.session.commit()

        return user

    @user_blueprint.arguments(UserPatchSchema)
    @user_blueprint.response(201, UserSchema)
    def patch(self, update_user, user_id):
        user: UserModel = UserModel.query.get_or_404(user_id)

        user.email = update_user.get('email', user.email)
        if update_user.get('password'):
            user.password = app_bcrypt.generate_password_hash(
                update_user.get('password')).decode()
        user.username = update_user.get('username', user.username)

        db.session.commit()

        return user


@user_blueprint.route('/api/users/<int:user_id>/orders')
class UserOrderView(MethodView):

    @user_blueprint.response(200,OrderSchema(many=True))
    def get(self, user_id):
        user: UserModel = UserModel.query.get_or_404(user_id)

        orders = OrderModel.query.filter(OrderModel.user_id == user.id
                                        ,OrderModel.order_status == OrderStatus.DELIVERED)

        return orders

    @user_blueprint.arguments(OrderSchema)
    @user_blueprint.response(201, OrderSchema)
    def post(self, order_data, user_id):
        user = UserModel.query.get_or_404(user_id)
        article: ArticleModel = ArticleModel.query.get_or_404(
            order_data.get('article_id'))

        order_data.pop('article_id')
        order: OrderModel = OrderModel(**order_data)

        order.user = user
        order.articles.append(article)
        article.amount -= order_data.get('amount')
        db.session.add(order)
        db.session.commit()
        return order


@user_blueprint.route('/api/users/<int:user_id>/orders/price_sum')
class UserPriceView(MethodView):

    def get(self, user_id):
        user: UserModel = UserModel.query.get_or_404(user_id)
        _sum = 0
        for order in user.orders:
            _sum += order.amount * order.articles[0].price

        #Delivery fee
        _sum += 200
        return {"Sum is :": _sum}, 200
