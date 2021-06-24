# config.py
# contient les variables e configuration de l'application
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    # YzNjbC0zNXQtYzRjaDM= peut être n'importe quoi
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'YzNjbC0zNXQtYzRjaDM='

    # Base de données
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False