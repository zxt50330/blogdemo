from flask import Blueprint
from flask import request, jsonify
from models import Post, Comment
from schema import PostSchema, CommentSchema
from base import db

blueprint = Blueprint('post', __name__)

post_schema = PostSchema()

@blueprint.route('/api/posts/', methods=['GET', 'POST'])
def get_posts():
    if request.method == 'POST':
        try:
            data = request.get_json()
            # if not data['title'] or not data['content']:
            #     return jsonify({'code': 400})
            post_data = post_schema.load(data).data
            db.session.add(post_data)
            db.session.commit()
            dump_data = post_schema.dump(post_data).data
            return jsonify({'code': 201, 'data': dump_data})
        except Exception as e:
            return jsonify({'code': 500, 'data': e})
    else:
        posts = Post.query.all()
        total = len(posts)
        data = post_schema.dump(posts, many=True).data
        return jsonify({'data': data, 'total': total})


@blueprint.route('/api/posts/<int:pk>', methods=['GET'])
def get_post(pk):
    post = Post.query.filter_by(id=pk).one()
    data = post_schema.dump(post).data
    return jsonify({'data': data})


@blueprint.route('/api/posts/<int:pk>', methods=['PUT'])
def put_post(pk):
    data = request.get_json()
    post = Post.query.filter_by(id=pk).first()
    if post:
        post.content = data.get('content', '')
        post.title = data.get('title', '')
        db.session.commit()
    else:
        post = Post(id=pk, **data)
        db.session.add(post)
        db.session.commit()
    dump_data = post_schema.dump(post).data
    return jsonify({'data': dump_data})


@blueprint.route('/api/posts/<int:pk>', methods=['PATCH'])
def patch_post(pk):
    data = request.get_json()
    post = Post.query.filter_by(id=pk).first()
    if post:
        post.content = data.get('content', '')
        post.title = data.get('title', '')
        db.session.commit()
    else:
        return jsonify({'code': 404})
    dump_data = post_schema.dump(post).data

    return jsonify({'data': dump_data})


@blueprint.route('/api/posts/<int:pk>', methods=['DELETE'])
def delete_post(pk):
    post = Post.query.filter_by(id=pk).one()
    db.session.delete(post)
    db.session.commit()
    return jsonify({'data': ''})