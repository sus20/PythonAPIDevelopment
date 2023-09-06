"""add content column to posts table

Revision ID: cb38c0beecfb
Revises: 06ea2a76759f
Create Date: 2023-09-06 10:43:09.532061

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'cb38c0beecfb'
down_revision: Union[str, None] = '06ea2a76759f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op. drop_column('posts', 'content')
    pass
