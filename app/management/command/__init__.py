from django.core.management.base import BaseCommand
from app.model import Category, Language

class Command(BaseCommand):
    help = 'Seed the database with initial data'

    def handle(self, *args, **kwargs):
        categories = ['Tech', 'Business', 'Health']
        languages = [
            {'name': 'French', 'code': 'fr'},
            {'name': 'English', 'code': 'en'},
            {'name': 'Spanish', 'code': 'es'}
        ]