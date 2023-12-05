from marshmallow import Schema,fields, post_load
from marshmallow.validate import Range, Length


class ArticleMixin(Schema):
    id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class ArticleSchema(ArticleMixin):
    name = fields.Str(required=True, validate=Length(max=40))
    price = fields.Float(required=True,validate=Range(min=10))
    amount = fields.Float(required=True,validate=Range(min=1))
    description = fields.Str()
    image = fields.Raw(type="image")

    @post_load
    def _convert_image(self, in_data, **kwargs):
        if in_data.get('image'):
            in_data['image'] = bytes(in_data.get('image'),"utf-8")
        return in_data


class ArticleInOrderSchema(Schema):
    name = fields.Str()
    amount = fields.Float()
    price = fields.Float()


class ArticleSchemaDTO(ArticleMixin):
    name = fields.Str()
    price = fields.Float()
    amount = fields.Float()
    description = fields.Str()
    image = fields.Str()


class ArticleUpdate(Schema):
    price = fields.Float(validate=Range(min=10))
    amount = fields.Float(validate=Range(min=1))
    description = fields.Str()
    image = fields.Raw(type="image")

    @post_load
    def _convert_image(self, in_data, **kwargs):
        if in_data.get('image'):
            in_data['image'] = bytes(in_data.get('image'),"utf-8")
        return in_data