from db import db
from sqlalchemy import Integer,String,Enum,DateTime,Column
import enum
from datetime import datetime
from web_bcrypt import app_bcrypt



class UserRoleEnum(enum.Enum):
    USER = 'user'
    ADMIN = 'admin'
    SELLER = "seller"



class UserModel(db.Model):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True)
    email = Column(String(80), unique=True, nullable=False)
    username = Column(String(80), unique=True, nullable=False)
    password = Column(String(80), nullable=False)
    user_type = Column(Enum(UserRoleEnum),nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def __init__(self, email, username, password, user_type):
        self.email = email,
        self.username = username
        self.password = app_bcrypt.generate_password_hash(password, 10).decode()
        self.user_type = user_type
        self.created_at = datetime.now()
        self.updated_at = None
