from django.core.management.base import BaseCommand
from app.api.models import Categories, Languages, Civilites, Countries, Formats, States, Editors, Authors

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        categories = ['Roman', 'Science-Fiction', 'Fantasy', 'Thriller', 'Romance', 'Aventure', 'Drame', 'Horreur', 'Contes et Légendes', 'Dystopie', 'Historique', 'Biographie', 'Essaie', 'Mémoire', 'Science', 'Politique', 'Economie', 'BD', 'Manga']
        languages = [
            {'name': 'French'},
            {'name': 'English'},
            {'name': 'Spanish'},
            {'name': 'Deutch'},
            {'name': 'Italiano'},
            {'name': '中国人'},
            {'name': '한국'},
            {'name': '북한'},
            {'name': 'Русский'},
        ]
        civilites = ['Monsieur', 'Madame', 'Autre']