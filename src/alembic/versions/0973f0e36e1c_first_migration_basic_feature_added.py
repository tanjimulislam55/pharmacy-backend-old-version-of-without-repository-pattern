"""first migration - basic feature added

Revision ID: 0973f0e36e1c
Revises: 6fc0f9c424a8
Create Date: 2021-12-09 12:00:31.152662

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '0973f0e36e1c'
down_revision = '6fc0f9c424a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customers', sa.Column('bloodgroup', sa.Enum('ap', 'an', 'bp', 'bn', 'op', 'on', 'abp', 'abn', name='bloodgroupenum'), nullable=True))
    op.drop_column('customers', 'blood_group')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customers', sa.Column('blood_group', mysql.ENUM('ap', 'an', 'bp', 'bn', 'op', 'on', 'abp', 'abn'), nullable=True))
    op.drop_column('customers', 'bloodgroup')
    # ### end Alembic commands ###