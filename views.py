from flask import Blueprint
from flask import request, jsonify
from models import Post, Comment
from schema import PostSchema, CommentSchema

blueprint = Blueprint('post', __name__)


@blueprint.route('/api/posts/', methods=['GET', 'POST'])
def get_posts():
    post_schema = PostSchema()
    if request.method == 'POST':
        try:
            data = request.get_json()
            if not data['title'] or not data['content']:
                return jsonify({'code': 400})

            return jsonify({'code': 201, 'data': data})
        except Exception as e:
            return jsonify({'code': 400, 'data': e})
    else:
        posts = Post.query.all()
        data = post_schema.dump(posts, many=True).data
        return jsonify({'data': data})


@blueprint.route('/api/posts/<int:pk>', methods=['GET'])
def get_post(pk):
    post = Post.query.filter_by(id=pk).one()
    post_schema = PostSchema()
    data = post_schema.dump(post).data
    return jsonify({'data': data})