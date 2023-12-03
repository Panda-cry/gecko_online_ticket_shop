from marshmallow import Schema,fields, pre_load
from marshmallow.validate import OneOf
from database_layer.user import UserRoleEnum

class UserShemaMixin(Schema):
    id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class UserSchema(UserShemaMixin):
    username = fields.Str(required=True)
    email = fields.Str(required=True)
    password = fields.Str(required=True)
    user_type = fields.Enum(UserRoleEnum,validate=OneOf(choices=UserRoleEnum))


class LoginSchema(Schema):
    username_email = fields.Str(required=True)
    password = fields.Str(required=True)


class TokenSchema(Schema):
    access_token = fields.Str()
    refresh_token = fields.Str()


