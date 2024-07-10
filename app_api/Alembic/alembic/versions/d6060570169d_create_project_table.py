"""Create Project table

Revision ID: d6060570169d
Revises: 
Create Date: 2024-07-07 17:34:17.760639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd6060570169d'
down_revision = None
branch_labels = None
depends_on = None

table_name = "Student"


def upgrade():
    op.create_table(
        table_name,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(20), unique=True, nullable=False),
        sa.Column("teacher", sa.String(50), nullable=False),
    )


def downgrade():
    op.drop_table(table_name)
