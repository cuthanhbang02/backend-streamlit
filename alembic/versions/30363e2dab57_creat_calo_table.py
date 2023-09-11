"""creat calo table

Revision ID: 30363e2dab57
Revises: 56939d841878
Create Date: 2023-09-08 12:12:32.275340

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '30363e2dab57'
down_revision = '56939d841878'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('calo',
    sa.Column('id', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('created_date', sa.String(), nullable=False),
    sa.Column('calo_in', sa.Float(), nullable=False),
    sa.Column('calo_out', sa.Float(), nullable=False),
    sa.Column('calo_diff', sa.Float(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.Column('updated_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('calo')
    # ### end Alembic commands ###