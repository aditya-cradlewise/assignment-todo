"""create todo app

Revision ID: e80ff5437ad0
Revises: 
Create Date: 2026-02-22 18:34:13.417534

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e80ff5437ad0'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        "todo_lists",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String, nullable=False),
        sa.Column("is_archived", sa.Boolean, default=False),
        sa.Column("created_at", sa.DateTime, server_default=sa.func.now())
    )

    op.create_table(
        "todo_items",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("list_id", sa.Integer, sa.ForeignKey("todo_lists.id")),
        sa.Column("title", sa.String),
        sa.Column("completed", sa.Boolean, default=False),
        sa.Column("due_date", sa.DateTime),
        sa.Column("expiry", sa.DateTime),
        sa.Column("archived", sa.Boolean, default=False)
    )



def downgrade():
    op.drop_table("todo_items")
    op.drop_table("todo_lists")
