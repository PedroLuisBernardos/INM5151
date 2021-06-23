# INM5151 Système de Facturation (sdf)
---

## TODO
---
On est rendus [ici](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-viii-followers) - chapitre 8 - Followers. J ne sais pas si c'est utile, mais il faudrait voir s'il y a de l'information intéressante.

## Documents
---
[OpsCon](https://docs.google.com/document/d/1gFm7OCDQM8OezZi54VzVFRqCNnuyvWAwm8ISOs8H8CQ/edit#)

[PowerPoint OpsCon](https://docs.google.com/presentation/d/1uslppIrlWSKgbWBgeMfVUH1LqGnuOxLnIFBX-3rYHqU/edit)

[Sprint 1](https://docs.google.com/document/d/1YnsLE2BXZ-MREk3PWpu65Rmxpdcfev8nZcXn98PMk6g/edit#)

[Documentation Flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

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

Deux utilisateurs de base sont déjà présents:
```
user: admin
email: admin@admin.com
pass: admin
```

```
user: admin2
email: admin2@admin.com
pass: admin2
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
        index.html          --> page d'accueil des utilisateurs
        wellcome.html       --> page d'accueil des invités
        login.html          --> page de login
        register.html       --> page d'inscription
        user.html           --> page du profil de l'utilisateur
        edit_profile.html   --> page de modification du profil de l'utilisateur
        _factures.html      --> page d'affichage des factures (le modèle de base)
        404.html            --> page d'erreur 404
        500.html            --> page d'erreur 500
    __init__.py             --> exécute et définit les symboles que les paquets exposent à l'extérieur de l'application.
    forms.py                --> définis les formulaires (connexion, inscription ...)
    models.py               --> définis les modèles de la base de données (user, facture ...)
    routes.py               --> définis les routes vers les différentes pages (/, /index, /login, ...)
    errors.py               --> défini les erreurs possibles

migrations/                 --> répertoire qui contient les modifications faites dans la bd
venv/                       --> répertoire contenant l'environnement virtuel

.flaskenv                   --> permet de paramétrer la variable d'environnement FLASK_APP automatiquement
app.db                      --> base de données
config.py                   --> contient les variables de configuration, voir les [logs](History-log.md) pour plus d'information
sdf.py                      --> défini l'instance de l'application Flask
.gitignore
```