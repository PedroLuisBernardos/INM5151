# models.py
# défini les modèles de classe de l'application, si un modèle est ajouté, modfier le fichier sdf.py
from datetime import datetime
from hashlib import md5
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from time import time
import jwt
from app import app

# Utilisateurs
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    factures = db.relationship('Facture', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)

    # Affichage des utilisateurs
    def __repr__(self):
        return 'User: {}'.format(self.username)

    # Set un mot de passe et le converti en hash_code (pour plus de sécurité)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Vérifie si le mot de passe est le bon
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Get le token pour la reinitialisation du mot de passe
    def get_reset_password_token(self, expires_in=600):
        return jwt.encode({'reset_password': self.id, 'exp': time() + expires_in}, app.config['SECRET_KEY'], algorithm='HS256')

    # Vérifie si le token est le bon
    @staticmethod
    def verify_reset_password_token(token):
        try:
            id = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])['reset_password']
        except:
            return
        return User.query.get(id)

    # Gestion de l'avatar
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# Factures
class Facture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    amount = db.Column(db.Float)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Affichage des factures
    def __repr__(self):
        return 'Facture: {} due pour le {}'.format(self.body,format(self.timestamp))