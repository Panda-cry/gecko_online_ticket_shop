import base64
import os.path

from marshmallow import Schema,fields, post_load, post_dump
from marshmallow.validate import Range, Length
from os import getenv


class ArticleMixin(Schema):
    id = fields.Integer(dump_only=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class ArticleSchema(ArticleMixin):
    name = fields.Str(required=True, validate=Length(max=40))
    price = fields.Float(required=True,validate=Range(min=10))
    amount = fields.Float(required=True,validate=Range(min=1))
    description = fields.Str()
    image = fields.Str()


class ArticleInOrderSchema(Schema):
    name = fields.Str()
    amount = fields.Float()
    price = fields.Float()
    image = fields.Str()


class ArticleSchemaDTO(ArticleMixin):
    name = fields.Str()
    price = fields.Float()
    amount = fields.Float()
    description = fields.Str()
    image = fields.Str()

    @post_dump
    def _convert_image_to_base64(self, in_data, **kwargs):
        image_url = f"{getenv('IMAGE_LOCATION')}/{in_data.get('image')}"
        if os.path.isfile(image_url):
            with open(image_url, "rb") as image:
                encoded_image = base64.b64encode(image.read()).decode("utf-8")
                in_data['image'] = encoded_image

        return in_data


class ArticleUpdate(Schema):
    price = fields.Float(validate=Range(min=10))
    amount = fields.Float(validate=Range(min=1))
    description = fields.Str()
    image = fields.Str()

    @post_load
    def _convert_image(self, in_data, **kwargs):
        if in_data.get('image'):
            in_data['image'] = bytes(in_data.get('image'),"utf-8")
        return in_data