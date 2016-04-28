"""add admin user

Revision ID: cfcae550a784
Revises: f9d9c8e5ec6f
Create Date: 2016-04-14 14:09:51.503822

"""

# revision identifiers, used by Alembic.
revision = 'cfcae550a784'
down_revision = 'f9d9c8e5ec6f'
branch_labels = None
depends_on = None

import time
from alembic import op
import sqlalchemy as sa


def upgrade():
    now = int(time.time())
    op.execute("insert into user(username, password, role, atime) \
            values('ruanzhao', 'ruanzhao', 'admin', {})".format(now))


def downgrade():
    op.execute("delete from user where username = 'ruanzhao'")
