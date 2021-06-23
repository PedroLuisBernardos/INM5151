from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
# Si l'utilisateur n'est pas connecte, le rediriger vers /wellcome
login.login_view = 'wellcome'
# Modification du message de demande de connexion
login.login_message = "Vous devez vous connecter pour accéder à cette page !"
app.static_folder = 'static'

from app import routes, models