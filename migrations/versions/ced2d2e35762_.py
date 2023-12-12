"""empty message

Revision ID: ced2d2e35762
Revises: 48f7630a9da0
Create Date: 2021-03-20 18:26:30.521343

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ced2d2e35762'
down_revision = '48f7630a9da0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'active',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'active',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###