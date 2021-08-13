# __init__.py
# exécute et définit les symboles que les paquets exposent à l'extérieur de l'application
from flask import Flask, request, session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from flask_babel import Babel, lazy_gettext as _l
from flask_moment import Moment

app = Flask(__name__)
app.config.from_object(Config)
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
# Si l'utilisateur n'est pas connecte, le rediriger vers /welcome
login.login_view = 'welcome'
# Modification du message de demande de connexion
login.login_message = _l('Vous devez vous connecter pour accéder à cette page !')
app.static_folder = 'static'
#Gestion de la langue
babel = Babel(app)
#Gestion du fuseau horaire selon l'endroit de l'utilisateur
moment = Moment(app)

#Ceci choisi la meilleure langue à utiliser selon les préférences de l'utilisateur
@babel.localeselector
def get_locale():
    # si l'utilisateur a sauvegardé une langue, l'utiliser, sinon prendre la langue du navigateur
    try:
        language = session['language']
    except KeyError:
        language = None
    if language is not None:
        return language
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())
@app.context_processor
def inject_conf_var():
    return dict(AVAILABLE_LANGUAGES=app.config['LANGUAGES'], CURRENT_LANGUAGE=session.get('language',request.accept_languages.best_match(app.config['LANGUAGES'].keys())))

with app.app_context():
    if db.engine.url.drivername == 'sqlite':
        migrate.init_app(app, db, render_as_batch=True)
    else:
        migrate.init_app(app, db)

#Gestion des erreurs
from app.errors import bp as errors_bp
app.register_blueprint(errors_bp)

from app import routes, models