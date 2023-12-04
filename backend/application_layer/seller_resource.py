from flask.views import MethodView
from flask_smorest import Blueprint, abort
from application_layer.schemas.article_schema import ArticleSchema, ArticleUpdate
from application_layer.schemas.orders import OrderSchema
from db import db
from flask import jsonify
from database_layer import ArticleModel,OrderModel
from database_layer.order import OrderStatus
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token

seller_blueprint = Blueprint("seller", __name__,
                             description="Seller CRUD operations ")


@seller_blueprint.route("/api/articles")
class SellerView(MethodView):

    @seller_blueprint.response(200, ArticleSchema(many=True))
    def get(self):
        return ArticleModel.query.all()

    @seller_blueprint.arguments(ArticleSchema)
    @seller_blueprint.response(201, ArticleSchema)
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

    @seller_blueprint.response(200, ArticleSchema)
    def get(self, article_id):
        article = ArticleModel.query.get_or_404(article_id)
        return article

    @seller_blueprint.arguments(ArticleUpdate)
    @seller_blueprint.response(201, ArticleSchema)
    def put(self, article_data, article_id):
        article: ArticleModel = ArticleModel.query.get_or_404(article_id)

        article.name = article_data.get('name', article.name)
        article.price = article_data.get('price', article.price)
        article.amount = article_data.get('amount', article.amount)
        article.description = article_data.get('description',
                                               article.description)

        db.session.commit()
        return article

    def delete(self, article_id):
        article: ArticleModel = ArticleModel.query.get_or_404(article_id)

        db.session.delete(article)
        db.session.commit()

        return "Entity deleted",204


@seller_blueprint.route('/api/orders')
class SellerOrders(MethodView):

    @seller_blueprint.response(200,OrderSchema(many=True))
    def get(self):
        orders = OrderModel.query.filter(OrderModel.order_status == OrderStatus.IN_TRANSPORT)

        return orders

@seller_blueprint.route('/api/users/orders')
class SellerOrders(MethodView):

    @seller_blueprint.response(200,OrderSchema(many=True))
    def get(self):
        #TODO izvuci iz tokena user_id i pronaci ga ovde
        orders = OrderModel.query.filter(OrderModel.order_status == OrderStatus.DELIVERED)

        return orders