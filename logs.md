# Logs

---
> On devrait écrire ici toutes nos manipulations pour que les autres soient capables de suivre !
> J'ai ajouté des liens vers les commits respectifs pour que ce soit facile de voir l'évolution du projet.

À lister en ordre **décroissant** pour faciliter la recherche.

## Est-ce que ces deux parties sont utiles ?

---
[Chapitre 14 - Ajax](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiv-ajax)

[Chapitre 16 - Full text search](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvi-full-text-search)

### 26. Ajouter de fonctionnalité thème sombre/clair

---

Ajout de fonctionnalité permettant l'affichage de l'application web en mode clair ou sombre 

Toutefois, il faut être connecté et accéder à son profil pour changer le thème. Le thème persiste même après la déconnection.
On devrait peut-être pouvoir changer à partir de n'importe où

[Commit:](https://github.com/ta-truong/inm5151-ete2021-projet/commit/b4266fb3b6bd849be8884ca0db865589d2d6eb13)


### 25. Ajout de la gestion de comptes

---

Idem que contacts.

[commit:](https://github.com/ta-truong/inm5151-ete2021-projet/commit/161afb035c9d3ffe2ae5e3d9f90bfc0f85712d15)

### 24. Ajouter gestion de Profil d'entreprise

---

J'ai déplacé la gestion de factures (initialement à la page d'accueil/index) vers sa propre page `bill.html`

La page d'accueil contient la gestion de profil d'entreprise. On peut ajouter/modifier/supprimer un profil d'entreprise
et un profil d'entreprise lit les factures et contacts correspondant au profil d'entreprise sélectionné.

[Commit:](https://github.com/ta-truong/inm5151-ete2021-projet/commit/c9dea110c4aedd1da2bc7a711d70d9dd3befd7d8)


### 23. Ajouter dropdown Contacts dans le formulaire de Facture

---

J'ai ajouté ces lignes dans `forms.py`:

```python
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app.models import Contact
...
contact = QuerySelectField(query_factory=lambda:Contact.query.all(),get_label="name")
```

Il resterai à ajouter l'option **Créer un Contact** mais j'ignore comment faire.

[Commit:](https://github.com/ta-truong/inm5151-ete2021-projet/commit/e03bcdcc3aeb3971c920d3e4024c67974050d5d9)

### 22. Ajouter la gestion de contacts

---

J'ai ajouter un modèle et table *Contact*: `app.db`, `app/models.py`

Un réajustement de la *db* (`app.db`) a donc été fait: `migrations/versions/75e5773c0465_reajustement_pour_ajouter_table_contact.py`

Le lien de l'onglet *Contacts* est activé: `app/templates/base.html`

On peut désormais *enregistrer*, *modifier* et *supprimer* un contact ainsi qu'une pagination pour l'affichage des contacts (15 par page): `app/routes.py`, `config.py`

Les fichiers *HTML* ajoutés à cet effet sont: `app/templates/contacts.html`, `app/templates/update_contact.html`

[Commit: daa452b4ed6d8d89c3043bcaaf867c618ee6d686](https://github.com/ta-truong/inm5151-ete2021-projet/commit/daa452b4ed6d8d89c3043bcaaf867c618ee6d686)

### 21. Ajouter la gestion du statut (impayée/payée) à la facture

---

J'ai ajouter l'attribut *Statut* au modèle de factures (`app.db`, `app/forms.py`, `app/models.py`, `app/routes.py`).

En SQL, les colonnes de type *boolean* n'existe. Il fonctionne plutôt avec des *INTEGER* dont *0 = False* et *1 = True*.

La *db* (`app.db`) a désormais une colonne *paid*, dont les valeurs possibles sont : 
  * *0* pour faux: impayée
  * *1* pour vrai: payée
    
Désormais, dans la liste d'affichage de factures, la date d'échéance et le statut s'affichent en rouge lorsque la date d'échance est =< à la date d'aujourd'hui et que le statut est « Impayée » (`app/templates/index.html`).

[Commit: 20d396200263bfe6741c8bd06b55fbec7a4be8ee](https://github.com/ta-truong/inm5151-ete2021-projet/commit/20d396200263bfe6741c8bd06b55fbec7a4be8ee)

### 20. Ajouter la gestion de dates et valider l'attribut de référence (facture)

---

J'ai ajouter l'attribut *Date* au modèle de factures. Le type de la colonne *date* dans la *database* (`app.db`) est désormais *DATE* puisque c'est seulement la date qui m'intéresse.
(`app/forms.py`, `app/models.py`, `app/routes.py`)

J'ai ajouter une validation pour la *référence* de la facture pour que celle-ci soit unique (`app/forms.py`).

[Commit: 7d09073a239f18eff792d518244c93a01741a2ef](https://github.com/ta-truong/inm5151-ete2021-projet/commit/7d09073a239f18eff792d518244c93a01741a2ef)

J'ai ajouter l'attribut *Date d'échéance* au modèle de factures (`app.db`, `app/models.py`, `app/routes.py`, ).
Validation: elle doit être => à la date de la facture (`app/forms.py`).
Lorsque la date d'échéance est =< à la date d'aujourd'hui, elle s'affiche en rouge (`app/templates/index.html`, `app/static/css/style.css`).

[Commit: dcd9b420359c96edd7d71134b317827d907c5d3d](https://github.com/ta-truong/inm5151-ete2021-projet/commit/dcd9b420359c96edd7d71134b317827d907c5d3d)

### 19. Rectifier les attributs de facture & database et autres améliorations

---

J'ai corrigé les noms de colonnes de la *database* `app.db`:
* name -> référence
* body -> description
* timestamp -> date

La correction a été fait dans les fichiers: `app/forms.py`, `app/models.py` `app/routes.py`, `app/templates/all.html`, `app/templates/index.html`

J'ai changé l'affichage des attributs des factures pour en garder ceux pertinents (`app/templates/index.html`):
* Référence
* Date
* Description
* Montant ($)
* Options

J'ai modifier les fichiers `app/templates/reset_password.html` et `app/templates/reset_password_request.html` pour l'adapter à la structure du code actuel (*WTForms*)

J'ai améliorer l'affichage de quelques attributs et messages.

[Commit: 5a46deaa328c6d98b9ab9109d94dfb1603bd5426](https://github.com/ta-truong/inm5151-ete2021-projet/commit/5a46deaa328c6d98b9ab9109d94dfb1603bd5426)

### 18. Mettre en "blanc" l'onglet actif

---

Ajout du caractère en blanc sur l'onglet actif en modifiant la `app/templates/base.html` en ajoutant des conditions "if" sur les classes "nav-item" de la balise "li" de chacune des onglets fonctionnels.

Ps: Cette façon de faire a été privilégier car la manière javascript, bien qu'elle peut modifier la classe en ajoutant "active" à la suite du "nav-item" elle ne modifie que la page courante et ne sauvegarde pas la modification lors d'un changement de page. En bref, le changement se fait en une fraction de seconde (lors du clique sur l'onglet) et à la nouvelle page, elle retourne comme avant. À moins d'utiliser un "LocalStorage" ou une base de donnée pour traiter ces changements, j'ai décidé d'opter pour la méthode conditionnelle avec python qui semble être plus simple. Est-ce la meilleur solution? Je ne sais pas.


### 17. Support par email pour la réinitialisation d'un mot de passe

---

J'ai ajouté un lien sur la page de connection (`app/templates/login.html`) qui dirige vers un formulaire qui permet de ***demander*** une réinitialisation du mot de passe (`app/templates/reset_password_request.html`) : les instructions sont envoyées au courriel soumis (il doit être inscrit dans la *db*).
Une route et un formulaire ont donc été ajouté : `app/routes.py`, `app/forms.py`.

J'ai ajouté le nouvelle *requirement* `pyjwt` (`requirements.txt`) et des *functions* qui permet de générer et de vérifier un *token* pour s'assurer que seuls les liens valides peuvent être utilisés pour réinitialiser le mot de passe (`app/models.py`).

J'ai ajouté le fichier `app/templates/email/reset_password.html` pour le *body* du courriel de réinitialisation du mot de passe (instructions et lien).

J'ai créer un courriel *gmail* : `systemedefacturation@gmail.com` qui se trouve dans `app.config['ADMINS']['email']` pour nous permettre d'envoyer des courriels. Le mot de passe est celle de `app.config[SECRET_KEY]`. Voir `config.py`.

J'ai ajouté le fichier `app/email.py` qui permet d'initialiser le courriel à cet effet et de l'envoyer à l'utilisateur.

J'ai ajouté le fichier `app/templates/reset_password.html` qui permet de ***réinitialiser*** le mot de passe.
Une route (lien + *token*) et un formulaire ont donc été ajouté : `app/routes.py`, `app/forms.py`

[Commit : d54896cf5ff709a7deeea89a4e636c6903e0276f](https://github.com/ta-truong/inm5151-ete2021-projet/commit/d54896cf5ff709a7deeea89a4e636c6903e0276f)

### 16. Traduction en anglais et en espagnol

---

J'ai fait la gestion de la traduction (sauf les dates). Tous les fichiers ont été modifiés pour pouvoir être traduits.

Pour les fichiers `html`, procéder de cette façon:
```html
{{ _("S'inscrire") }}
```

Pour les fichiers `py`, procéder de cette façon:
Utiliser `_()` ou `_l()` selon les `import` du fichier.
```
_l('Entrez à nouveau votre mot de passe')
_('Accueil')
```

Un fichier de configuration a été ajouté: `babel.cfg`. Des configurations supplémentaires ont été ajoutées dans `__init__.py`, `config.py` et `sdf.py`.

Les `requierements` ont été modifiés.

Un fichier `cli.py` a été ajouté pour simplifier les commandes:

avant:
```bash
pybabel init -i messages.pot -d app/translations -l <language>
pybabel extract -F babel.cfg -k _l -o messages.pot .
pybabel compile -d app/translations
```

après
```bash
flask translate init <language>
flask translate update
flask translate compile
```

Des fichiers `translations/en/messages.po` et `translations/es/messages.po` ont été modifiés grâce à l'outil [Poedit](https://poedit.net). On peut aussi les modifier directement.

Les fichiers `messages.mo` sont les fichiers compilés.

#### Comment faire si vous ajoutez des textes à traduire ?

---

* Utilisez la bonne syntaxe comme expliqué ci-dessus.

* `flask translate update`

* Modifier les fichiers `messages.po`

* `flask translate compile`

[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/c6f328270c148fe3130d0d1303946f2dbd5c8157)

### 15. Pagination

---

J'ai géré la pagination de factures. Une variable `FACTURES_PAR_PAGE` est définie dans `config.py`. Les routes de `/index` ont été modifiées dans `routes.py` et la page `index.html` a été ajustée.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/dbc43cf86a07e11a3f7d444fdc1add3c5ae5a71e)

### 14. Amélioration du CSS, ajout du Makefile et amélioration du modèle de Facture

---

J'ai ajouté la librairie `flask-bootstrap` et j'ai modifié les formulaires grâce à `bootstrap/wtf.html` sauf celui dans la page `update_facture.html`.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/060b1d880803f4b977af0086639ae373fe495903)

J'ai modifié le modèle de base du fichier `base.html` en suivant la structure de bootstrap.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/060b1d880803f4b977af0086639ae373fe495903#diff-9ba5b84a377a6a734932f7f6a3003e6f8bae1b02c34cf4729cfc95a5fd6179c8)

J'ai ajouté un fichier Makefile pour faciliter la saisie de commandes.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/79153ff7295e6f87da2f63f713d6a24a9ad0dd89#diff-76ed074a9305c04054cdebb9e9aad2d818052b07091de1f20cad0bbac34ffb52)

J'ai amélioré le modèle de Facture en ajoutant d'autres attributs. Les modifications respectives ont été faites dans les fichiers suivants: `forms.py`, `models.py`, `routes.py`, `index.html` et `update_facture.html`.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/79153ff7295e6f87da2f63f713d6a24a9ad0dd89)

### 13. Gestion des erreurs dans les routes, amélioration de l'installation des librairies et ajout d'une page pour les tests

---
J'ai ajouté une page `all.html` (et sa route dans `routes.py`) qui contient la liste de tous les utilisateurs et toutes les factures.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/0570b73396c11ada16fb15039e8b07a8d8acf562#diff-0ff488b2e6357717687f02abc57d83507dca9b1e2d32c3b0f7f33df64098a3a7)

J'ai amélioré la gestion d'erreurs dans `routes.py` et j'ai créé une page personnalisée pour les erreurs: `error.html`.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/0570b73396c11ada16fb15039e8b07a8d8acf562#diff-f67826701212aab477be0634a23fdcd7ffdfe748b8ce35eb27b8f690d334c732)

J'ai ajouté le fichier `requirements.txt` qui contient toutes les librairies à installer pour pouvoir utiliser l'application. L'information est dans le [README](README.md)
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/ca7e19f75822e013ec7546b7825f75f01515baaf#diff-4d7c51b1efe9043e44439a949dfd92e5827321b34082903477fd04876edb7552)

### 12. Ajout du formulaire de Factures, de modification/suppression de factures et suppression des utilisateurs

---
J'ai ajouté un formulaire pour la gestion de factures dans `forms.py`, une route dans `routes.py` et l'affichage de ces factures dans `index.html`. J'ai aussi migré et upgradé la base de données avec le modèle de `Facture`.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/e288e2cc463b10461dd070f6bd90982a8bb827fb)

J'ai ajouté la gestion de modification/suppression de factures dans `routes.py`, `index.html` et `update_facture.html` et la gestion de suppression du compte dans `user.html` et `routes.py`.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/67a41090b6d2ad46135acc5ec80dcd5f86280afa)

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

### 10. Ajout du profil, de l'avatar et d'une page de modification du profil

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
flask db migrate -m "ajout de about_me et last_seen"
flask db upgrade
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

### 8. Ajout des formulaires de Logins/Logout/Register et amélioration de routes

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

### 7. Ajout de la Database, modeles d'Utilisateur et de Facture

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
flask db init
```

J'ai fait ma première migration (*to make the database schema match the application models*) avec la commande:

```bash
flask db migrate -m "...commentaire ici..."
```

Pour modifier la base de données (ou pour la créer (le fichier `app.db`) vu qu'elle n'existe pas) j'ai fait la commande ci-dessous. Elle *generates the migration script*

```bash
flask db upgrade
```

> Pour mieux comprendre, allez voir la section [Database Upgrade and Downgrade Workflow](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)
> La base de données suit maintenant les `models.py` et est prête à être utilisée.

J'ai modifié le fichier `sdf.py` pour qu'on puisse utiliser le `flask shell`. Ceci nous évitera de devoir `import` tous les trucs à *import* lors de nos tests.
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/733837a6abbeb6594f8cca5808b33e237abcd197#diff-c99a9313c27a862fb4664512cff6e9111cafd41bc9f44657edfc9b58d3589289)

> Pour faire un test de tout ceci aller à [Play Time](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database)

### 6. Ajout de Bootstrap et modification de `base.html`

---
[lien](https://github.com/ta-truong/inm5151-ete2021-projet/commit/4b4d0e3be6e40b319a1c1ce9ce1bc70bdf5666a1#diff-9ba5b84a377a6a734932f7f6a3003e6f8bae1b02c34cf4729cfc95a5fd6179c8)

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

### 3. Ajout de templates et de routes

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

### 1. Installation de l'environnement virtuel et des libraires

---
J'ai installé le **venv** et me suis connecté avec:

```bash
python3 -m venv venv
virtualenv venv
source venv/bin/activate
```

J'ai aussi installé ces librairies:

```bash
pip install flask
pip install python-dotenv
pip install flask-wtf
pip install flask-sqlalchemy
pip install flask-migrate
pip install flask-login
pip install email-validator
```
