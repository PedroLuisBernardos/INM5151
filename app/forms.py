# forms.py
# défini les formulaires de l'application
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
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
            raise ValidationError('Ce nom d\'utilisateur a déjà été utilisé.')

    # Si le email existe déjà
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Cette adresse courriel a déjà été utilisée.')

# Modifier le profil de l'utilisateur
class EditProfileForm(FlaskForm):
    username = StringField('Utilisateur', validators=[DataRequired(message="Veuillez saisir un nom d'utilisateur")])
    about_me = TextAreaField('À propos de moi', validators=[Length(min=0, max=140)])
    submit = SubmitField('Soumettre')

    # @Override du constructeur. Il a maintenant comme argument le original_username=current_user.username
    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    # Valider si l'utilisateur existe déjà
    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError('Ce nom d\'utilisateur a déjà été utilisé.')

# Défini un formulaire pour la saisie de factures
class FactureForm(FlaskForm):
    # À ajouter des attributs
    facture = TextAreaField('Entrez votre facture', validators=[DataRequired(message="Veuillez écrire entre 1 et 140 caractères"), Length(min=1, max=140)])
    submit = SubmitField('Enregistrer')