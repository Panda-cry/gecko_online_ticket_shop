import os
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from application_layer.schemas.user_schema import UserSchema, LoginSchema, \
    TokenSchemaDTO, UserSchemaDTO, ImageSchema, LoginViaThirdApi, OTPCodeSchema
from db import db
from web_bcrypt import app_bcrypt
from database_layer import UserModel
from datetime import timedelta
from flask_jwt_extended import create_access_token, create_refresh_token, \
    get_jwt_identity, jwt_required
from celery_workers.celery_workind_man_kind import add
from flask_bcrypt import Bcrypt
import pyotp

auth_blueprint = Blueprint("auth", __name__,
                           description="Authentication operations ",
                           url_prefix="/api")

bcrypt = Bcrypt()


@auth_blueprint.route('/login')
class Login(MethodView):

    @auth_blueprint.arguments(LoginSchema)
    @auth_blueprint.response(200)
    def post(self, login_data):
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

        otp_url = pyotp.TOTP(user.otp_base34_password).provisioning_uri(
            name=user.username,
            issuer_name="Lunch store app")

        access_token = create_access_token(identity=user.id,
                                           fresh=True,
                                           expires_delta=timedelta(
                                               hours=5),
                                           additional_claims={
                                               "user_type": user.user_type.name})
        refresh_token = create_refresh_token(identity=user.id,
                                             expires_delta=timedelta(
                                                 days=1))

        return {"qr_url": otp_url, "access_token": access_token,
                "refresh_token": refresh_token}


@auth_blueprint.route('/login/code')
class LoginWithCode(MethodView):
    @jwt_required()
    @auth_blueprint.arguments(OTPCodeSchema)
    @auth_blueprint.response(200, TokenSchemaDTO)
    def post(self, code):
        user_id = get_jwt_identity()
        user = UserModel.query.get_or_404(user_id)
        totp = pyotp.TOTP(user.otp_base34_password)
        if not totp.verify(code.get("code")):
            abort(404, message="Wrong code !!!")
        if user.user_type.name == "USER":
            access_token = create_access_token(identity=user.id,
                                               fresh=True,
                                               expires_delta=timedelta(
                                                   hours=5),
                                               additional_claims={
                                                   "user_type": user.user_type.name})
            refresh_token = create_refresh_token(identity=user.id,
                                                 expires_delta=timedelta(
                                                     days=1))
        else:
            access_token = create_access_token(identity=user.id,
                                               fresh=True,
                                               additional_claims={
                                                   "user_type": user.user_type.name})
            refresh_token = create_refresh_token(identity=user.id)

        return {"access_token": access_token,
                "refresh_token": refresh_token}


@auth_blueprint.route('/register')
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

        new_user.otp_base34_password = pyotp.random_base32(32)
        add.delay("tatarata", "sender_email", "message")

        db.session.add(new_user)
        db.session.commit()
        return new_user


@auth_blueprint.route('/image')
class UserImageUpload(MethodView):

    @auth_blueprint.arguments(ImageSchema, location="files")
    @auth_blueprint.response(201)
    def post(self, image):
        image = image.get('image')
        image.save(os.getenv("IMAGE_LOCATION") + f"/{image.filename}")
        return


@auth_blueprint.route('/login/third_api')
class UserThirdApiLogin(MethodView):

    @auth_blueprint.arguments(LoginViaThirdApi)
    @auth_blueprint.response(201, TokenSchemaDTO)
    def post(self, api_data):
        user = UserModel.query.filter(
            UserModel.email == api_data.get('email')).first()
        if not user:
            abort(404, message="User not found")

        access_token = create_access_token(identity=user.id,
                                           fresh=True,
                                           expires_delta=timedelta(hours=5),
                                           additional_claims={
                                               "user_type": user.user_type
                                           })
        refresh_token = create_refresh_token(identity=user.id,
                                             expires_delta=timedelta(days=30))

        return {"access_token": access_token, "refresh_token": refresh_token}


@auth_blueprint.route('/refresh')
class RefreshToken(MethodView):

    @jwt_required(refresh=True)
    @auth_blueprint.response(200, TokenSchemaDTO)
    def get(self):
        user_id = get_jwt_identity()
        user = UserModel.query.get_or_404(user_id)

        if not user:
            abort(404, message="Invalid user id")

        access_token = create_access_token(identity=user.id,
                                           expires_delta=timedelta(hours=10),
                                           additional_claims={
                                               "user_type": user.user_type.name})
        refresh_token = create_refresh_token(identity=user.id,
                                             expires_delta=timedelta(days=1))

        return {"access_token": access_token,
                "refresh_token": refresh_token}
