# History log
---
> On devrait écrire ici toutes nos manipulations pour que les autres soient capables de suivre !

> J'ai ajouté des liens vers les commits respectifs pour que ce soit facile de voir l'évolution du projet.

À lister en ordre **décroissant** pour faciliter la recherche.

### . LE TUTORIEL EST TERMINÉ, MAINTENANT FAUDRA GOOGLER POUR AMÉLIORER L'APPLICATION :P
---

### 22. [Deploiement du projet (linux/heroku/docker)](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux)
---

### 22. [Pour aller plus loin](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxiii-application-programming-interfaces-apis)
---

### 21. [Background jobs](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxii-background-jobs)
---

### 20. [Gestion de notifications](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxi-user-notifications)
---

### 19. [Bonus: javascript](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xx-some-javascript-magic)
---

### 18. [Gestion de la recherche](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvi-full-text-search)
---

### 17. [Amélioration de la structure de l'application](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure)
---

### 16. [Gestion de la langue](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n)
---

### 15. [Gestion des dates et du temps](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xii-dates-and-times)
---

### 14. [Support par email](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support)
---

### 13. [Pagination](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ix-pagination)
---

### 12. Ajout du formulaire de Factures
---
J'ai ajouté un formulaire pour la gestion de factures dans `forms.py`, une route dans `routes.py` et l'affichage de ces factures dans `index.html`.
[lien]()

### Je n'ai pas fait la section [Followers](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers)
---

### 11. Gestion des erreurs (il y a juste 404 et 500 qui ont été gérés)
---
J'ai ajouté un module d'erreurs dans le fichier `__init__.py`.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/75a3b3d6bba9326da7a82efbfa61d92564343bf4#diff-9cec7b11237bc29d77a439e81c9b7acfac003d8e8855731eb6bc130b5a8ce602)

J'ai ajouté les fichiers `errors.py`, `404.html` et `500.html`. Pour tester la page 404, visiter une page inexistante. Pour tester la page 500, une des façons est de changer le nom de l'utilisateur `admin` pour un autre utilisateur existant: `admin2`.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/75a3b3d6bba9326da7a82efbfa61d92564343bf4)

Je n'ai pas fait les parties [Sending Errors by Email et Logging to a File](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vii-error-handling).

J'ai géré le bug *si on change le nom d'utilisateur pour un utilisateur qui existe déjà: erreur 500* en modifiant les fichiers `forms.py` et `routes.py`.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/7097fde95ae0359c91fa8a70d71553bc549e9c07)

### 10. Ajout du profil et de l'avatar
---

J'ai ajouté une route dans le fichier `routes.py` vers `/user/<username>`, où *<username>* est le nom d'utilisateur de l'utilisateur courant.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/9a46fb9889616b579f63aebf70587cbf18e709b6#diff-f67826701212aab477be0634a23fdcd7ffdfe748b8ce35eb27b8f690d334c732)

J'ai créé la page `user.html` qui est la page du profil de l'utilisateur.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/9a46fb9889616b579f63aebf70587cbf18e709b6#diff-683c3160e4f8458e32177dbd2f8b46ccaa89779ce95a700e6d70ce9338f1fd45)

J'ai créé une page `_factures.html` que j'appelle dans `user.html`. Le but était de séparer le code. 
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/9a46fb9889616b579f63aebf70587cbf18e709b6#diff-a6d6b64db10f6d2749274e6d7a97987d54edcc06494a59b6a219549cd8409568)

J'ai modifié la barre de navigation de `base.html` pour ajouter le Profil et le Logout sous forme de *dropdown*.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/9a46fb9889616b579f63aebf70587cbf18e709b6#diff-9ba5b84a377a6a734932f7f6a3003e6f8bae1b02c34cf4729cfc95a5fd6179c8)

J'ai ajouté un modèle d'avatar dans `models.py`. J'ai aussi ajouté les sections `about_me` et `last_seen`. J'ai ensuite migré et modifié la base de données.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/9a46fb9889616b579f63aebf70587cbf18e709b6#diff-90c680eba43456b516da8b4c2573d467ae17d1b0ed4373549f2a593ced3616d5)
```bash
(venv) $ flask db migrate -m "ajout de about_me et last_seen"
(venv) $ flask db upgrade
```

J'ai ajouté une section `last_seen` qui dit quand l'utilisateur s'est connecté pour la dernière fois. Cette modification a été faite dans `routes.py`: *The @before_request decorator from Flask register the decorated function to be executed right before the view function. This is extremely useful because now I can insert code that I want to execute before any view function in the application*.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/9a46fb9889616b579f63aebf70587cbf18e709b6#diff-f67826701212aab477be0634a23fdcd7ffdfe748b8ce35eb27b8f690d334c732)

J'ai ajouté un formulaire pour modifier le profil dans `forms.py`.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/9a46fb9889616b579f63aebf70587cbf18e709b6#diff-11d6970831623c0904e31518fb0efd2e718dab0c3b4f00a6a1bd81fb2c707156)

J'ai créé une page `edit_profile.html` pour éditer le profil de l'utilisateur courant.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/9a46fb9889616b579f63aebf70587cbf18e709b6#diff-deb01cb30dcc45affa7777fdee6284aced3d58c1aca021cbadcba0b3208f52f9)

J'ai ajouté la route vers la page `edit_profile.html` dans le fichier `routes.py`
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/9a46fb9889616b579f63aebf70587cbf18e709b6#diff-f67826701212aab477be0634a23fdcd7ffdfe748b8ce35eb27b8f690d334c732)

### 9. Modification du CSS et création d'une page de bienvenue
---
Les fichiers CSS sont dans un répertoire `static`. J'ai dû aussi modifier les fichiers `__init__.py` et `base.html` pour dire où est ce répertoire.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/0a0bb300a4983c34ce19e99c72a5f4be147ea628)

J'ai créé une page de bienvenue `wellcome.html` qui accueille les invités (non connectés). Si un invité essaie d'aller à une page `@login_required`, il sera automatiquement redirigé à cette page-là.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/1b74e07b04e3eb5b84a7f0fad799fbfdbe522347)

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