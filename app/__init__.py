# __init__.py
# exécute et définit les symboles que les paquets exposent à l'extérieur de l'application
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_babel import Babel, lazy_gettext as _l

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
# Si l'utilisateur n'est pas connecte, le rediriger vers /wellcome
login.login_view = 'welcome'
# Modification du message de demande de connexion
login.login_message = _l('Vous devez vous connecter pour accéder à cette page !')
app.static_folder = 'static'
#Gestion de la langue
babel = Babel(app)

# Ceci choisi la meilleure langue à utiliser selon les préférences de l'utilisateur
@babel.localeselector
def get_locale():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

from app import routes, models, errors