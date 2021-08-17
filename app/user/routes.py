# routes.py
# défini les routes de l'application en lien avec les utilisateurs
from datetime import date, datetime
from flask import render_template, flash, redirect, url_for, request, session
from flask_login import logout_user, current_user, login_required
from app import app, db
from app.user import bp
from app.user.forms import EditProfileForm
from app.models import User, Facture
from flask_babel import _

# Page profil
@bp.route('/user/<username>')
@login_required
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user/user.html', title=_('Mon profil'), user=user)

# Supprimer un utilisateur et toutes ses factures
@bp.route('/delete_user/<username>')
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
        return redirect(url_for('welcome'))
    except:
        error_string = _('Il y a eu une erreur avec la suppression de l\'utilisateur.')
        return render_template('errors/error.html', title=_('Erreur'), error=error_string)
        
# Modifier son profil
@bp.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    try:
        form = EditProfileForm(current_user.username)
        if form.validate_on_submit():
            current_user.username = form.username.data
            current_user.about_me = form.about_me.data
            db.session.commit()
            flash(_('Les modifications ont été sauvegardées.'))
            return redirect(url_for('user.user', username=current_user.username))
        elif request.method == 'GET':
            form.username.data = current_user.username
            form.about_me.data = current_user.about_me
        return render_template('user/edit_profile.html', title=_('Modifier votre profil'),form=form)
    except:
        error_string = _('Il y a eu une erreur avec la modification du profil.')
        return render_template('errors/error.html', title=_('Erreur'), error=error_string)