"""empty message

Revision ID: ce209e6e732d
Revises: 94eb365b057b
Create Date: 2018-04-09 10:39:44.400646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ce209e6e732d'
down_revision = '94eb365b057b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('post_content_key', 'post', type_='unique')
    op.drop_constraint('post_title_key', 'post', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('post_title_key', 'post', ['title'])
    op.create_unique_constraint('post_content_key', 'post', ['content'])
    # ### end Alembic commands ###