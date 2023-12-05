from marshmallow import Schema, fields
from marshmallow.validate import  Range, Length
from application_layer.schemas.article_schema import ArticleInOrderSchema


class OrderSchema(Schema):
    amount = fields.Integer(required=True, validate=Range(1))
    comment = fields.Str(validate=Length(max=100))
    address = fields.Str(required=True, validate=Length(max=50))
    created_at = fields.DateTime(dump_only=True)
    article_id = fields.Integer(required=True)
    articles = fields.List(fields.Nested(ArticleInOrderSchema), dump_only=True)


class OrderInUserSchema(Schema):
    comment = fields.Str()
    address = fields.Str()
    articles = fields.List(fields.Nested(ArticleInOrderSchema))


class OrdersSchemaDTO(Schema):
    amount = fields.Integer()
    comment = fields.Str()
    address = fields.Str()
    created_at = fields.DateTime()
    articles = fields.List(fields.Nested(ArticleInOrderSchema))