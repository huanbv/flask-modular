"""new migrate íntance

Revision ID: c46eb1ec3b4a
Revises: 22f600decef8
Create Date: 2021-08-09 22:55:00.766364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c46eb1ec3b4a'
down_revision = '22f600decef8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('first_name',
               existing_type=sa.VARCHAR(length=30),
               nullable=False)
        batch_op.alter_column('last_name',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.alter_column('password_hash',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
        batch_op.alter_column('last_name',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
        batch_op.alter_column('first_name',
               existing_type=sa.VARCHAR(length=30),
               nullable=True)

    # ### end Alembic commands ###
