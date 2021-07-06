# INM5151 Système de Facturation (sdf)

---
Oubliez pas de tout documenter dans les logs et de dire les parties que vous ne faites pas ! Au cas où elles sont aussi utiles ! J'ai mis très brievement ce qu'on doit faire dans les [logs](logs.md) du projet.

On est rendus [ici (chapitre 9 - Pagination)](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ix-pagination)

## TODO sprint 2

---

* Mettre en gras l'onglet actif. Présentement le seul onglet en gras est **Accueil** à cause du `<li class="nav-item active">`.

* Traduire tout ce qui est en anglais en français: modifier le texte `Edit Profile` dans son profil pour `Modifier mon profil`, les erreurs dans les formulaires, les hover dans les formulaires, etc.

* Ajouter une pagination et une navigation entre facutres. [Voir comment faire ici](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ix-pagination).

* Ajouter un support par email et une réinialisation de mot de passe. [Voir comment faire ici](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-x-email-support).

* Ajouter une gestion des dates et du temps. Ceci modifiera le `timestamp` du modèle `Facture` aussi. [Voir comment faire ici](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xii-dates-and-times).

* Ajouter une gestion de la langue. [Voir comment faire ici](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n).

* Améliorer la structure de l'application. [Voir comment faire ici](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure).

* Faire la gestion de la barre de recherche. [Voir comment faire ici](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvi-full-text-search).

* Faire la gestion des notifications. [Voir comment faire ici](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxi-user-notifications).

* Ajouter un modèle `profil d'entreprise` et une page `profils_entreprise.html`. Cette page sera la première page que l'utilisateur **connecté** verra. On va devoir **ajouter**, **modifier** et **supprimer** des profils d'entreprise (au maximum 5). Une fois le profil sélectionné, on est redirigés à la page `index.html`. Ajouter dans la barre de navigation (sûrement dans le *drop-down* de **Mon profil** un lien pour modifier le profil courrant).

