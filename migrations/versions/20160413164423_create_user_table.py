"""create user table

Revision ID: f9d9c8e5ec6f
Revises: 
Create Date: 2016-04-13 16:44:23.998925

"""

# revision identifiers, used by Alembic.
revision = 'f9d9c8e5ec6f'
down_revision = None
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa

roles = ('admin', 'common')

def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String(20), nullable=False),
        sa.Column('password', sa.String(32), nullable=False),
        sa.Column('role', sa.Enum(*roles), nullable=False, server_default='common'),
        sa.Column('atime', sa.Integer, nullable=False)
    )


def downgrade():
    op.drop_table('user')
