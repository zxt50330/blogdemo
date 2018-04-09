from base import ma
from models import Post, Comment
from marshmallow import post_load


class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post


class CommentSchema(ma.ModelSchema):
    class Meta:
        model = Comment
