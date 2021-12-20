# ![](app/static/favicon.ico) INM5151-30-E21 - Système de Facturation (sdf)

---

Cet API est un système de facturation fait pour notre cours [INM5151](https://etudier.uqam.ca/cours?sigle=INM5151) à l'UQAM lors de l'été 2021. On a dû apprendre à utiliser Python et Flask pour développer une application de notre choix. Nous avons suivi principalement [ce tutoriel](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) mais nous avons complété notre apprentissage avec des recherches sur Internet.

## Auteurs

---

* [Pedro Luis Bernardos](https://www.linkedin.com/in/pedro-luis-bernardos/)
* [Willy Tim](https://www.linkedin.com/in/willy-tim/)
* [Thuc-An Truong](https://www.linkedin.com/in/thuc-an-truong-915941148/)

## Comment utiliser l'application

---

### Installation

Cloner ce dépôt et accéder au répertoire principal

```bash
$ git clone https://github.com/ta-truong/inm5151-ete2021-projet
$ cd inm5151-ete2021-projet
```

Pour la suite, **vous avez deux possibilités**:

#### 1: Makefile

Faites uniquement la commande suivante:

```bash
$ make
```

#### 2: Au long

Installer les librairies nécessaires:

```bash
pip install -r requirements.txt --user
```

Lancer l'application

```bash
flask run
```

### Ouvrir l'application

---

Ouvrir un navigateur et aller à l'adresse: <http://127.0.0.1:5000/>

Une fois vous avez terminé faites `Ctrl+C` dans votre terminal.

### Mettre à jour la base de données

---

Pour mettre à jour les nouvelles versions de la bd (en changeant le fichier `modules.py`):

```bash
flask db migrate -m "message de modification ici"
flask db upgrade
```

En cas d'erreur:

```bash
flask db downgrade
```

### Ajouter une nouvelle langue

---

Pour ajouter une nouvelle langue, faire les commandes suivantes:

```bash
flask translate init <nom de la langue>
flask translate update
# aller modifier le fichier `app/translations/<nom de la langue>/messages.po`
flask translate compile
```

## Explication des répertoires et des fichiers

---

```
app/                            --> répertoire qui héberge l'application
    auth/                       --> répertoire qui contient les routes en lien avec l'authentication
        ...
    entrees/                    --> répertoire qui contient les routes en lien avec les entrées: profils, factures, contacts et comptes
        ...
    errors/                     --> répertoire qui contient les routes des erreurs
        ...
    static/                     --> répertoire qui contient les fichiers statiques de l'application: css, js et images
        ...
    templates/                  --> répertoire qui contient les modèles des pages HTML
        auth/                   --> répertoire qui contient les modèles des pages en lien avec l'authentication
            ...
        email/                  --> répertoire qui contient les modèles des pages en lien avec les envois par email
            ...
        entrees/                --> répertoire qui contient les modèles des pages en lien avec les entrées
            ...
        errors/                 --> répertoire qui contient les modèles des pages en lien avec les erreurs
        user/                   --> répertoire qui contient les modèles des pages en lien avec l'utilisateur courrant
        all.html                --> page cachée, qui contient tous les utilisateurs et toutes les factures
        base.html               --> HTML de base
        wellcome.html           --> page d'accueil des invités
    translations/               --> répertoire qui contient les traductions
        en/                     --> répertoire qui contient les traductions en anglais
        es/                     --> répertoire qui contient les traductions en espagnol
    __init__.py             --> exécute et définit les symboles que les paquets exposent à l'extérieur de l'application
    cli.py                  --> défini des commandes flask traduction plus simples pour la gestion des 
    models.py               --> défini les modèles de la base de données (user, facture ...)
    routes.py               --> défini les routes vers les pages générales
    user/                   --> répertoire qui contient les routes en lien avec l'utilisateur courrant
        ...

migrations/                 --> répertoire qui contient les modifications faites dans la bd

.flaskenv                   --> permet de paramétrer la variable d'environnement FLASK_APP automatiquement
.gitignore                  --> permet de ne pas ajouter au dépôt certains fichiers
app.db                      --> base de données
babel.cfg                   --> contient la configuration de la traduction
config.py                   --> contient les variables de configuration, voir les [logs](logs.md) pour plus d'information
Makefile                    --> permet de rouler l'application en une seule commande
requirements.txt            --> liste de librairies à installer
sdf.py                      --> défini l'instance de l'application Flask
```

## Documents de référence

---

[Documentation Flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

[Les logs du projet](logs.md)
