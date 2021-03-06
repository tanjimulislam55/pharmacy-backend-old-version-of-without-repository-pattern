"""edited users table columns

Revision ID: 01747ae6ec32
Revises: 0973f0e36e1c
Create Date: 2021-12-09 15:20:21.006642

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '01747ae6ec32'
down_revision = '0973f0e36e1c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.String(length=255), nullable=True))
    op.add_column('users', sa.Column('deactivated', sa.Boolean(), nullable=False))
    op.drop_column('users', 'hashed_password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('hashed_password', mysql.VARCHAR(length=255), nullable=True))
    op.drop_column('users', 'deactivated')
    op.drop_column('users', 'password')
    # ### end Alembic commands ###
