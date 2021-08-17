# INM5151-30-E21 - Système de Facturation (sdf)

---

Cet API est un système de facturation fait pour notre cours [INM5151](https://etudier.uqam.ca/cours?sigle=INM5151) à l'UQAM lors de l'été 2021.

## Auteurs

---

* [Pedro Luis Bernardos](https://github.com/PedroLuisBernardos)
* [Willy Tim](https://github.com/WillyTim)
* [Thuc-An Truong](https://github.com/ta-truong)

## TODO - Tâches non-complétées

---

* [ ] Améliorer le module **Facture**. Faire les modifications nécessaires dans les routes et les pages html concernées.
  * [ ] Ajouter dans le *drop-down* de `comptes de revenus/dépenses` et de `contacts` une option pour en créer un.
  * [ ] Créer une page nommée `modele_facture.html` et l'ajouter dans la barre de navigation. Il y aura un formulaire qui nous permet d'ajouter des modèles de facture. Ces modèles seront visibles dans l'ajout (uniquement l'ajout) de factures sous forme de *drop-down*. On doit aussi pouvoir les créer directement dans ce *drop-down* (l'option est à la toute fin).
* [ ] Pourquoi **loyer** ne s'affiche pas dans aucune langue dans la barre de navigation ?
* [ ] Traduire tout ce qui est en anglais en français: les erreurs dans les formulaires, les hover dans les formulaires, etc.
* [ ] Faire la gestion de la barre de recherche. [Voir comment faire ici](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xvi-full-text-search).
* [ ] Faire la gestion des notifications. [Voir comment faire ici](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xxi-user-notifications).
* [ ] Gérer l'exportation de factures en format PDF.
* [ ] Modifier la structure de l'application
* [ ] Gérer l'envoi des factures par email (exportées en PDF).
* [ ] Gérer le filtrage de factures.
* [ ] Gérer le calcul des montants des factures sélectionnées.
* [ ] Améliorer le CSS pour rendre l'application plus belle.
* [ ] Ajouter des `try/except` dans **toutes** les routes du fichier `routes.py`.
* [ ] Améliorer la structure de l'application. [Voir comment faire ici](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure).
* [ ] *Bonus: pouvoir cliquer dans les id des utilisateurs dans la page `/all` et en le faisant faire apparaître les Factures pour cet Utilisateur.*

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
pip install -r requirements.txt --user
```

Rouler l'application

```bash
flask run
```

### Ouvrir l'application

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

## Autres commandes

---

### Vider la base de données manuellement

---

Pour voir tous les utilisateurs et toutes les factures voir <http://127.0.0.1:5000/all>.

Pour vider la base de données vous pouvez faire la suite de commandes suivante:

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
>>> contacts = Contact.query.all()
>>> for c in users:
...     db.session.delete(c)
...
>>> comptes = Compte.query.all()
>>> for c in factures:
...     db.session.delete(c)
...
>>> profilsEntreprise = CompanyProfil.query.all()
>>> for p in users:
...     db.session.delete(p)
...
>>> db.session.commit()
```

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

Pour ajouter une nouvelle langue faire les commandes suivantes:

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
    errors/                     --> répertoire qui contient les routes des erreurs
        __init__.py             --> défini les blueprint des erreurs
        handlers.py             --> défini les routes des erreurs
    static/                     --> répertoire qui contient les fichiers statiques de l'application
        css/                    --> répertoire qui contient le CSS de l'application
            style.css           --> CSS de l'application (en plus de Bootstrap)
        js/                     --> répertoire qui contient le JS de l'application
            script.js           --> JS de l'application (en plus de Bootstrap)
        favicon.ico             --> favicon
    templates/                  --> répertoire qui contient les modèles des pages HTML
        errors/                 --> répertoire qui gère les pages en lien avec les erreurs
            404.html            --> page qui gère l'erreur 404
            500.html            --> page qui gère l'erreur 500
            error.html          --> page d'erreurs généraux
        update/                 --> répertoire qui contient les pages de modification
            edit_profile.html   --> page de modification du profil de l'utilisateur
            register_com...     --> page qui gère l'ajout d'un profil d'entreprise
            reset_pass...       --> page de demande de la réinitialisaiton du mot de passe
            reset_password.html --> page de réinitialisation du mot de passe
            update_company...   --> page qui gère la modification du profil d'entreprise
            update_compte.html  --> page qui gère la modification du compte
            update_contact.html --> page qui gère la modification du contact
            update_facture.html --> page qui gère la modification de la facture
        all.html                --> page cachée, qui contient tous les utilisateurs et toutes les factures
        base.html               --> HTML de base
        bill.html               --> page de factures
        comptes.html            --> page des comptes
        contacts.html           --> page des contacts
        index.html              --> page d'accueil des utilisateurs où on voit les factures
        login.html              --> page de login
        register.html           --> page d'inscription
        user.html               --> page du profil de l'utilisateur
        update_facture.html     --> page de modification de la facture sélectionnée
        wellcome.html           --> page d'accueil des invités
    translations/               --> répertoire qui contient les traductions
        en/                     --> répertoire qui contient les traductions en anglais
        es/                     --> répertoire qui contient les traductions en espagnol
    __init__.py             --> exécute et définit les symboles que les paquets exposent à l'extérieur de l'application
    cli.py                  --> défini des commandes flask traduction plus simples pour la gestion des 
    errors.py               --> défini les erreurs possibles
    forms.py                --> défini les formulaires (connexion, inscription ...)
    models.py               --> défini les modèles de la base de données (user, facture ...)
    routes.py               --> défini les routes vers les différentes pages (/, /index, /login, ...)

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

## Documents

---

[Documentation Flask](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)

[Les logs du projet](logs.md)
