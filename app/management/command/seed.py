from django.core.management.base import BaseCommand
from app.api.models import Categories, Languages, Civilites, Countries, Formats, States, Editors, Authors

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        categories = ['Tech', 'Business', 'Health']
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