import datetime

from db import db
from sqlalchemy import Integer,String,DateTime,Column,ForeignKey, Enum
from sqlalchemy.orm import Relationship
import enum


class OrderStatus(enum.Enum):
    CREATED = "Created"
    IN_TRANSPORT = "In transport"
    DELIVERED = "Delivered"


class OrderModel(db.Model):
    __tablename__ = "orders"
    id = Column(Integer,autoincrement=True,primary_key=True)

    amount = Column(Integer,nullable=False)
    comment = Column(String(100))
    address = Column(String(100), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    user_id = Column(Integer,ForeignKey("users.id"),nullable=False)
    user = Relationship("UserModel",back_populates="orders")
    order_status = Column(Enum(OrderStatus), default=OrderStatus.CREATED)
    delivery_time = Column(DateTime)
    articles = Relationship("ArticleModel",secondary="orders_articles",back_populates="orders")

