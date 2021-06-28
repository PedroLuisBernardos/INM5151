# INM5151 Système de Facturation (sdf)
---
Oubliez pas de tout documenter dans les logs et de dire les parties que vous ne faites pas ! Au cas où elles sont aussi utiles ! J'ai mis très brievement ce qu'on doit faire dans les [logs](logs.md) du projet.

## TODO
---
On est rendus [ici (chapitre 9 - Pagination)](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ix-pagination)

* Toutes les sections vides des [logs](logs.md) du projet.

* La route `Modifier des factures` et la page `update_facture.html` n'ont pas le même template que toutes les autres pages/routes. Il faudra le modifier, mais ça fonctionne.

* Remplacer les link style par la librairie [flask-bootstrap](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xi-facelift)

* Améliorer le module Facture en ajoutant des attributs. Faire les modifications nécessaires dans les routes et les pages html concernées.

* Séparer l'ajout de la facture et la page d'affichage de celles-ci.

* Faire la gestion de la barre de recherche.

* Améliorer le CSS.

* Bonus: pouvoir cliquer dans les id des utilisateurs dans la page `/all` et en le faisant faire apparaître les Factures pour cet Utilisateur.

## Documents
---
[OpsCon](https://docs.google.com/document/d/1gFm7OCDQM8OezZi54VzVFRqCNnuyvWAwm8ISOs8H8CQ/edit#)

[PowerPoint OpsCon](https://docs.google.com/presentation/d/1uslppIrlWSKgbWBgeMfVUH1LqGnuOxLnIFBX-3rYHqU/edit)

[Sprint 1](https://docs.google.com/document/d/1YnsLE2BXZ-MREk3PWpu65Rmxpdcfev8nZcXn98PMk6g/edit#)

[Documentation Flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

[Les logs du projet](logs.md)

## Comment utiliser l'application
---
Cloner ce dépôt et accéder au répertoire principal
```bash
$ git clone https://github.com/ta-truong/inm5151-ete2021-projet
$ cd inm5151-ete2021-projet
```

Installer les librairies nescessaires:
```bash
$ pip install -r requirements.txt
```

Rouler l'application
```bash
$ flask run
```

### Ça ne marche pas ?
---
Remplacez `#!/usr/bin/python2` par `#!/usr/bin/python3` dans le fichier `/home/myUser/.local/bin/flask`.

### Allez utiliser l'application !
---
Ouvrir un navigateur et aller à l'adresse: http://127.0.0.1:5000/

Une fois vous avez terminé faites `Ctrl+C` dans votre terminal.

## Pour les administrateurs
---
Un utilisateur de base est déjà présent:
```
user: admin
email: admin@admin.com
pass: admin
```

Pour voir tous les utilisateurs et toutes les factures voir http://127.0.0.1:5000/all
On peut les supprimer dans l'application mais pour le faire en ligne de commande:

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

Pour mettre à jour les nouvelles versions de la bd (en changeant le fichier `modules.py`):
```
(venv) $ flask db migrate -m "message de modification ici"
(venv) $ flask db upgrade
```
En cas d'erreur:
```
(venv) $ flask db downgrade
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
        base.html           --> HTML de base
        index.html          --> page d'accueil des utilisateurs où on voit les factures
        wellcome.html       --> page d'accueil des invités
        login.html          --> page de login
        register.html       --> page d'inscription
        user.html           --> page du profil de l'utilisateur
        edit_profile.html   --> page de modification du profil de l'utilisateur
        update_facture.html --> page de modification de la facture sélectionnée
        404.html            --> page d'erreur 404
        500.html            --> page d'erreur 500
        error.html          --> page d'erreurs généraux
        all.html            --> page cachée, qui contient tous les utilisateurs et toutes les factures
    __init__.py             --> exécute et définit les symboles que les paquets exposent à l'extérieur de l'application
    forms.py                --> définis les formulaires (connexion, inscription ...)
    models.py               --> définis les modèles de la base de données (user, facture ...)
    routes.py               --> définis les routes vers les différentes pages (/, /index, /login, ...)
    errors.py               --> défini les erreurs possibles

migrations/                 --> répertoire qui contient les modifications faites dans la bd

.flaskenv                   --> permet de paramétrer la variable d'environnement FLASK_APP automatiquement
app.db                      --> base de données
config.py                   --> contient les variables de configuration, voir les [logs](logs.md) pour plus d'information
sdf.py                      --> défini l'instance de l'application Flask
requirements.txt            --> liste de librairies à installer
.gitignore
```
