from app.models import usuario
from app.models import receitas
from app import db
from app.forms import LoginForm
from datetime import timedelta
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import secrets


## return render_template("/inicio.html", usuarios=db.session.execute(db.select(usuario).order_by(usuario.id)).scalars()) 

def init_app(app):



    @app.route('/')
    def inicio():
        return render_template('inicio.html')
    
    @app.route('/sobre')
    def sobre():
        return render_template('sobre.html')
    
    @app.route('/excluir/<int:id>')
    def excluir_receita(id):
        delete=receitas.query.filter_by(id=id).first()
        db.session.delete(delete)
        db.session.commit()
        return redirect(url_for('lista_receita'))
    
    @app.route('/receitas')
    def lista_receita():
        return render_template('receitas.html', receitas=db.session.execute(db.select(receitas).order_by(receitas.id)).scalars())
    
    @app.route('/cadreceita', methods=["GET", "POST"])
    def cad_receita():
        if request.method == "POST":
            receita = receitas()
            receita.nome = request.form["nome"]
            receita.descricao = request.form["descricao"]
            receita.ingredientes = request.form["ingredientes"]
            receita.utensilios = request.form["utensilios"]
            receita.tempo = request.form["tempo"]
            receita.nota = request.form["nota"]
            receita.dificuldade = request.form["dificuldade"]
            db.session.add(receita)
            db.session.commit()

            flash("Receita adicionada a lista!")
            return redirect(url_for('lista_receita'))
        return render_template('cad_receita.html')
    
    @app.route('/atualizar/<int:id>', methods=["GET", "POST"])
    def atualizar_receita(id):
        atualiza=receitas.query.filter_by(id=id).first()
        if request.method == "POST":
            nome_receita = request.form["nome"]
            descricao_receita = request.form["descricao"]
            ingrediente_receita = request.form["ingredientes"]
            utensilios_receita = request.form["utensilios"]
            tempo_receita = request.form["tempo"]
            nota_receita = request.form["nota"]
            dificuldade_receita = request.form["dificuldade"]

            flash("Receita alterada com sucesso!")

            atualiza.query.filter_by(id=id).update({"nome":nome_receita, "descricao":descricao_receita, "ingredientes":ingrediente_receita,
             "utensilios":utensilios_receita, "tempo":tempo_receita, "nota":nota_receita, "dificuldade":dificuldade_receita})
            db.session.commit()
            return redirect(url_for("lista_receita"))
        return render_template('atualizar_receita.html', atualiza=atualiza)