* Améliorer le module **Facture** en ajoutant des attributs. Faire les modifications nécessaires dans les routes et les pages html concernées.
  * Un deuxième `id`. Lui qui est déjà présent est l'id de la base de données, nous on veut un deuxième `id`, **unique** et **personnalisable**. L'ajouter dans le formulaire et dans l'affichage des factures.
  * Un booléen nommé `paiement`, en *drop-down*: **payée** ou **non-payée**. L'ajouter dans le formulaire et dans l'affichage des factures. Par défaut, se placer sur `non-payée`.
  * Une valeur fixe `taxe` qui est de **14.975%**. L'ajouter dans le formulaire et dans l'affichage des factures. Faire le calcul du montant `amount` automatiquement.
  * Un *drop-down* **modifiable** nommé `comptes de revenus/dépenses`. Il va avoir une page pour les créer et ils seront disponibles dans le *drop-down* des factures. On doit aussi pouvoir les créer directement dans ce *drop-down* (l'option est à la toute fin). L'ajouter dans le formulaire et dans l'affichage des factures.
  * idem mais nommé `contacts`.
  * Créer une page nommée `modele_facture.html` dans la barre de navigation. Il y aura un formulaire qui nous permet d'ajouter des modèles de facture. Ces modèles seront visibles dans l'ajout (uniquement l'ajout) de factures sous forme de *drop-down*. On doit aussi pouvoir les créer directement dans ce *drop-down* (l'option est à la toute fin).

## TODO sprint 3

---

* Ajouter du javascript. [Voir comment faire ici](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xx-some-javascript-magic).

* Lui je sais pas c'est quoi, faudra voir si c'est pertinent. Ajouter des background jobs. [Voir comment faire ici](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxii-background-jobs).

* Gérer l'exportation de factures en format PDF.

* Ajouter un favicon

* Gérer l'envoi des factures par email (exportées en PDF).

* Si c'est pas déjà fait, gérer les notifications de rappel par email (le email qui est dans le modèle `User`).

* Gérer le filtrage de factures.

* Gérer le calcul des montants des factures sélectionnées.

* Gérer la modification du thème (page supplémentaire dans **Mon profil**).

* Séparer l'ajout de la facture et la page d'affichage de celles-ci.

* Modifier les bouttons Modifier et Supprimer de la page `index.html`.

* Améliorer le CSS pour rendre l'application plus belle.

* Ajouter des `try/except` dans **toutes** les routes du fichier `routes.py`.

* *Bonus: pouvoir cliquer dans les id des utilisateurs dans la page `/all` et en le faisant faire apparaître les Factures pour cet Utilisateur.*

* Pour aller plus loin selon Miguel. [Voir comment faire ici](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxiii-application-programming-interfaces-apis). Aussi, pour aller plus loin, section sur les APIs. [Voir comment faire ici](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxiii-application-programming-interfaces-apis).

* Déploiement sur Héroku, Linux ou Docker. Faudra en choisir un des trois. [Voir comment faire ici](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvii-deployment-on-linux).

## Documents

---
[OpsCon](https://docs.google.com/document/d/1gFm7OCDQM8OezZi54VzVFRqCNnuyvWAwm8ISOs8H8CQ/edit#)

[PowerPoint OpsCon](https://docs.google.com/presentation/d/1uslppIrlWSKgbWBgeMfVUH1LqGnuOxLnIFBX-3rYHqU/edit)

[Sprint 1](https://docs.google.com/document/d/1YnsLE2BXZ-MREk3PWpu65Rmxpdcfev8nZcXn98PMk6g/edit#)

[PowerPoint Sprint 1](https://docs.google.com/presentation/d/1ovp0vUbbqoy77J7YeX1wLURpROjskBO-f2CdZjpM9RQ/edit?usp=sharing)

[Documentation Flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

[Les logs du projet](logs.md)

## Comment utiliser l'application

---
Cloner ce dépôt et accéder au répertoire principal

```bash
git clone https://github.com/ta-truong/inm5151-ete2021-projet
cd inm5151-ete2021-projet
```

### Vous avez deux possibilités

---

#### 1: Makefile

---

Faites uniquement la commande suivante:

```bash
make
```

#### 2: Au long

---

Installer les librairies nescessaires:

```bash
pip install -r requirements.txt
```

Rouler l'application

```bash
flask run
```

### Ça ne marche pas ?

---
Remplacez `#!/usr/bin/python2` par `#!/usr/bin/python3` dans le fichier `/home/myUser/.local/bin/flask`.

### Allez utiliser l'application

---
Ouvrir un navigateur et aller à l'adresse: <http://127.0.0.1:5000/>

Une fois vous avez terminé faites `Ctrl+C` dans votre terminal.

## Pour les administrateurs

---
Un utilisateur de base est déjà présent:

```
user: admin
email: admin@admin.com
pass: admin
```

Pour voir tous les utilisateurs et toutes les factures voir <http://127.0.0.1:5000/all>
On peut les supprimer dans l'application mais pour le faire en ligne de commande:

```bash
flask shell
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

Pour mettre à jour les nouvelles versions de la bd (en changeant le fichier `modules.py`):

```bash
flask db migrate -m "message de modification ici"
flask db upgrade
```

En cas d'erreur:

```bash
flask db downgrade
```

## Explication des répertoires et des fichiers

---

```
app/                        --> répertoire qui héberge l'application
    static/                 --> répertoire qui contient les fichiers statiques de l'application
        css/                --> répertoire qui contient le CSS de l'application
            style.css       --> CSS de l'application (en plus de Bootstrap)
        js/                 --> répertoire qui contient le JS de l'application
            script.js       --> JS de l'application (en plus de Bootstrap)
    templates/              --> répertoire qui contient les modèles des pages HTML
        404.html            --> page d'erreur 404
        500.html            --> page d'erreur 500
        all.html            --> page cachée, qui contient tous les utilisateurs et toutes les factures
        base.html           --> HTML de base
        edit_profile.html   --> page de modification du profil de l'utilisateur
        error.html          --> page d'erreurs généraux
        index.html          --> page d'accueil des utilisateurs où on voit les factures
        login.html          --> page de login
        register.html       --> page d'inscription
        user.html           --> page du profil de l'utilisateur
        update_facture.html --> page de modification de la facture sélectionnée
        wellcome.html       --> page d'accueil des invités
    __init__.py             --> exécute et définit les symboles que les paquets exposent à l'extérieur de l'application
    errors.py               --> défini les erreurs possibles
    forms.py                --> défini les formulaires (connexion, inscription ...)
    models.py               --> défini les modèles de la base de données (user, facture ...)
    routes.py               --> défini les routes vers les différentes pages (/, /index, /login, ...)

migrations/                 --> répertoire qui contient les modifications faites dans la bd

.flaskenv                   --> permet de paramétrer la variable d'environnement FLASK_APP automatiquement
.gitignore                  --> permet de ne pas ajouter au dépôt certains fichiers
app.db                      --> base de données
config.py                   --> contient les variables de configuration, voir les [logs](logs.md) pour plus d'information
Makefile                    --> permet de rouler l'application en une seule commande
requirements.txt            --> liste de librairies à installer
sdf.py                      --> défini l'instance de l'application Flask
```
