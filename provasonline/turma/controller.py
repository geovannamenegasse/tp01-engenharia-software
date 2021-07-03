import re
from provasonline import db, login_required
from flask import Blueprint
from flask import render_template, redirect, url_for, flash, request
from provasonline.turma.models.Turma import Turma , AlunoTurma
from provasonline.aluno.models.Aluno import Aluno
import json

turma = Blueprint('turma', __name__, template_folder='templates')

@turma.route("/listar_turmas", methods=["GET","POST"])
def listar_turmas():
    turmas = Turma.query.all()
    return render_template("listar_turmas.html", turmas=turmas)

@turma.route("/cadastrar_turma", methods=["GET", "POST"])
def cadastrar_turma():
    if request.method == 'POST':

        # descricao = request.form['prova']
        nome = request.form['nome']
        descricao = request.form['descricao']
        turma     = Turma(descricao, nome)
        db.session.add(turma)
        db.session.commit()
        flash("Prova cadastrada com sucesso")
        return redirect(url_for('turma.listar_turmas'))
    return render_template("cadastrar_turma.html")

@turma.route("/adicionar_alunos", methods=["GET", "POST"])
def adicionar_alunos():
    id = request.args.get('id')
    alunos = db.session.query(Aluno, AlunoTurma).outerjoin(AlunoTurma, (Aluno.id == AlunoTurma.aluno_id) & (AlunoTurma.turma_id == id)).all()

    if request.method == 'POST':
        lista_id = request.form.getlist('alunos')
        id_turma = request.form['id_turma']
        AlunoTurma.query.filter(AlunoTurma.turma_id == id_turma).delete()
        db.session.commit()
        for id_user in lista_id:
            alunoturma = AlunoTurma(id_user, id_turma)
            db.session.add(alunoturma)
            db.session.commit()
        id = id_turma
        return redirect(url_for('turma.adicionar_alunos', id=id))
    return render_template("adicionar_alunos.html", id = id, alunos = alunos)

@turma.route("/ver_turma/<_id>", methods=["GET","POST"])
def ver_turma(_id):
    turma = Turma.query.get_or_404(_id)
    return render_template("ver_turma.html", turma=turma)
