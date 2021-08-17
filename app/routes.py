# routes.py
# défini les routes de l'application
from datetime import datetime
from flask import render_template, redirect, url_for, session
from flask_login import current_user
from app import app, db
from app.models import User, Facture
from flask_babel import _

# Page d'accueil pour les invités
@app.route('/')
@app.route('/welcome')
def welcome():
    # Si l'utilisateur est actuellement connecté, ne pas aller à la page /welcome
    if current_user.is_authenticated:
        return redirect(url_for('entrees.index'))
    return render_template('welcome.html', title=_('Bienvenue'))

# Pour savoir c'est quand la dernière fois que l'utilisateur s'est connecté
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

# UNIQUEMENT POUR LES ADMINISTRATEURS
@app.route('/all')
def all():
    users = User.query.all()
    factures = Facture.query.all()
    return render_template('all.html', users=users, factures=factures)

# Modifier la langue
@app.route('/language/<language>')
def set_language(language=None):
    session['language'] = language
    return redirect(url_for('entrees.index'))
