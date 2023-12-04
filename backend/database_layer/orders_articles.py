from db import db
from  sqlalchemy import Integer,ForeignKey,Column


class OrderArticleModel(db.Model):
    __tablename__ = "orders_articles"
    id = Column(Integer, autoincrement=True, primary_key=True)
    order_id = Column(Integer,ForeignKey("orders.id"),nullable=False)
    article_id = Column(Integer,ForeignKey("articles.id"),nullable=False)
