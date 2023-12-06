import datetime

from db import db
from sqlalchemy import Integer, String, Column, Float,DateTime,LargeBinary
from sqlalchemy.orm import Relationship

class ArticleModel(db.Model):
    __tablename__ = "articles"

    id = Column(Integer, autoincrement=True, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    price = Column(Float, nullable=False)
    amount = Column(Integer, nullable=False)
    description = Column(String)
    created_at = Column(DateTime,default=datetime.datetime.now)
    updated_at = Column(DateTime, onupdate=datetime.datetime.now)
    orders = Relationship("OrderModel",secondary="orders_articles",back_populates="articles")
    image = Column(String, nullable=True)
