"""Cria tabela contas a pagar e receber

Revision ID: ca69b4ea5332
Revises: 
Create Date: 2024-04-12 23:48:53.107323

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ca69b4ea5332'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contas_a_pagar_e_receber',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('descricao', sa.String(), nullable=False),
    sa.Column('valor', sa.Numeric(), nullable=False),
    sa.Column('tipo', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('contas_a_pagar_e_receber')
    # ### end Alembic commands ###
