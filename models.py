from base import db
from sqlalchemy import func, text
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime
from transitions import Machine
from statemachine import states, transitions


class ModelTimeMixin(object):
    @declared_attr
    def create_time(cls):
        return db.Column(db.DateTime, default=datetime.utcnow())

    @declared_attr
    def update_time(cls):
        return db.Column(
            db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())


class Post(db.Model, ModelTimeMixin):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(80),  nullable=False)
    # update_time = db.Column(db.TIMESTAMP(True), nullable=False)
    # create_time = db.Column(db.TIMESTAMP(True), nullable=False, server_default=text('NOW()'))
    comment = db.relationship('Comment', backref='post')
    view_count = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Post %r>' % self.title
    #
    # @property
    # def last_commented_time(self):
    #     return self.update_time


class Comment(Machine, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(80), nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow())
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)
    status = db.Column(db.String(80), nullable=False)

    def __init__(self, **kwargs):
        super(Comment, self).__init__(**kwargs)
        # 状态定义
        states = ['wait', 'pass', 'not pass']
        Machine.__init__(self, states=states, initial='wait')
        self.add_transition('review', 'wait', 'pass')
        self.status = 'wait'

        # Machine(self, states, transitions=transitions)

    def __repr__(self):
        return '<Comment %r>' % self.content

    def on_enter_pass(self):
        self.status = 'pass'
        db.session.commit()
        print('wait for u')

