# forms.py
# défini les formulaires en lien avec l'authentication
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from flask_babel import _, lazy_gettext as _l
from datetime import date
from app.models import User

# Défini un formulaire de connexion
class LoginForm(FlaskForm):
    username = StringField(_l('Utilisateur'), validators=[DataRequired(message=_l('Veuillez entrer un utilisateur valide'))])
    password = PasswordField(_l('Mot de passe'), validators=[DataRequired(message=_l('Veuillez entrer un mot de passe valide'))])
    remember_me = BooleanField(_l('Se souvenir de moi'))
    submit = SubmitField(_l('Connexion'))

# Défini un formulaire demande de reinitialisation de mot du passe
class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Adresse courriel'), validators=[DataRequired(message=_l('Veuillez entrer une adresse courriel valide')), Email(message=_l('Veuillez entrer une adresse courriel valide'))])
    submit = SubmitField(_l('Demander la réinitialisation'))

# Défini un formulaire de reinitialisation de mot du passe
class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Mot de passe'), validators=[DataRequired(message=_l('Veuillez entrer un mot de passe valide'))])
    password2 = PasswordField(
        _l('Entrez à nouveau votre mot de passe'), validators=[DataRequired(message=_l('Veuillez entrer à nouveau votre mot de passe')),EqualTo('password',message=_l('Les mots de passe ne sont pas identiques'))])
    submit = SubmitField(_l('Réinitialiser votre mot de passe'))

# Défini un formulaire de création de comptes
class RegistrationForm(FlaskForm):
    username = StringField(_l('Utilisateur'), validators=[DataRequired(message=_l('Veuillez entrer un utilisateur valide'))])
    # le champ Email() vérifie la bonne structure d'une adresse courriel
    email = StringField(_l('Adresse courriel'), validators=[DataRequired(message=_l('Veuillez entrer une adresse courriel valide')), Email(message=_l('Veuillez entrer une adresse courriel valide'))])
    password = PasswordField(_l('Mot de passe'), validators=[DataRequired(message=_l('Veuillez entrer un mot de passe valide'))])
    password2 = PasswordField(
        _l('Entrez à nouveau votre mot de passe'), validators=[DataRequired(message=_l('Veuillez entrer à nouveau votre mot de passe')), EqualTo('password', message=_l('Les mots de passe ne sont pas identiques'))])
    submit = SubmitField(_l('Créer un compte'))

    # Si le nom d'utilisateur existe déjà
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_l('Ce nom d\'utilisateur est déjà utilisé'))

    # Si le email existe déjà
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_l('Cette adresse courriel est déjà utilisée'))