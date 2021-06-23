from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from app.models import User
from flask_login import current_user, login_user
from flask_login import logout_user
from flask_login import login_required
from app import db
from app.forms import RegistrationForm

@app.route('/')
@app.route('/index')
@login_required
def index():
    return render_template('index.html', title='Accueil')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Si l'utilisateur est actuellement connecté, ne pas aller a la page /login
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
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
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