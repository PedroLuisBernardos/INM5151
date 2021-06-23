# History log
---
> On devrait écrire ici toutes nos manipulations pour que les autres soient capables de suivre !

> J'ai ajouté des liens vers les commits respectifs pour que ce soit facile de voir l'évolution du projet.

À lister en ordre **décroissant** pour faciliter la recherche.

### 9. Modification du CSS
---
Les fichiers CSS sont dans un répertoire `static`. J'ai dû aussi modifier les fichiers `__init__.py` et `base.html` pour dire où est ce répertoire.
> PAR CONTRE MOI DANS MON ORDI LE CSS NE SEMBLE PAS MARCHER. SI VOUS MODIFIEZ `style.css` CA MARCHE PAS et jsp pourquoi :(

### 8. Ajout des User Logins/Logout/Register
---
J'ai modifié le fichier `models.py` en ajoutant des fonctions de génération et de vérification du mot de passe. J'ai aussi ajouté l'attribut `UserMixin` aux `User` pour avoir accès à des méthodes plus avancées telles que: *is_authenticated* ou *is_active*. J'ai ajouté le module `@login.user_loader` qui permet de suivre quel utilisateur est actuellement connecté (si j'ai bien compris la partie [User Loader Function](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins))
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/78994ab4a81d2dd0d3e84014803277537aa26c99#diff-90c680eba43456b516da8b4c2573d467ae17d1b0ed4373549f2a593ced3616d5)

J'ai modifié le fichier `__init__.py` pour initialiser l'instance de Flask-Login. J'ai aussi ajouté une option: si l'utilisateur n'est pas connecté, le rediriger vers la page `/login`.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/78994ab4a81d2dd0d3e84014803277537aa26c99#diff-9cec7b11237bc29d77a439e81c9b7acfac003d8e8855731eb6bc130b5a8ce602)

J'ai modifié le fichier `routes.py` pour pouvoir vérifier si l'user/mdp sont les bons. Si oui, les logger à l'application grâce à Flask-Login. J'ai aussi ajouté une route `/logout`. J'ai ajouté le champ `@login_required` à aux pages qui en avaient besoin. Une route vers `register.html` a été ajoutée.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/78994ab4a81d2dd0d3e84014803277537aa26c99#diff-f67826701212aab477be0634a23fdcd7ffdfe748b8ce35eb27b8f690d334c732)

J'ai ajouté dans la nav-bar de `base.html` la route `/logout` avec la condition *si l'utilisateur actuel est anonyme, afficher Login, sinon, afficher Logout*.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/78994ab4a81d2dd0d3e84014803277537aa26c99#diff-9ba5b84a377a6a734932f7f6a3003e6f8bae1b02c34cf4729cfc95a5fd6179c8)

J'ai ajouté un formulaire d'inscription dans le fichier `forms.py`.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/78994ab4a81d2dd0d3e84014803277537aa26c99#diff-11d6970831623c0904e31518fb0efd2e718dab0c3b4f00a6a1bd81fb2c707156)

Une nouvelle page a été ajoutée: `register.html`.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/78994ab4a81d2dd0d3e84014803277537aa26c99#diff-92eef37adb55fb4a2979aae075f722a09d73a6ce9f51e08895027852d5448fd0)

Un lien vers `register.html` a été ajouté dans `login.html`.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/78994ab4a81d2dd0d3e84014803277537aa26c99#diff-e1bc6bd8e3e268d122beae1cfee7bb0e06013a19b8fd6fe8b15b40f90b98a019)

J'ai installé:
```bash
(venv) $ pip install flask-login
(venv) $ pip install email-validator
```

#### Pour supprimer les utilisateurs de la bd:
```bash
(venv) $ flask shell
>>> users = User.query.all()
>>> for u in users:
...     db.session.delete(u)
...
>>> factures = Facture.query.all()
>>> for f in factures:
...     db.session.delete(f)
...
>>> db.session.commit()
```

### 7. Ajout de la Database
---
J'ai modifié le fichier `config.py`. [lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/733837a6abbeb6594f8cca5808b33e237abcd197#diff-117426151e93a626f8b46bfdb3a95b3f4a62e5f4dd6e65975a7c50759bf04482)
  * Ajout de la variable `SQLALCHEMY_DATABASE_URI`: *Flask-SQLAlchemy extension takes the location of the application's database from the SQLALCHEMY_DATABASE_URI configuration variable*
  * Ajout de la variable `SQLALCHEMY_TRACK_MODIFICATIONS`: *option is set to False to disable a feature of Flask-SQLAlchemy that I do not need*

J'ai modifié le fichier `__init__.py`. [lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/733837a6abbeb6594f8cca5808b33e237abcd197#diff-9cec7b11237bc29d77a439e81c9b7acfac003d8e8855731eb6bc130b5a8ce602)
  * Ajout d'un objet `SQLAlchemy`: *represents the database*
  * Ajout d'un objet `Migrate`: *represents the migration engine*
  * Ajout du module `models`: *This module will define the structure of the database.*

J'ai ajouté le fichier `models.py` qui définit les **utilisateurs** et les **factures** avec leurs relations.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/733837a6abbeb6594f8cca5808b33e237abcd197#diff-90c680eba43456b516da8b4c2573d467ae17d1b0ed4373549f2a593ced3616d5)

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

> Pour mieux comprendre, allez voir la section [Database Upgrade and Downgrade Workflow](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
> La base de données suit maintenant les `models.py` et est prête à être utilisée.

J'ai modifié le fichier `sdf.py` pour qu'on puisse utiliser le `(venv) $ flask shell`. Ceci nous évitera de devoir `import` tous les trucs à *import* lors de nos tests.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/733837a6abbeb6594f8cca5808b33e237abcd197#diff-c99a9313c27a862fb4664512cff6e9111cafd41bc9f44657edfc9b58d3589289)

> Pour faire un test de tout ceci aller à [Play Time](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)

### 6. Ajout de Bootstrap et modification de `base.html`. [lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/4b4d0e3be6e40b319a1c1ce9ce1bc70bdf5666a1#diff-9ba5b84a377a6a734932f7f6a3003e6f8bae1b02c34cf4729cfc95a5fd6179c8)
---

### 5. Ajout du formulaire de connexion (la validation n'est pas traitée)
---
J'ai ajouté un formulaire `forms.py` qui défini un *user login form*.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/7e313bca354ba3bda5ad2f701d52d2087318ae18#diff-11d6970831623c0904e31518fb0efd2e718dab0c3b4f00a6a1bd81fb2c707156)

J'ai ajouté la page `login.html`.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/acbc8b0e93c67c4bff3d98fe81e991aba639a995#diff-e1bc6bd8e3e268d122beae1cfee7bb0e06013a19b8fd6fe8b15b40f90b98a019)

### 4. Ajout d'une SECRET_KEY
---
J'ai créé un fichier de configuration, `config.py`, qui contient une `SECRET_KEY`. Celle-ci sert de *cryptographic key, useful to generate signatures or tokens. The Flask-WTF extension uses it to protect web forms against a nasty attack called Cross-Site Request Forgery or CSRF*.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/7e313bca354ba3bda5ad2f701d52d2087318ae18#diff-117426151e93a626f8b46bfdb3a95b3f4a62e5f4dd6e65975a7c50759bf04482)

J'ai linké le fichier `config.py` dans `__init__.py`.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/7e313bca354ba3bda5ad2f701d52d2087318ae18#diff-9cec7b11237bc29d77a439e81c9b7acfac003d8e8855731eb6bc130b5a8ce602)

### 3. Ajout de templates
---
J'ai ajouté un répertoire `templates`, dans lequel j'ai mis un template de base: `base.html` et la page `index.html`.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/7e313bca354ba3bda5ad2f701d52d2087318ae18#diff-a18b3b5de30df1bcf7531723d24c214d69b2acff3cd88540e1ff186409879b0a)

J'ai complexifié un peu le fichier `routes.py` en ajoutant un utilisateur (hardcodé) et une nouvelle route `/index`.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/7e313bca354ba3bda5ad2f701d52d2087318ae18#diff-f67826701212aab477be0634a23fdcd7ffdfe748b8ce35eb27b8f690d334c732)

### 2. Setup des premiers packages et routes
---
J'ai créé un répertoire `app`

J'ai créé un fichier `__init__.py` qui *executes and defines what symbols the package exposes to the outside world*.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/4e74287b7a72e8af79cd3fde4cdafad2dd1c40e7#diff-9cec7b11237bc29d77a439e81c9b7acfac003d8e8855731eb6bc130b5a8ce602)

J'ai créé un fichier `routes.py` qui contient les routes de notre application.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/4e74287b7a72e8af79cd3fde4cdafad2dd1c40e7#diff-f67826701212aab477be0634a23fdcd7ffdfe748b8ce35eb27b8f690d334c732)

J'ai défini le *Python script at the top-level that defines the Flask application instance* et il se nomme `sdf.py` (systemedefacturation).
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/4e74287b7a72e8af79cd3fde4cdafad2dd1c40e7#diff-c99a9313c27a862fb4664512cff6e9111cafd41bc9f44657edfc9b58d3589289)

Pour *set the FLASK_APP environment variable* j'ai créé le fichier `.flaskenv`.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/4e74287b7a72e8af79cd3fde4cdafad2dd1c40e7#diff-49203977c1cb1429e3b5e556e63eb8850f78c6362e53239c451388f7dbfb7ff9)

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