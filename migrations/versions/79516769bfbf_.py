"""empty message

Revision ID: 79516769bfbf
Revises: 9488760fb5da
Create Date: 2020-08-24 19:40:45.162344

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79516769bfbf'
down_revision = '9488760fb5da'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blog', sa.Column('username', sa.String(length=20), nullable=False))
    op.add_column('users', sa.Column('des', sa.Text(), nullable=True))
    op.add_column('users', sa.Column('hobbit', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'hobbit')
    op.drop_column('users', 'des')
    op.drop_column('blog', 'username')
    # ### end Alembic commands ###