from base import ma
from models import Post, Comment


class PostSchema(ma.ModelSchema):
    class Meta:
        model = Post


class CommentSchema(ma.ModelSchema):
    class Meta:
        model = Comment
