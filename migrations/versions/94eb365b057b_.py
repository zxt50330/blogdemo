"""empty message

Revision ID: 94eb365b057b
Revises: 59dd15c27d67
Create Date: 2018-04-09 10:01:39.504337

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '94eb365b057b'
down_revision = '59dd15c27d67'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('create_time', sa.DateTime(), nullable=True))
    op.add_column('post', sa.Column('update_time', sa.DateTime(), nullable=True))
    op.drop_column('post', 'created_at')
    op.drop_column('post', 'updated_at')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.add_column('post', sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
    op.drop_column('post', 'update_time')
    op.drop_column('post', 'create_time')
    # ### end Alembic commands ###
