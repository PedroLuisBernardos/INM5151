from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
# Si l'utilisateur n'est pas connecte, le rediriger vers /login
login.login_view = 'login'
# Modification du message de demande de connexion
login.login_message = "Vous devez vous connecter pour accéder à cette page !"

from app import routes, models