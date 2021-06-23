from app import app, db
from app.models import User, Facture

# Ceci importera automatiquement les modeles definis et seront disponibles dans le flask shell
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Facture': Facture}