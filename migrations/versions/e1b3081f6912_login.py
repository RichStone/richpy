"""login

Revision ID: e1b3081f6912
Revises: 55b71673d58e
Create Date: 2017-06-09 20:38:16.768796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1b3081f6912'
down_revision = '55b71673d58e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.String(length=64), nullable=True))
    op.add_column('users', sa.Column('password_hash', sa.String(length=128), nullable=True))
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_column('users', 'password_hash')
    op.drop_column('users', 'email')
    # ### end Alembic commands ###
