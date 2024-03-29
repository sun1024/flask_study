"""empty message

Revision ID: 48340b44dae0
Revises: 3781fdb2bc08
Create Date: 2019-06-24 16:31:59.690852

"""

# revision identifiers, used by Alembic.
revision = '48340b44dae0'
down_revision = '3781fdb2bc08'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'confirmed')
    # ### end Alembic commands ###
