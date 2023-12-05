from flask.views import MethodView
from flask_smorest import Blueprint, abort
from application_layer.schemas.article_schema import ArticleSchema, \
    ArticleUpdate, ArticleSchemaDTO
from application_layer.schemas.orders_schema import OrdersSchemaDTO
from db import db
from database_layer import ArticleModel, OrderModel
from database_layer.order import OrderStatus
from flask_jwt_extended import jwt_required, get_jwt_identity
from application_layer.token_utils import check_role

seller_blueprint = Blueprint("seller", __name__,
                             description="Seller CRUD operations ")


@seller_blueprint.route("/api/articles")
class SellerView(MethodView):
    @check_role(["SELLER","USER"])
    @seller_blueprint.response(200, ArticleSchemaDTO(many=True))
    def get(self):
        return ArticleModel.query.all()

    @check_role(["SELLER"])
    @seller_blueprint.arguments(ArticleSchema)
    @seller_blueprint.response(201, ArticleSchemaDTO)
    def post(self, article_data):
        if ArticleModel.query.filter(
                ArticleModel.name == article_data.get('name')).first():
            abort(404, message="We have this article already")

        article = ArticleModel(**article_data)
        db.session.add(article)
        db.session.commit()
        return article


@seller_blueprint.route("/api/articles/<int:article_id>")
class SellerView(MethodView):

    @check_role(["SELLER", "USER"])
    @seller_blueprint.response(200, ArticleSchemaDTO)
    def get(self, article_id):
        article = ArticleModel.query.get_or_404(article_id)
        return article

    @check_role(["SELLER"])
    @seller_blueprint.arguments(ArticleUpdate)
    @seller_blueprint.response(201, ArticleSchemaDTO)
    def put(self, article_data, article_id):
        article: ArticleModel = ArticleModel.query.get_or_404(article_id)

        article.name = article_data.get('name', article.name)
        article.price = article_data.get('price', article.price)
        article.amount = article_data.get('amount', article.amount)
        article.description = article_data.get('description',
                                               article.description)
        article.image = article_data.get('image',
                                               article.image)
        db.session.commit()
        return article

    @check_role(["SELLER"])
    @jwt_required(fresh=True)
    def delete(self, article_id):
        article: ArticleModel = ArticleModel.query.get_or_404(article_id)

        db.session.delete(article)
        db.session.commit()

        return "Entity deleted", 204


@seller_blueprint.route('/api/orders')
class SellerOrders(MethodView):

    @check_role(["SELLER"])
    @seller_blueprint.response(200, OrdersSchemaDTO(many=True))
    def get(self):
        user_id = get_jwt_identity()
        orders = OrderModel.query.filter(OrderModel.user_id == user_id,
                                         OrderModel.order_status == OrderStatus.IN_TRANSPORT)

        return orders


@seller_blueprint.route('/api/seller/orders')
class SellerOrders(MethodView):

    @check_role(["SELLER"])
    @seller_blueprint.response(200, OrdersSchemaDTO(many=True))
    def get(self):
        user_id = get_jwt_identity()
        orders = OrderModel.query.filter(OrderModel.user_id == user_id,
                                         OrderModel.order_status == OrderStatus.DELIVERED)
        return orders
