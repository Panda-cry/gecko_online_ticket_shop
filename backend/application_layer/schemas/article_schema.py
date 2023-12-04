from marshmallow import Schema,fields, pre_load
from marshmallow.validate import OneOf,Range, Length
from database_layer.user import UserRoleEnum

class ArticleMixin(Schema):
    id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

class ArticleSchema(ArticleMixin):

    name = fields.Str(required=True, validate=Length(max=40))
    price = fields.Float(required=True,validate=Range(min=10))
    amount = fields.Float(required=True,validate=Range(min=1))
    description = fields.Str()
    # orders = fields.Nested()


class ArticleSchemaDTO(Schema):
    name = fields.Str(required=True, validate=Length(max=40))
    price = fields.Float(required=True, validate=Range(min=10))
class ArticleUpdate(Schema):
    price = fields.Float(validate=Range(min=10))
    amount = fields.Float(validate=Range(min=1))
    description = fields.Str()
