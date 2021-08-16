# __init__.py
# défini le blueprint des erreurs

from flask import Blueprint

bp = Blueprint('errors', __name__)

from app.errors import handlers