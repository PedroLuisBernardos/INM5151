from datetime import datetime
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import login

# Utilisateurs
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Facture', backref='author', lazy='dynamic')

    # Affichage des utilisateurs
    def __repr__(self):
        return '<Utilisateur: {}>'.format(self.username)

    # Set un mot de passe et le converti en hash_code (pour plus de securite)
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Verifie si le mot de passe est le bon
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))

# Factures
class Facture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Affichage des factures
    def __repr__(self):
        return '<Facture: {} due pour le {}>'.format(self.body,format(self.timestamp))