from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Utilisateur', validators=[DataRequired(message='Veuillez entrer un utilisateur valide')])
    password = PasswordField('Mot de passe', validators=[DataRequired(message='Veuillez entrer un mot de passe valide')])
    remember_me = BooleanField('Se souvenir de moi')
    submit = SubmitField('Connexion')