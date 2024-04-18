from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def current_user(user_id):
    return usuario.query.get(user_id)

class usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"
    id = db.Column(db.Integer, primary_key=True)
    senha = db.Column(db.String(255), nullable=False)
    nome = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable = False, unique = True)
    data = db.Column(db.DateTime,  default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())   

class receitas(db.Model):
    __tablename__ = "receitas"
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.String(1000), nullable=False)
    ingredientes = db.Column(db.String(1000), nullable=False)
    utensilios = db.Column(db.String(1000), nullable=False)
    tempo = db.Column(db.Integer, nullable=False)
    nota = db.Column(db.String(100), nullable=False)
    dificuldade = db.Column(db.Integer, nullable=False)
