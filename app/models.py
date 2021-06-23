from datetime import datetime
from app import db

# Utilisateurs
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Facture', backref='author', lazy='dynamic')

    # Affichage des utilisateurs
    def __repr__(self):
        return '<Utilisateur: {}>'.format(self.username)

# Factures
class Facture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    # Affichage des factures
    def __repr__(self):
        return '<Facture: {} due pour le {}>'.format(self.body,format(self.timestamp))