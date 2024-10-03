# API de Gestion de Bibliothèque Personnelle

## Vue d'ensemble du projet

Ce projet est une API permettant de gérer une bibliothèque personnelle. Il permet aux utilisateurs d'ajouter, mettre à jour, consulter et supprimer des livres de leur collection, de suivre leur progression de lecture, de définir des objectifs de lecture et de générer des rapports sur leurs habitudes de lecture.

## Fonctionnalités

- **Gestion des livres** : Ajouter, mettre à jour, supprimer et consulter les livres dans la collection.
- **Suivi de la lecture** : Suivre l'état de lecture (à lire, en cours, terminé).
- **Catégorisation** : Organiser les livres en genres ou catégories.
- **Rapports** : Générer des rapports hebdomadaires ou mensuels sur les habitudes de lecture.
- **Recherche** : Rechercher des livres par titre, auteur ou genre.
- **Authentification des utilisateurs** : Bibliothèques spécifiques aux utilisateurs avec connexion sécurisée (basée sur JWT).
- **Notifications** : Recevoir des alertes pour les objectifs de lecture ou les livres non terminés.

## Technologies utilisées

- **Backend** : Django, Django REST Framework
- **Base de données** : PostgreSQL (vous pouvez utiliser SQLite pour le développement)
- **Authentification** : JWT (JSON Web Token) pour des sessions utilisateurs sécurisées
- **Frontend** : Cette API est conçue pour fonctionner avec un frontend de votre choix (par exemple, React, Vue.js)
- **Déploiement** : AWS (avec des services tels que Lambda et API Gateway pour un déploiement serverless) – optionnel

## Pré-requis

- Python 3.8+
- Django 4.x
- Django REST Framework
- PostgreSQL (ou SQLite pour le développement local)
- djangorestframework-simplejwt (pour l'authentification JWT)
- psycopg2 (pour la connexion à PostgreSQL)

## Installation et Configuration

### 1. Cloner le repository

```bash
git clone https://github.com/yourusername/library-management-api.git
cd library-management-api
```

### 2. Configurer un environnement virtuel

```bash
python3 -m venv venv
source venv/bin/activate  # Sur Windows : venv\Scripts\activate
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Configurer la base de données

- Si vous utilisez **PostgreSQL**, créez une base de données pour le projet.
- Mettez à jour la configuration `DATABASES` dans `settings.py` avec vos identifiants PostgreSQL.

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'nom_de_votre_bd',
        'USER': 'votre_utilisateur_bd',
        'PASSWORD': 'votre_mot_de_passe_bd',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Appliquer les migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Créer un super utilisateur

```bash
python manage.py createsuperuser
```

### 7. Lancer le serveur de développement

```bash
python manage.py runserver
```

### 8. Tester l'API

Vous pouvez tester l'API à l'aide d'outils comme **Postman** ou **cURL**. L'API devrait être accessible à l'adresse suivante :

```
http://localhost:8000/api/
```

## Points d'entrée API

Voici une liste des points d'entrée disponibles pour l'API :

- **/api/books/** (GET, POST) : Lister tous les livres, ajouter un nouveau livre
- **/api/books/{id}** (GET, PUT, DELETE) : Obtenir, mettre à jour ou supprimer un livre spécifique
- **/api/books/{id}/progress/** (PATCH) : Mettre à jour l'état de lecture (à lire, en cours, terminé)
- **/api/books/search/** (GET) : Rechercher des livres par titre, auteur ou genre
- **/api/reports/** (GET) : Générer des rapports de lecture (hebdomadaires/mensuels)
- **/api/auth/login/** (POST) : Connexion utilisateur (basé sur JWT)
- **/api/auth/register/** (POST) : Inscription utilisateur

## Modèles

Voici un aperçu des modèles utilisés dans ce projet :

### Livre

- `title`: CharField (obligatoire)
- `author`: CharField (obligatoire)
- `description`: TextField (optionnel)
- `genre`: CharField (optionnel)
- `status`: CharField (choix : "à lire", "en cours", "terminé")
- `created_at`: DateTimeField (auto_now_add=True)

### Utilisateur (modèle Django par défaut)

- Modèle utilisateur Django par défaut avec authentification JWT pour des bibliothèques utilisateur spécifiques sécurisées.

## Utilisation

1. **Ajouter un livre** :

   ```bash
   POST /api/books/
   {
       "title": "Le Grand Gatsby",
       "author": "F. Scott Fitzgerald",
       "genre": "Fiction",
       "status": "à lire"
   }
   ```

2. **Mettre à jour la progression de lecture** :

   ```bash
   PATCH /api/books/{id}/progress/
   {
       "status": "en cours"
   }
   ```

3. **Obtenir un rapport mensuel** :
   ```bash
   GET /api/reports/?period=monthly
   ```

## Déploiement

### 1. Configurer un environnement AWS

Vous pouvez utiliser des services comme **Elastic Beanstalk** ou **Lambda** et **API Gateway** pour un déploiement serverless.

### 2. Collecter les fichiers statiques

Avant le déploiement, collectez les fichiers statiques pour les utiliser en production.

```bash
python manage.py collectstatic
```

### 3. Déployer

Déployez le projet en utilisant votre méthode préférée (AWS, Heroku, etc.).

## Contribution

N'hésitez pas à forker le repository, à soumettre des pull requests et à contribuer au projet. Toutes les contributions sont les bienvenues !
