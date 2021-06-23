# INM5151 Système de Facturation (sdf)
---
## Documents
---
[OpsCon](https://docs.google.com/document/d/1gFm7OCDQM8OezZi54VzVFRqCNnuyvWAwm8ISOs8H8CQ/edit#)

[Sprint 1](https://docs.google.com/document/d/1YnsLE2BXZ-MREk3PWpu65Rmxpdcfev8nZcXn98PMk6g/edit#)

[Documentation Flask - on est rendus chapitre 6 - Profil page and Avatars](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-vi-profile-page-and-avatars)

[PowerPoint présentation du projet](https://docs.google.com/presentation/d/1uslppIrlWSKgbWBgeMfVUH1LqGnuOxLnIFBX-3rYHqU/edit)

## [Les logs du projet](History-log.md)
---

## Comment utiliser l'application
---
Cloner ce dépôt et accéder au répertoire principal
```bash
$ git clone https://github.com/ta-truong/inm5151-ete2021-projet
$ cd inm5151-ete2021-projet
```

Se connecter à l'environnement virtuel avec la commande:
```bash
$ source venv/bin/activate
```

Rouler l'application
```bash
(venv) $ flask run
```

Ouvrir un navigateur et aller à l'adresse: http://127.0.0.1:5000/

## Explication des répertoires et des fichiers
---
```
app/              --> répertoire qui héberge l'application
    templates/      --> répertoire qui contient les modèles des pages HTML
        base.html     --> HTML de base
        index.html    --> page d'accueil
        login.html    --> page de login
        register.html --> page d'inscription
    __init__.py     --> exécute et définis les symboles que les paquets exposent à l'extérieur de l'application.
    forms.py        --> définis les formulaires (connexion, inscription ...)
    models.py       --> définis les modèles de la base de données (user, facture ...)
    routes.py       --> définis les routes vers les différentes pages (/, /index, /login, ...)

migrations/       --> répertoire qui contient les modifications faites dans la bd
venv/             --> répertoire contenant l'environnement virtuel

.flaskenv         --> permet de paramétrer la variable d'environnement FLASK_APP automatiquement
app.db            --> base de données
config.py         --> contient les variables de configuration, voir les [logs](History-log.md) pour plus d'information
sdf.py            --> défini l'instance de l'application Flask
.gitignore
```