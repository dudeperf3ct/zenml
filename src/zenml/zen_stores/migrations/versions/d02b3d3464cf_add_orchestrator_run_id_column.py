"""Add orchestrator_run_id column [d02b3d3464cf].

Revision ID: d02b3d3464cf
Revises: ccd68b7825ae
Create Date: 2022-10-26 16:50:44.965578

"""

import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "d02b3d3464cf"
down_revision = "ccd68b7825ae"
branch_labels = None
depends_on = None


def upgrade() -> None:
    """Upgrade database schema and/or data, creating a new revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("pipelinerunschema", schema=None) as batch_op:
        batch_op.add_column(
            sa.Column(
                "orchestrator_run_id",
                sqlmodel.sql.sqltypes.AutoString(),
                nullable=True,
            )
        )

    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade database schema and/or data back to the previous revision."""
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table("pipelinerunschema", schema=None) as batch_op:
        batch_op.drop_column("orchestrator_run_id")

    # ### end Alembic commands ###
