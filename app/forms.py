# forms.py
# défini les formulaires de l'application
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, DecimalField, DateField, SelectField
from wtforms.validators import NumberRange, ValidationError, DataRequired, Email, EqualTo, Length
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flask_babel import _, lazy_gettext as _l
from datetime import date
from app.models import User, Contact, CompanyProfil, Compte
import re
from flask_login import current_user

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
                raise ValidationError(_l('Ce nom d\'utilisateur est déjà utilisé'))

# Défini un formulaire pour la saisie de factures
class FactureForm(FlaskForm):
    # À ajouter des attributs
    paid = SelectField('', choices=[(0, _l('Impayée')), (1, _l('Payée'))], coerce=int)
    reference = StringField(_l('Référence'), validators=[DataRequired(message=_l("Veuillez entrer une référence")), Length(min=1, max=50, message=_l('Veuillez écrire entre 1 et 50 caractères'))])
    date = DateField(_l('Date'), default=date.today(), format='%Y-%m-%d', validators=[DataRequired(message=_l("Veuillez entrer une date (AAAA-MM-JJ)"))])
    due_date = DateField(_l('Date d\'échéance'), format='%Y-%m-%d', validators=[DataRequired(message=_l("Veuillez entrer une date d'échéance (AAAA-MM-JJ)"))])
    description = TextAreaField(_l('Description'), validators=[DataRequired(message=_l("Veuillez entrer une description")), Length(min=1, max=140, message=_l(_l('Veuillez écrire entre 1 et 140 caractères')))])
    subtotal = DecimalField(_l('Sous-total'), validators=[DataRequired(message=_l("Veuillez entrer un montant numérique"))], places=2)
    tax = DecimalField(_l('Taxe (%)'), default=14.975, validators=[NumberRange(0, 100, _l("Veuillez entrer un nombre entre 0 et 100"))], places=3)

    contact_id = SelectField(_l('Contact ID'), validators=[DataRequired(message=_l('Veuillez entrer un contact'))])

    # Query qui get tous les comptes de l'utilisateur actif
    def get_comptes():
        return Compte.query.filter_by(user_id=current_user.id)

    compte_id = QuerySelectField(_l('Compte ID'), validators=[DataRequired(message=_l('Veuillez entrer un compte'))], query_factory=get_comptes, get_label="name", allow_blank=True)

    submit = SubmitField(_l('Enregistrer'))

    # Valider si date d'échéance est la même ou après la date initiale
    def validate_due_date(self, due_date):
        if due_date.data < self.date.data:
            raise ValidationError(_l('La date d\'échéance doit être la même ou après la date initale'))

    # Get le montant total après taxes en arrondissant à 2 décimals
    @staticmethod
    def get_total(tax, sub_total):
        return round((sub_total * (tax + 100) / 100), 2)

# Défini un formulaire pour la saisie de contacts
class ContactForm(FlaskForm):
    # Validation à améliorer
    name = StringField(_l('Nom'), validators=[DataRequired(message=_l("Veuillez entrer un nom")), Length(min=1, max=50, message=_l('Veuillez écrire entre 1 et 50 caractères'))])
    phone_number = StringField(_l('Téléphone'), [DataRequired(Length(min=12, max=12, message=_l('Veuillez entrer un numéro de téléphone (123-456-7890)')))])
    email = StringField(_l('Adresse courriel'), validators=[DataRequired(message=_l('Veuillez entrer une adresse courriel valide')), Email(message=_l('Veuillez entrer une adresse courriel valide'))])
    address = TextAreaField(_l('Adresse'), validators=[DataRequired(message=_l("Veuillez entrer une adresse")), Length(min=1, max=140, message=_l(_l('Veuillez écrire entre 1 et 140 caractères')))])
    submit = SubmitField(_l('Enregistrer'))

    def validate_phone_number(self, phone_number):
        phone_number = phone_number.data
        pattern = "^\d{3}-\d{3}-\d{4}$"
        match = re.search(pattern, phone_number)
        if not match:
            raise ValidationError(_l('Veuillez entrer un numéro de téléphone valide (123-456-7890)'))

# Défini un formulaire pour la saisie de comptes
class CompteForm(FlaskForm):
    name = StringField(_l('Nom'), validators=[DataRequired(message=_l("Veuillez entrer un nom")), Length(min=1, max=50, message=_l('Veuillez écrire entre 1 et 50 caractères'))])
    submit = SubmitField(_l('Enregistrer'))

# Défini un formulaire pour la profil d'entreprise
class CompanyProfilForm(FlaskForm):
    # Validation à améliorer
    name = StringField(_l('Nom'), validators=[DataRequired(message=_l("Veuillez entrer un nom")), Length(min=1, max=50, message=_l('Veuillez écrire entre 1 et 50 caractères'))])
    submit = SubmitField(_l('Enregistrer'))

# Défini un formulaire de sélection de profil d'entreprise
class SelectCompanyProfilForm(FlaskForm):
    # Query qui get tous les contacts de l'utilisateur actif
    def get_company_profil():
        return CompanyProfil.query.filter_by(user_id=current_user.id)

    company_profil_name = QuerySelectField(_l('Nom de l\'entreprise'), validators=[DataRequired(message=_l('Veuillez choisir un profil d\'entreprise'))], query_factory=get_company_profil, get_label="name", allow_blank=False)
    submit = SubmitField(_l('Sélectionner'))