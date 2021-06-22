# History log
---
On devrait écrire ici toutes nos manipulations pour que les autres soient capables de suivre !
À lister en ordre décroissant pour faciliter la recherche.

### 2. Setup des premiers packages et routes
---
J'ai créé un repertoire `app`

J'ai créé un fichier `__init__.py` qui *executes and defines what symbols the package exposes to the outside world*

J'ai défini le *Python script at the top-level that defines the Flask application instance* et il se nomme `sdf.py` (systemedefacturation)

Pour *set the FLASK_APP environment variable* j'ai créé le fichier `.flaskenv`

### 1. Installation de l'environnement virtuel
---
J'ai installé le **venv** et me suis connecté avec: 
```bash
$ python3 -m venv venv
$ virtualenv venv
$ source venv/bin/activate
```

J'ai aussi installé ces librairies:
```bash
$ pip install flask
$ pip install python-dotenv
$ pip install flask-wtf
$ pip install flask-sqlalchemy
$ pip install flask-migrate
$ pip install flask-login
```
