# forms.py
# défini les formulaires de l'application
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DecimalField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from flask_babel import _, lazy_gettext as _l
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
            raise ValidationError(_l('Ce nom d\'utilisateur a déjà été utilisé.'))

    # Si le email existe déjà
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_l('Cette adresse courriel a déjà été utilisée.'))

# Modifier le profil de l'utilisateur
class EditProfileForm(FlaskForm):
    username = StringField(_l('Utilisateur'), validators=[DataRequired(message=_l("Veuillez saisir un nom d'utilisateur"))])
    about_me = TextAreaField(_l('À propos de moi'), validators=[Length(min=0, max=140)])
    submit = SubmitField(_l('Enregistrer'))

    # @Override du constructeur. Il a maintenant comme argument le original_username=current_user.username
    def __init__(self, original_username, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)
        self.original_username = original_username

    # Valider si l'utilisateur existe déjà
    def validate_username(self, username):
        if username.data != self.original_username:
            user = User.query.filter_by(username=self.username.data).first()
            if user is not None:
                raise ValidationError(_l('Ce nom d\'utilisateur a déjà été utilisé.'))

# Défini un formulaire pour la saisie de factures
class FactureForm(FlaskForm):
    # À ajouter des attributs
    name = TextAreaField(_l('Entrez le nom de votre facture'), validators=[DataRequired(message=_l("Veuillez entrer un nom")), Length(min=1, max=50, message=_l('Veuillez écrire entre 1 et 50 caractères'))])
    body = TextAreaField(_l('Entrez la description de votre facture'), validators=[DataRequired(message=_l("Veuillez entrer une description")), Length(min=1, max=140, message=_l(_l('Veuillez écrire entre 1 et 50 caractères')))])
    amount = DecimalField(_l('Entrez le montant de votre facture'), validators=[DataRequired(message=_l("Veuillez entrer un montant numérique"))], places=2)
    submit = SubmitField(_l('Enregistrer'))