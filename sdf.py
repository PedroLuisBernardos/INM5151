# sdf.py
# défini l'instance de l'application Flask
from app import app, db, cli
from app.models import User, Facture

# Ceci importera automatiquement les modèles définis et seront disponible dans le Flask Shell
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Facture': Facture}