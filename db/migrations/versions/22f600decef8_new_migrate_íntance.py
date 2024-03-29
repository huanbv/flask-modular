"""new migrate íntance

Revision ID: 22f600decef8
Revises: 2083853331e9
Create Date: 2021-08-09 22:54:03.880111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22f600decef8'
down_revision = '2083853331e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('first_name', sa.String(length=30), nullable=True))
        batch_op.add_column(sa.Column('last_name', sa.String(length=20), nullable=True))
        batch_op.add_column(sa.Column('password_hash', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('password_hash')
        batch_op.drop_column('last_name')
        batch_op.drop_column('first_name')

    # ### end Alembic commands ###
