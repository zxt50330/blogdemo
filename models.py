from base import db
from sqlalchemy import func, text
from sqlalchemy.ext.declarative import declared_attr
from datetime import datetime


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

    def __repr__(self):
        return '<Post %r>' % self.title
    #
    # @property
    # def last_commented_time(self):
    #     return self.update_time


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(80), nullable=False)
    content = db.Column(db.String(80), nullable=False)
    created = db.Column(db.TIMESTAMP(True), nullable=False, server_default=text('NOW()'))
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'), nullable=False)

    def __repr__(self):
        return '<Comment %r>' % self.content

# admin = User(username='admin', email='admin@example.com')
# guest = User(username='guest', email='guest@example.com')
# db.session.add(admin)
# db.session.add(guest)
# db.session.commit()

# def get_addresses_from_user(user_name):
#     user = db.session.query(User).filter_by(username=user_name).first()
#     # address = Address(email_address='4sadas4', user_id=user.id)
#     # db.session.add(address)
#     # db.session.commit()
#     print(user.address)
#
#     a = db.session.query(Address).filter(Address.email_address.like('%4%')).all()
#     print([(i.user,i) for i in a])

# if __name__ == '__main__':
#     get_addresses_from_user('guest')