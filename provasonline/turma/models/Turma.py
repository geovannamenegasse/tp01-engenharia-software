from provasonline import db

AlunoTurma = db.Table("aluno_na_turma",
             db.Column('aluno_id', db.Integer, db.ForeignKey('aluno.id')),
             db.Column('turma_id', db.Integer, db.ForeignKey('turma.id')))


class Turma(db.Model):
    __tablename__ = 'turma'
    id              = db.Column(db.Integer, primary_key = True)
    id_professor    = db.Column(db.Integer, db.ForeignKey('professor.id', ondelete = 'CASCADE'), nullable = True)
    descricao       = db.Column(db.Text, nullable = True)
    nome            = db.Column(db.Text, nullable = True)

    alunos = db.relationship("Aluno", secondary=AlunoTurma, back_populates="turmas")

    def __init__(self, descricao, nome): #id_professor
        #self.id_professor      = id_professor
        self.descricao = descricao
        self.nome = nome