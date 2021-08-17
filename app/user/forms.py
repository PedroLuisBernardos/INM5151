# forms.py
# défini les formulaires en lien avec les utilisateurs
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Length
from flask_babel import _, lazy_gettext as _l
from app.models import User

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
