"""Add user relationship to Reservation

Revision ID: 5a12786b8dd8
Revises: c1677783e2d4
Create Date: 2024-09-20 01:19:03.805743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a12786b8dd8'
down_revision = 'c1677783e2d4'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        batch_op.add_column(sa.Column('user_id', sa.Integer(), nullable=True))
        # В этой строке вместо None укажите название внешнего ключа.
        batch_op.create_foreign_key('fk_reservation_user_id_user', 'user', ['user_id'], ['id'])


def downgrade():
    with op.batch_alter_table('reservation', schema=None) as batch_op:
        # В этой строке вместо None укажите название внешнего ключа.
        batch_op.drop_constraint('fk_reservation_user_id_user', type_='foreignkey')
        batch_op.drop_column('user_id')

    # ### end Alembic commands ###
