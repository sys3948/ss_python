"""empty message

Revision ID: e7e76c410487
Revises: ae1e1c2d3b3c
Create Date: 2020-11-19 11:45:14.369727

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e7e76c410487'
down_revision = 'ae1e1c2d3b3c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('test',
    sa.Column('test_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('test_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('test')
    # ### end Alembic commands ###
