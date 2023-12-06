from marshmallow import Schema, fields, post_load, pre_load
from marshmallow.validate import OneOf, Length, Email
from database_layer.user import UserRoleEnum
from application_layer.schemas.orders_schema import OrderInUserSchema
from flask_smorest.fields import Upload


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


class UserPutSchema(Schema):
    username = fields.Str(required=True, validate=Length(min=5))
    email = fields.Str(required=True, validate=Email())
    password = fields.Str(required=True, validate=Length(min=5))
    image = fields.Raw()

    @post_load
    def _convert_image(self, in_data, **kwargs):
        if in_data.get('image'):
            in_data['image'] = bytes(in_data.get('image'),"utf-8")
        return in_data