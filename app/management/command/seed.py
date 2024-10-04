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
        formats = ['Ebook', 'Audio', 'Physique']
        states = ['En Stock', 'Epuisé', 'Reviend dans pas longtemps']
        countries = [
            "France",
            "Royaume-Uni",
            "Japan",
            "Brazil",
            "Australia",
            "Germany",
            "India",
            "South Africa",
            "United States",
            "China",
            "Mexico",
            "Italy",
            "Spain",
            "Russia",
            "Argentina"
        ]

        authors = [
            {
                "name": "Hugo",
                "firstname": "Victor",
                "is_alive": False,
                "birthday": "1802-02-26",
                "civilite_id": 1,  # Exemple de civilité (Mr/Mrs/etc.)
                "country_id": 1    # France
            },
            {
                "name": "Rowling",
                "firstname": "J.K.",
                "is_alive": True,
                "birthday": "1965-07-31",
                "civilite_id": 1,
                "country_id": 2    # Royaume-Uni
            },
            {
                "name": "Orwell",
                "firstname": "George",
                "is_alive": False,
                "birthday": "1903-06-25",
                "civilite_id": 1,
                "country_id": 2    # Royaume-Uni
            },
            {
                "name": "Murakami",
                "firstname": "Haruki",
                "is_alive": True,
                "birthday": "1949-01-12",
                "civilite_id": 1,
                "country_id": 3    # Japon
            },
            {
                "name": "Camus",
                "firstname": "Albert",
                "is_alive": False,
                "birthday": "1913-11-07",
                "civilite_id": 1,
                "country_id": 1    # France
            }
        ]

        editors = [
            {
                "name": "Gallimard",
                "adress": "5 Rue Sébastien Bottin, Paris, France",
                "web_site": "https://www.gallimard.fr",
                "logo": "https://www.gallimard.fr/logo.png",
                "email": "contact@gallimard.fr",
                "country_id": 1    # France
            },
            {
                "name": "Bloomsbury",
                "adress": "50 Bedford Square, London, UK",
                "web_site": "https://www.bloomsbury.com",
                "logo": "https://www.bloomsbury.com/logo.png",
                "email": "info@bloomsbury.com",
                "country_id": 2    # Royaume-Uni
            },
            {
                "name": "Shinchosha",
                "adress": "71 Yotsuya, Shinjuku, Tokyo, Japan",
                "web_site": "https://www.shinchosha.co.jp",
                "logo": "https://www.shinchosha.co.jp/logo.png",
                "email": "contact@shinchosha.co.jp",
                "country_id": 3    # Japon
            },
            {
                "name": "Secker & Warburg",
                "adress": "20 Vauxhall Bridge Road, London, UK",
                "web_site": "https://www.penguin.co.uk",
                "logo": "https://www.penguin.co.uk/logo.png",
                "email": "info@penguin.co.uk",
                "country_id": 2    # Royaume-Uni
            }
        ]

        
        

        