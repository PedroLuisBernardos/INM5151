# routes.py
# défini les routes en lien avec l'authentication
from datetime import date, datetime
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user, current_user
from app import db
from app.auth import bp
from app.auth.forms import LoginForm, RegistrationForm, ResetPasswordRequestForm, ResetPasswordForm
from app.models import User
from flask_babel import _
from app.auth.email import send_password_reset_email

# Se connecter
@bp.route('/login', methods=['GET', 'POST'])
def login():
  try:
    # Si l'utilisateur est actuellement connecté, ne pas aller à la page /login
    if current_user.is_authenticated:
      return redirect(url_for('entrees.index'))
    form = LoginForm()
    # Si le form a été submit
    if form.validate_on_submit():
      # filter.by va lire la base de données. S'il y a un match ou pas, il va mettre cette valeur dans la variable user
      user = User.query.filter_by(username=form.username.data).first()
      # Si l'utilisateur n'existe pas OU si le mot de passe est incorrect... Erreur !
      if user is None or not user.check_password(form.password.data):
        flash(_('Utilisateur ou mot de passes invalides !'))
        return redirect(url_for('auth.login'))
      # Si l'utilisateur et le mdp sont justes, le Flask-Forms va le marquer comme logged. Des variables comme current_user seront maintenant remplies
      login_user(user, remember=form.remember_me.data)
      return redirect(url_for('entrees.index'))
    return render_template('auth/login.html', title=_('Connexion'), form=form)
  except Exception:
    error_string = _('Il y a eu une erreur avec la connexion.')
    return render_template('errors/error.html', title=_('Erreur'), error=error_string)

# Se déconnecter
@bp.route('/logout')
def logout():
  try:
    # Si l'utilisateur est actuellement connecté, le déconnecter
    if current_user.is_authenticated:
      logout_user()
      flash(_('Vous avez été déconnecté.'))
      return redirect(url_for('welcome'))
    return redirect(url_for('entrees.index'))
  except Exception:
    error_string = _('Il y a eu une erreur avec la déconnexion.')
    return render_template('errors/error.html', title=_('Erreur'), error=error_string)

# Page de de demande de réinitialisation du mot de passe
@bp.route('/reset_password_request', methods=['GET', 'POST'])
def reset_password_request():
  if current_user.is_authenticated:
    return redirect(url_for('entrees.index'))
  form = ResetPasswordRequestForm()
  if form.validate_on_submit():
    user = User.query.filter_by(email=form.email.data).first()
    if user:
      send_password_reset_email(user)
      flash(_('Consultez vos courriels pour réinitialiser votre mot de passe.'))
      return redirect(url_for('auth.login'))
    else:
      flash(_('Cette adresse courriel n\'est pas inscrite.'))
  return render_template('email/reset_password_request.html', title=_('Réinitialiser un mot de passe'), form=form)

# Page de réinitialisation du mot de passe
@bp.route('/reset_password/<token>', methods=['GET', 'POST'])
def reset_password(token):
  if current_user.is_authenticated:
    return redirect(url_for('entrees.index'))
  user = User.verify_reset_password_token(token)
  if not user:
    return redirect(url_for('entrees.index'))
  form = ResetPasswordForm()
  if form.validate_on_submit():
    user.set_password(form.password.data)
    db.session.commit()
    flash(_('Votre mot de passe a été réinitialisé.'))
    return redirect(url_for('auth.login'))
  return render_template('email/reset_password.html', title=_('Réinitialiser un mot de passe'), form=form)

# Page d'enregistrement
@bp.route('/register', methods=['GET', 'POST'])
def register():
  try:
    # Si l'utilisateur est actuellement connecté, ne pas aller à la page /login
    if current_user.is_authenticated:
      return redirect(url_for('entrees.index'))
    form = RegistrationForm()
    if form.validate_on_submit():
      user = User(username=form.username.data, email=form.email.data)
      user.set_password(form.password.data)
      db.session.add(user)
      db.session.commit()
      flash(_('Vous êtes maintenant inscrit !'))
      return redirect(url_for('auth.login'))
    return render_template('auth/register.html', title=_('S\'inscrire'), form=form)
  except Exception:
    error_string = _('Il y a eu une erreur avec l\'inscription.')
    return render_template('errors/error.html', title=_('Erreur'), error=error_string)
  