import os
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from application_layer.schemas.user_schema import UserSchema, LoginSchema, \
    TokenSchemaDTO, UserSchemaDTO, ImageSchema
from db import db
from web_bcrypt import app_bcrypt
from database_layer import UserModel
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity, jwt_required
from celery_workers.celery_workind_man_kind import add
from flask_bcrypt import Bcrypt
auth_blueprint = Blueprint("auth", __name__,
                           description="Authentication operations ")

bcrypt = Bcrypt()

@auth_blueprint.route('/api/login')
class Login(MethodView):
    @auth_blueprint.arguments(LoginSchema)
    @auth_blueprint.response(200, TokenSchemaDTO)
    def post(self, login_data):
        print("a sada idemo dalje")
        user_email = UserModel.query.filter(
            UserModel.email == login_data.get('username_email')).first()
        user_username = UserModel.query.filter(
            UserModel.username == login_data.get('username_email')).first()

        user: UserModel = user_email or user_username
        if not user:
            abort(404, message="Invalid email or username")

        if not app_bcrypt.check_password_hash(user.password,
                                          login_data.get('password')):
            abort(404, message="Invalid password")

        if user.user_type.name == "USER":
            access_token = create_access_token(identity=user.id,
                                               fresh=True,
                                               expires_delta=timedelta(minutes=10),
                                               additional_claims={
                                                   "user_type": user.user_type.name})
            refresh_token = create_refresh_token(identity=user.id,
                                                 expires_delta=timedelta(days=1))
        else:
            access_token = create_access_token(identity=user.id,
                                               fresh=True,
                                               additional_claims={
                                                   "user_type": user.user_type.name})
            refresh_token = create_refresh_token(identity=user.id)

        return {"access_token": access_token,
                "refresh_token": refresh_token}


@auth_blueprint.route('/api/register')
class Register(MethodView):

    @auth_blueprint.arguments(schema=UserSchema)
    @auth_blueprint.response(status_code=201, schema=UserSchemaDTO)
    def post(self, user_data):
        if UserModel.query.filter(
                UserModel.email == user_data.get('email')).first():
            abort(404, message="We have this user already please login")
        user_data['password'] = app_bcrypt.generate_password_hash(
            user_data.get('password')).decode("utf-8")
        new_user = UserModel(**user_data)

        add.delay("tatarata", "sender_email", "message")
        db.session.add(new_user)
        db.session.commit()
        return new_user


@auth_blueprint.route('/api/image')
class UserImageUpload(MethodView):

    @auth_blueprint.arguments(ImageSchema, location="files")
    @auth_blueprint.response(201)
    def post(self, image):
        image = image.get('image')
        image.save(os.getenv("IMAGE_LOCATION") + f"/{image.filename}")
        return


@auth_blueprint.route('/api/refresh')
class RefreshToken(MethodView):

    @jwt_required(refresh=True)
    @auth_blueprint.response(200, TokenSchemaDTO)
    def get(self):
        user_id = get_jwt_identity()
        user = UserModel.query.get_or_404(user_id)

        if not user:
            abort(404, message="Invalid user id")

        access_token = create_access_token(identity=user.id,
                                           expires_delta=timedelta(minutes=10),
                                           additional_claims={
                                               "user_type": user.user_type.name})
        refresh_token = create_refresh_token(identity=user.id,
                                             expires_delta=timedelta(days=1))

        return {"access_token": access_token,
                "refresh_token": refresh_token}
