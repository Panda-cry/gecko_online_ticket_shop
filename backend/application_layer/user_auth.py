from flask.views import MethodView
from flask_smorest import Blueprint, abort
from application_layer.schemas.user_schema import UserSchema, LoginSchema, \
    TokenSchema
from db import db
from web_bcrypt import app_bcrypt
from database_layer import UserModel
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token

auth_blueprint = Blueprint("auth", __name__,
                           description="Authentication operations ")


@auth_blueprint.route('/login')
class Login(MethodView):
    @auth_blueprint.arguments(LoginSchema)
    @auth_blueprint.response(200, TokenSchema)
    def post(self, login_data):
        user_email = UserModel.query.filter(
            UserModel.email == login_data.get('username_email')).first()
        user_username = UserModel.query.filter(
            UserModel.username == login_data.get('username_email')).first()

        user: UserModel = user_email or user_username
        if not user:
            abort(404, message="Invalid email or username")

        if app_bcrypt.check_password_hash(user.password,
                                          login_data.get('password')):
            abort(404, message="Invalid password")

        access_token = create_access_token(identity=user.id,
                                           fresh=True,
                                           expires_delta=timedelta(seconds=10),
                                           additional_claims={
                                               "user_type": user.user_type.name})
        refresh_token = create_refresh_token(identity=user.id,
                                             expires_delta=timedelta(days=1))

        return TokenSchema().dump({"access_token": access_token,
                                   "refresh_token": refresh_token})


@auth_blueprint.route('/register')
class Register(MethodView):

    @auth_blueprint.arguments(UserSchema)
    @auth_blueprint.response(201, UserSchema)
    def post(self, user_data):
        if UserModel.query.filter(
                UserModel.email == user_data.get('email')).first():
            abort(404, message="We have this user already please login")
        user_data['password'] = app_bcrypt.generate_password_hash(
            user_data.get('password'))
        new_user = UserModel(**user_data)

        db.session.add(new_user)
        db.session.commit()

        return new_user
