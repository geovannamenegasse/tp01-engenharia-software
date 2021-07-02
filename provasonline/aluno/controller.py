from flask import Blueprint
from provasonline.aluno.models.Aluno import Aluno
from provasonline.turma.models.Turma import Turma
from flask import render_template, redirect, url_for, flash, request

aluno = Blueprint('aluno', __name__, template_folder='templates')

@aluno.route("/listar_alunos", methods=["GET","POST"])
def listar_alunos():
    alunos = Aluno.query.all()
    return render_template("listar_alunos.html", alunos = alunos)

@aluno.route("/ver_aluno/<_id>", methods=["GET","POST"])
def ver_aluno(_id):
    aluno = Aluno.query.get_or_404(_id)
    turmas = aluno.turmas
    return render_template("ver_aluno.html", aluno = aluno, turmas = turmas)