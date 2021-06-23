# History log
---
> On devrait écrire ici toutes nos manipulations pour que les autres soient capables de suivre !

À lister en ordre **décroissant** pour faciliter la recherche.

### 7. Ajout de la Database
---
J'ai modifié le fichier `config.py`:
  * Ajout de la variable `SQLALCHEMY_DATABASE_URI`: *Flask-SQLAlchemy extension takes the location of the application's database from the SQLALCHEMY_DATABASE_URI configuration variable*
  * Ajout de la variable `SQLALCHEMY_TRACK_MODIFICATIONS`: *option is set to False to disable a feature of Flask-SQLAlchemy that I do not need*

J'ai modifié le fichier `__init__.py`:
  * Ajout d'un objet `SQLAlchemy`: *represents the database*
  * Ajout d'un objet `Migrate`: *represents the migration engine*
  * Ajout du module `models`: *This module will define the structure of the database.*

J'ai ajouté le fichier `models.py` qui défini les **utilisateurs** et les **factures** avec leur relations

J'ai créé le *migration repository (which is a directory in which it stores its migration scripts. Each time a change is made to the database schema, a migration script is added to the repository with the details of the change)* avec la commande:
```bash
(venv) $ flask db init
```

J'ai fait ma première migration (*to make the database schema match the application models*) avec la commande:
```bash
(venv) $ flask db migrate -m "...commentaire ici..."
```

Pour modifier la base de données (ou pour la créer (le fichier `app.db`) vu qu'elle n'existe pas) j'ai fait la commande ci-dessous. Elle *generates the migration script*
```bash
(venv) $ flask db upgrade
```

> Pour mieux comprendre aller voir la section [Database Upgrade and Downgrade Workflow](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
> La base de données suit maintenant les `models.py` et est prête à être utilisée.

J'ai modifié le fichier `sdf.py` pour qu'on puisse utiliser le `(venv) $ flask shell`. Ceci nous évitera de devoir `import` tous les trucs à *import* lors de nos tests.

> Pour faire un test de tout ceci aller à [Play Time](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)

### 6. Ajout de Bootstrap et modification de `base.html`
---

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
