# __init__.py
# défini le blueprint de l'authentication
from flask import Blueprint

bp = Blueprint('auth', __name__)

from app.auth import routes