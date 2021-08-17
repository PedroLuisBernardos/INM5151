# __init__.py
# défini le blueprint des utilisateurs
from flask import Blueprint

bp = Blueprint('user', __name__)

from app.user import routes