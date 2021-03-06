"""empty message

Revision ID: bcac38b19c75
Revises: 3818c3caa122
Create Date: 2021-07-03 15:40:19.133310

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bcac38b19c75'
down_revision = '3818c3caa122'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('aluno_na_turma_ibfk_2', 'aluno_na_turma', type_='foreignkey')
    op.drop_constraint('aluno_na_turma_ibfk_1', 'aluno_na_turma', type_='foreignkey')
    op.create_foreign_key(None, 'aluno_na_turma', 'usuario', ['aluno_id'], ['id'], ondelete='CASCADE')
    op.create_foreign_key(None, 'aluno_na_turma', 'turma', ['turma_id'], ['id'], ondelete='CASCADE')
    op.drop_constraint('turma_ibfk_1', 'turma', type_='foreignkey')
    op.create_foreign_key(None, 'turma', 'usuario', ['id_professor'], ['id'], ondelete='CASCADE')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'turma', type_='foreignkey')
    op.create_foreign_key('turma_ibfk_1', 'turma', 'professor', ['id_professor'], ['id'], ondelete='CASCADE')
    op.drop_constraint(None, 'aluno_na_turma', type_='foreignkey')
    op.drop_constraint(None, 'aluno_na_turma', type_='foreignkey')
    op.create_foreign_key('aluno_na_turma_ibfk_1', 'aluno_na_turma', 'aluno', ['aluno_id'], ['id'])
    op.create_foreign_key('aluno_na_turma_ibfk_2', 'aluno_na_turma', 'turma', ['turma_id'], ['id'])
    # ### end Alembic commands ###
