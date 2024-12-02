# B3-Dev-API-REST

**B3-Dev-API-REST** est une API RESTful développée avec **Django** et **Django Rest Framework**. Elle permet de gérer une bibliothèque en ligne, en offrant des fonctionnalités pour gérer les utilisateurs, les livres, les emprunts, et les retours de livres.

## Description du projet

Ce projet a pour but de créer une API permettant de gérer une bibliothèque avec les fonctionnalités suivantes :

- **Gestion des utilisateurs** : Création, mise à jour, suppression et récupération des informations des utilisateurs.
- **Gestion des livres** : Ajout, mise à jour, suppression et consultation des livres disponibles dans la bibliothèque.
- **Emprunts de livres** : Permet aux utilisateurs d'emprunter des livres, avec un suivi des dates d'emprunt et de retour.
- **Historique des retours** : Permet aux utilisateurs de voir l'historique de leurs retours de livres.

### Objectifs

- Fournir une interface API simple pour gérer les utilisateurs et les livres dans une bibliothèque.
- Suivre les emprunts et retours de livres.
- Offrir une interface d'administration pour faciliter la gestion des utilisateurs et des livres.

## Technologies utilisées

- **Django** : Framework Python pour le développement web.
- **Django Rest Framework (DRF)** : Bibliothèque Django pour la création d'APIs RESTful.
- **SQLite** : Base de données par défaut pour le stockage des données.
- **Python** : Langage de programmation utilisé.

## Fonctionnalités principales

- Création, modification et suppression des utilisateurs et des livres.
- Suivi des emprunts et retours de livres.
- Visualisation de l'historique des retours pour chaque utilisateur.

## Installation

1. Clonez ce repository :

```
git clone https://github.com/AdryanCourtial/B3-Dev-API-REST
cd B3-Dev-API-REST
```

Install :

Commande d'install:

```
pip install --upgrade setuptools

```

```

pip install drf-yasg

```

```

pip install djangorestframework

```

Appliquez les migrations pour configurer la base de données :

```
cd app
python manage.py migrate
```

Migration des Seeders

Si vous avez des données à insérer dans la base (seeders), vous pouvez utiliser cette commande :

```
python manage.py seed
```

Créez un super utilisateur pour accéder à l'interface d'administration :

```
python manage.py createsuperuser
```

Lancez le serveur local :

```
python manage.py start
```

base_url : http://127.0.0.1:8000/api
swagger_url : http://127.0.0.1:8000/swagger