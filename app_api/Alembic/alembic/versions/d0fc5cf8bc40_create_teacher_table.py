"""Create teacher table

Revision ID: d0fc5cf8bc40
Revises: d6060570169d
Create Date: 2024-07-07 17:43:16.796928

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0fc5cf8bc40'
down_revision = 'd6060570169d'
branch_labels = None
depends_on = None

teacher_table_name = "Teacher"
project_table_name = "Teacher"


def upgrade():
    op.create_table(
        teacher_table_name,
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("name", sa.String(50), nullable=False),
        sa.Column("age", sa.Integer, nullable=False),
    )
    op.create_foreign_key("fk_teacher_subject_id", )


def downgrade():
    op.drop_table(teacher_table_name)
