# History log
---
> On devrait écrire ici toutes nos manipulations pour que les autres soient capables de suivre !
> À lister en ordre **décroissant** pour faciliter la recherche.

### 6. Ajout de Bootstrap et modification de `base.html`

### 5. Ajout du formulaire de connexion (la validation n'est pas traitée)
---
J'ai ajouté un formulaire `forms.py` qui défini un *user login form*

J'ai ajouté la page `login.html`

### 4. Ajout d'une SECRET_KEY
---
J'ai créé un fichier de configuration, `config.py`, qui contient une `SECRET_KEY`. Celle-ci sert de *cryptographic key, useful to generate signatures or tokens. The Flask-WTF extension uses it to protect web forms against a nasty attack called Cross-Site Request Forgery or CSRF*

J'ai linké le fichier `config.py` dans `__init__.py`

### 3. Ajout de templates
---
J'ai ajouté un repertoire `templates`, dans lequel j'ai mis un template de base: `base.html` et la page `index.html`

J'ai complexifié un peu le fichier `routes.py` en ajoutant un utilisateur (hardcodé) et une nouvelle route `/index`

### 2. Setup des premiers packages et routes
---
J'ai créé un repertoire `app`

J'ai créé un fichier `__init__.py` qui *executes and defines what symbols the package exposes to the outside world*

J'ai créé un fichier `routes.py` qui contient les routes de notre application

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
