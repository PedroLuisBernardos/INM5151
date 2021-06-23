from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User

# Défini un formulaire de connexion
class LoginForm(FlaskForm):
    username = StringField('Utilisateur', validators=[DataRequired(message='Veuillez entrer un utilisateur valide')])
    password = PasswordField('Mot de passe', validators=[DataRequired(message='Veuillez entrer un mot de passe valide')])
    remember_me = BooleanField('Se souvenir de moi')
    submit = SubmitField('Connexion')

# Défini un formulaire de création de comptes
class RegistrationForm(FlaskForm):
    username = StringField('Utilisateur', validators=[DataRequired(message='Veuillez entrer un utilisateur valide')])
    # le champ Email() vérifie la bonne structure d'une adresse courriel
    email = StringField('Email', validators=[DataRequired(message='Veuillez entrer une adresse courriel valide'), Email(message='Veuillez entrer une adresse courriel valide')])
    password = PasswordField('Mot de passe', validators=[DataRequired(message='Veuillez entrer un mot de passe valide')])
    password2 = PasswordField(
        'Entrez à nouveau votre mot de passe', validators=[DataRequired(message='Veuillez entrer à nouveau votre mot de passe'), EqualTo('password', message='Les mots de passe ne sont pas identiques')])
    submit = SubmitField('Créer un compte')

    # Si le nom d'utilisateur existe déjà
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Le nom d\'utilisateur existe déjà.')

    # Si le email existe déjà
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('L\'adresse courriel existe déjà.')