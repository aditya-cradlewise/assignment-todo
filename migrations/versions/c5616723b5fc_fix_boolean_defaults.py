"""fix boolean defaults

Revision ID: c5616723b5fc
Revises: e80ff5437ad0
Create Date: 2026-02-24 21:13:55.741585

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c5616723b5fc'
down_revision: Union[str, Sequence[str], None] = 'e80ff5437ad0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.alter_column(
        'todo_lists',
        'is_archived',
        existing_type=sa.Boolean(),
        nullable=False,
        server_default=sa.text('false')
    )

    op.alter_column(
        'todo_items',
        'completed',
        existing_type=sa.Boolean(),
        nullable=False,
        server_default=sa.text('false')
    )

    op.alter_column(
        'todo_items',
        'archived',
        existing_type=sa.Boolean(),
        nullable=False,
        server_default=sa.text('false')
    )


def downgrade():
    op.alter_column('todo_lists', 'is_archived', nullable=True)
    op.alter_column('todo_items', 'completed', nullable=True)
    op.alter_column('todo_items', 'archived', nullable=True)
