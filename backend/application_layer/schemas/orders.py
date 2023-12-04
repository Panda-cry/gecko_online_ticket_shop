from marshmallow import Schema,fields, pre_load
from marshmallow.validate import OneOf,Range, Length
from database_layer.user import UserRoleEnum
from application_layer.schemas.article_schema import ArticleSchemaDTO

class OrderSchema(Schema):
    amount = fields.Integer(required=True, validate=Range(1))
    comment = fields.Str(validate=Length(max=100))
    address = fields.Str(required=True, validate=Length(max=50))
    created_at = fields.DateTime(dump_only=True)
    article_id = fields.Integer(required=True)
    articles = fields.List(fields.Nested(ArticleSchemaDTO),dump_only=True)