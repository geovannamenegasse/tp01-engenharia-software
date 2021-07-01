import re
from provasonline import db, login_required
from flask import Blueprint
from flask import render_template, redirect, url_for, flash, request
from provasonline.turma.models.Turma import Turma
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
    # if request.method == 'POST':
        # id = request.form['id']
        # nome = request.form['nome']
        # nome = "%{}%".format(nome)
        # alunos = Aluno.query.all(Turma.nome.like(search), Turma.email.like(search) )
        # shows = [
            # {"nome": 1, "email": "Sesaeme Street"},
            # {"id": 2, "name": "Dora The Explorer"},
        # ]
    return render_template("adicionar_alunos.html", id = id)