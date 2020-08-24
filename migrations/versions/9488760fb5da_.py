"""empty message

Revision ID: 9488760fb5da
Revises: 1a57855e4876
Create Date: 2020-08-24 17:56:13.870920

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9488760fb5da'
down_revision = '1a57855e4876'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('blog',
    sa.Column('wid', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=20), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('thumb', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('wid')
    )
    op.create_table('blog_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=True),
    sa.Column('wid', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('blog_user')
    op.drop_table('blog')
    # ### end Alembic commands ###
