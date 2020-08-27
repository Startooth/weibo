"""empty message

Revision ID: 491a77bf0af0
Revises: 10d24914d06b
Create Date: 2020-08-27 10:05:41.926868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '491a77bf0af0'
down_revision = '10d24914d06b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('uid', sa.Integer(), nullable=False),
    sa.Column('wid', sa.Integer(), nullable=False),
    sa.Column('cid', sa.Integer(), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_comment_cid'), 'comment', ['cid'], unique=False)
    op.create_index(op.f('ix_comment_uid'), 'comment', ['uid'], unique=False)
    op.create_index(op.f('ix_comment_wid'), 'comment', ['wid'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_comment_wid'), table_name='comment')
    op.drop_index(op.f('ix_comment_uid'), table_name='comment')
    op.drop_index(op.f('ix_comment_cid'), table_name='comment')
    op.drop_table('comment')
    # ### end Alembic commands ###
