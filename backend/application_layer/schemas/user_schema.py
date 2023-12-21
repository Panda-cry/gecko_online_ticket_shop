from marshmallow import Schema, fields, post_load, pre_load, post_dump
from marshmallow.validate import OneOf, Length, Email
from database_layer.user import UserRoleEnum
from application_layer.schemas.orders_schema import OrderInUserSchema
from flask_smorest.fields import Upload
from os import getenv
import os
import base64


class UserSchemaMixin(Schema):
    id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class UserSchema(UserSchemaMixin):
    username = fields.Str(required=True, validate=Length(min=5))
    email = fields.Str(required=True, validate=Email())
    password = fields.Str(required=True, validate=Length(min=5))
    user_type = fields.Enum(UserRoleEnum, validate=OneOf(choices=UserRoleEnum))
    image = fields.Str()


class ImageSchema(Schema):
    image = Upload()


class UserSchemaDTO(UserSchemaMixin):
    username = fields.Str()
    email = fields.Str()
    password = fields.Str()
    user_type = fields.Enum(UserRoleEnum)
    is_verified = fields.Boolean()
    orders = fields.List(fields.Nested(OrderInUserSchema))
    image = fields.Str()

    @post_dump
    def _convert_image_to_base64(self, in_data, **kwargs):
        image_url = f"{getenv('IMAGE_LOCATION')}/{in_data.get('image')}"
        if os.path.isfile(image_url):
            with open(image_url, "rb") as image:
                encoded_image = base64.b64encode(image.read()).decode("utf-8")
                in_data['image'] = encoded_image

        return in_data


class LoginSchema(Schema):
    username_email = fields.Str(required=True)
    password = fields.Str(required=True)


class TokenSchemaDTO(Schema):
    access_token = fields.Str()
    refresh_token = fields.Str()


class UserPatchSchema(Schema):
    username = fields.Str(validate=Length(min=5))
    email = fields.Str(validate=Email())
    password = fields.Str(validate=Length(min=5))
    image = fields.Str()


class UserPutSchema(Schema):
    username = fields.Str(required=True, validate=Length(min=5))
    email = fields.Str(required=True, validate=Email())
    password = fields.Str(required=True, validate=Length(min=5))
    image = fields.Str(required=True)


class LoginViaThirdApi(Schema):
    email = fields.Str(required=True, validate=Email())


class OTPCodeSchema(Schema):
    code = fields.Integer(required=True)
