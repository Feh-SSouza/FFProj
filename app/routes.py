from app.models import usuario
from app import db
from app.forms import LoginForm
from datetime import timedelta
from flask import render_template, request, redirect, url_for, flash, jsonify
from flask_login import login_required, login_user, logout_user
from werkzeug.security import generate_password_hash, check_password_hash
import secrets

def init_app(app):

    @app.route('/')
    def inicio():
        return render_template('inicio.html')
    
    @app.route('/sobre')
    def sobre():
        return render_template('sobre.html')