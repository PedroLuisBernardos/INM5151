# INM5151 Système de Facturation (sdf)
---
## Documents
---
[OpsCon](https://docs.google.com/document/d/1gFm7OCDQM8OezZi54VzVFRqCNnuyvWAwm8ISOs8H8CQ/edit#)

[Sprint 1](https://docs.google.com/document/d/1YnsLE2BXZ-MREk3PWpu65Rmxpdcfev8nZcXn98PMk6g/edit#)

[Documentation Flask - on est rendus chapitre 5 - User logins](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins)

[PowerPoint presentation du projet](https://docs.google.com/presentation/d/1uslppIrlWSKgbWBgeMfVUH1LqGnuOxLnIFBX-3rYHqU/edit)

## [Les logs du projet](History-log.md)
---

## Comment utiliser l'application
---
Clôner ce dépot et accéder au repertoire principal
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

## Explication des repertoires et des fichiers
---
```
app/              --> repertoire qui heberge l'application
  templates/      --> repertoire qui contient les modeles des pages html
    base.html     --> html de base
    index.html    --> page d'accueil
    login.html    --> page de login
  __init__.py     --> execute et defini les symbols que les paquets exposent a l'exterieur de l'application
  forms.py        --> defini les formulaires (connexion, inscription, ...)
  models.py       --> defini les modeles de la base de donnees (user, facture, ...)
  routes.py       --> defini les routes vers les differentes pages (/, /index, /login, ...)

migrations/       --> repertoire qui contient les modifications faites dans la bd
venv/             --> repertoire contenant l'environnement virtuel

.flaskenv         --> permet de parametrer la variable d'environnement FLASK_APP automatiquement
.gitignore
app.db            --> base de données
config.py         --> contient les variables de configuration, voir les [logs](History-log.md) pour plus d'information
sdf.py            --> defini l'instance de l'application flask
```