from provasonline import db
class Turma(db.Model):
    __tablename__ = 'turma'
    id              = db.Column(db.Integer, primary_key = True)
    id_professor    = db.Column(db.Integer, db.ForeignKey('usuario.id', ondelete = 'CASCADE'), nullable = True)
    descricao       = db.Column(db.Text, nullable = True)
    nome            = db.Column(db.Text, nullable = True)

    def __init__(self, descricao, nome): #id_professor
        #self.id_professor      = id_professor
        self.descricao = descricao
        self.nome = nome