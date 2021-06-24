# routes.py
# défini les routes de l'application
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm
from app.models import User

@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Accueil')

@app.route('/')
@app.route('/wellcome')
def wellcome():
    # Si l'utilisateur est actuellement connecté, ne pas aller à la page /wellcome
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('wellcome.html', title='Bienvenue')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Si l'utilisateur est actuellement connecté, ne pas aller à la page /login
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    # Si le form a été submit
    if form.validate_on_submit():
        # filter.by va lire la base de données. S'il y a un match ou pas, il va mettre cette valeur dans la variable user
        user = User.query.filter_by(username=form.username.data).first()
        # Si l'utilisateur n'existe pas OU si le mot de passe est incorrect... Erreur !
        if user is None or not user.check_password(form.password.data):
            flash('Utilisateur ou mot de passes invalides !')
            return redirect(url_for('login'))
        # Si l'utilisateur et le mdp sont justes, le Flask-Forms va le marquer comme logged. Des variables comme current_user seront maintenant remplies
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Connexion', form=form)

@app.route('/logout')
def logout():
    # Si l'utilisateur est actuellement connecté, le déconnecter
    if current_user.is_authenticated:
        logout_user()
        flash('Vous avez été déconnecté')
        return redirect(url_for('wellcome'))
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Si l'utilisateur est actuellement connecté, ne pas aller à la page /login
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Vous êtes maintenant inscrit !')
        return redirect(url_for('login'))
    return render_template('register.html', title='S\'inscrire', form=form)

@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    # Ceci sont des factures example, on les enlèvera quand on sauvegardera des factures dans la bd
    factures = [
        {'author': user, 'body': 'Test facture #1'},
        {'author': user, 'body': 'Test facture #2'}
    ]
    return render_template('user.html', user=user, factures=factures)

# Pour savoir c'est quand la dernière fois que l'utilisateur s'est connecté
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm(current_user.username)
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.about_me = form.about_me.data
        db.session.commit()
        flash('Les modifications ont été sauvegardées')
        return redirect(url_for('user', username=current_user.username))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', title='Modifier votre profil',form=form)