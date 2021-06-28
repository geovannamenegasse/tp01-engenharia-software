"""tabela_turma

Revision ID: 01bc05d69e09
Revises: 
Create Date: 2021-06-26 15:02:11.203138

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '01bc05d69e09'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('turma',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_foreign_key(None, 'resposta', 'prova', ['prova'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'resposta', type_='foreignkey')
    op.drop_table('turma')
    # ### end Alembic commands ###