# __init__.py
# défini le blueprint du core de l'application
from flask import Blueprint

bp = Blueprint('entrees', __name__)

from app.entrees import routes