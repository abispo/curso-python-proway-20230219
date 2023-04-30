"""Criada model Log

Revision ID: 387d7ddd7101
Revises: 001c994f0021
Create Date: 2023-04-30 15:18:53.801409

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '387d7ddd7101'
down_revision = '001c994f0021'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_logs',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('log', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_logs')
    # ### end Alembic commands ###