# routes.py
# défini les routes de l'application
from datetime import datetime
from flask import render_template, flash, redirect, url_for, request
from flask.globals import session
from flask_login import login_user, logout_user, current_user, login_required
from werkzeug.urls import url_parse
from app import app, db
from app.forms import LoginForm, RegistrationForm, EditProfileForm, FactureForm
from app.models import Facture, User

# Page d'accueil pour les utilisateurs
@app.route('/index', methods=['GET', 'POST'])
@login_required
def index():
    form = FactureForm()
    # À ajouter des attributs
    if form.validate_on_submit():
        facture = Facture(body=form.body.data, author=current_user)
        db.session.add(facture)
        db.session.commit()
        flash('Votre facture a été ajoutée.')
        return redirect(url_for('index'))
    # Toutes les factures de l'utilisateur actuel
    factures = Facture.query.filter_by(user_id=current_user.id).all()
    return render_template("index.html", title='Accueil', form=form, factures=factures)

# Page d'accueil pour les invités
@app.route('/')
@app.route('/wellcome')
def wellcome():
    # Si l'utilisateur est actuellement connecté, ne pas aller à la page /wellcome
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    return render_template('wellcome.html', title='Bienvenue')

# Se connecter
@app.route('/login', methods=['GET', 'POST'])
def login():
    try:
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
    except:
        error_string = 'Il y a eu une erreur avec la connexion.'
        return render_template('error.html', title='Erreur', error=error_string)

# Se déconnecter
@app.route('/logout')
def logout():
    try:
        # Si l'utilisateur est actuellement connecté, le déconnecter
        if current_user.is_authenticated:
            logout_user()
            flash('Vous avez été déconnecté')
            return redirect(url_for('wellcome'))
        return redirect(url_for('index'))
    except:
        error_string = 'Il y a eu une erreur avec la déconnexion.'
        return render_template('error.html', title='Erreur', error=error_string)

# Page d'enregistrement
@app.route('/register', methods=['GET', 'POST'])
def register():
    try:
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
    except:
        error_string = 'Il y a eu une erreur avec l\'inscription.'
        return render_template('error.html', title='Erreur', error=error_string)

# Page profil
@app.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', title='Mon profil', user=user)

# Supprimer un utilisateur et toutes ses factures
@app.route('/delete_user/<username>')
@login_required
def delete_user(username):
    try:
        user = User.query.filter_by(username=username).first_or_404()
        factures = Facture.query.filter_by(user_id=user.id).all()
        for f in factures:
            db.session.delete(f)
        logout_user()
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('wellcome'))
    except:
        error_string = 'Il y a eu une erreur avec la suppression de l\'utilisateur.'
        return render_template('error.html', title='Erreur', error=error_string)

# Supprimer des factures
@app.route('/delete/<facture_id>')
@login_required
def delete(facture_id):
    facture_to_delete = Facture.query.get_or_404(facture_id)
    try:
        db.session.delete(facture_to_delete)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        error_string = 'Il y a eu une erreur avec la suppression de la facture.'
        return render_template('error.html', title='Erreur', error=error_string)

# Modifier des factures
@app.route('/update/<facture_id>', methods=['GET', 'POST'])
def update(facture_id):
    facture_to_update = Facture.query.get_or_404(facture_id)
    if request.method == 'POST':
        # À ajouter des attributs
        facture_to_update.body = request.form['body']
        try:
            db.session.commit()
            return redirect(url_for('index'))
        except:
            error_string = 'Il y a eu une erreur avec la modification de la facture.'
            return render_template('error.html', title='Erreur', error=error_string)
    else:
        return render_template('update_facture.html', title='Modification de factures', facture=facture_to_update)

# Pour savoir c'est quand la dernière fois que l'utilisateur s'est connecté
@app.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

# Modifier son profil
@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    try:
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
    except:
        error_string = 'Il y a eu une erreur avec la modification du profil.'
        return render_template('error.html', title='Erreur', error=error_string)

@app.route('/all')
# UNIQUEMENT POUR LES ADMINISTRATEURS
def all():
    users = User.query.all()
    factures = Facture.query.all()
    return render_template('all.html', users=users, factures=factures)