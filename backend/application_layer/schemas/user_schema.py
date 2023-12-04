from marshmallow import Schema, fields, pre_load
from marshmallow.validate import OneOf, Length, Email
from database_layer.user import UserRoleEnum
from application_layer.schemas.orders import OrderSchema

class UserShemaMixin(Schema):
    id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class UserSchema(UserShemaMixin):
    username = fields.Str(required=True, validate=Length(min=5))
    email = fields.Str(required=True, validate=Email())
    password = fields.Str(required=True, validate=Length(min=5))
    user_type = fields.Enum(UserRoleEnum, validate=OneOf(choices=UserRoleEnum))
    orders = fields.List(fields.Nested(OrderSchema))

class LoginSchema(Schema):
    username_email = fields.Str(required=True)
    password = fields.Str(required=True)


class TokenSchema(Schema):
    access_token = fields.Str()
    refresh_token = fields.Str()


class AdminSchema(UserSchema):
    is_verified = fields.Boolean()


class UserPatchSchema(Schema):
    username = fields.Str(validate=Length(min=5))
    email = fields.Str(validate=Email())
    password = fields.Str(validate=Length(min=5))


class UserPutSchema(Schema):
    username = fields.Str(required=True,validate=Length(min=5))
    email = fields.Str(required=True,validate=Email())
    password = fields.Str(required=True,validate=Length(min=5))

