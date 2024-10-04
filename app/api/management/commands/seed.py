from django.core.management.base import BaseCommand
from api.models import Categories, Languages, Civilites, Countries, Formats, States, Editors, Authors, Books
from datetime import date

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
                "birthday": '1802-02-26',
                "civilite_id": 1,  # Exemple de civilité (Mr/Mrs/etc.)
                "country_id": 2    # France
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
                "country_id": 2  # Royaume-Uni
            },
            {
                "name": "Shinchosha",
                "adress": "71 Yotsuya, Shinjuku, Tokyo, Japan",
                "web_site": "https://www.shinchosha.co.jp",
                "logo": "https://www.shinchosha.co.jp/logo.png",
                "email": "contact@shinchosha.co.jp",
                "country_id": 3   # Japon
            },
            {
                "name": "Secker & Warburg",
                "adress": "20 Vauxhall Bridge Road, London, UK",
                "web_site": "https://www.penguin.co.uk",
                "logo": "https://www.penguin.co.uk/logo.png",
                "email": "info@penguin.co.uk",
                "country_id": 2   # Royaume-Uni
            }
        ]

        books = [
            {
                "name": "Les Misérables",
                "author_id": 1,  # Victor Hugo
                "year_of_publication": "1862-01-01",
                "isbn": 9781234567890,
                "editor_id": 1,  # Gallimard
                "language_id": 1,  # Français
                "category_id": 1,  # Roman
                "summary": "Un chef-d'œuvre de la littérature française, explorant la justice et la rédemption.",
                "price": "19.99",
                "picture": "https://example.com/les-miserables.jpg",
                "state_id": 1,  # Neuf
                "format_id": 1,  # Broché
                "quantity": 100
            },
            {
                "name": "Harry Potter and the Philosopher's Stone",
                "author_id": 2,  # J.K. Rowling
                "year_of_publication": "1997-06-26",
                "isbn": 9780747532699,
                "editor_id": 2,  # Bloomsbury
                "language_id": 2,  # Anglais
                "category_id": 2,  # Fantaisie
                "summary": "Le premier roman de la série Harry Potter.",
                "price": "25.99",
                "picture": "https://example.com/harry-potter-1.jpg",
                "state_id": 1,
                "format_id": 1,
                "quantity": 200
            },
            {
                "name": "1984",
                "author_id": 3,  # George Orwell
                "year_of_publication": "1949-06-08",
                "isbn": 9780451524935,
                "editor_id": 4,  # Secker & Warburg
                "language_id": 2,  # Anglais
                "category_id": 3,  # Dystopie
                "summary": "Un roman dystopique explorant la surveillance et le totalitarisme.",
                "price": "14.99",
                "picture": "https://example.com/1984.jpg",
                "state_id": 1,
                "format_id": 1,
                "quantity": 150
            },
            {
                "name": "Kafka on the Shore",
                "author_id": 4,  # Haruki Murakami
                "year_of_publication": "2002-09-12",
                "isbn": 9781400079278,
                "editor_id": 3,  # Shinchosha
                "language_id": 3,  # Japonais
                "category_id": 4,  # Fiction contemporaine
                "summary": "Un roman mystérieux et onirique de Haruki Murakami.",
                "price": "22.50",
                "picture": "https://example.com/kafka-on-the-shore.jpg",
                "state_id": 1,
                "format_id": 1,
                "quantity": 120
            }
        ]        

        for category_name in categories:
                category, created = Categories.objects.get_or_create(name=category_name)
                if created:
                    self.stdout.write(self.style.SUCCESS(f'Category "{category_name}" created'))
                else:
                    self.stdout.write(self.style.WARNING(f'Category "{category_name}" already exists'))
        

        for language_name in languages:
            language, created = Languages.objects.get_or_create(name=language_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Language "{language_name}" created'))
            else:
                self.stdout.write(self.style.WARNING(f'Language "{language_name}" already exists'))


        for civilites_name in civilites:
            civilite, created = Civilites.objects.get_or_create(name=civilites_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Civilites "{civilites_name}" created'))
            else:
                self.stdout.write(self.style.WARNING(f'Civilites "{civilites_name}" already exists'))


        for format_name in formats:
            format, created = Formats.objects.get_or_create(name=format_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Format "{format_name}" created'))
            else:
                self.stdout.write(self.style.WARNING(f'Format "{format_name}" already exists'))


        for state_name in states:
            state, created = States.objects.get_or_create(name=state_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'States "{state_name}" created'))
            else:
                self.stdout.write(self.style.WARNING(f'States "{state_name}" already exists'))

            
        for country_name in countries:
            country, created = Countries.objects.get_or_create(name=country_name)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Country "{country_name}" created'))
            else:
                self.stdout.write(self.style.WARNING(f'Country "{country_name}" already exists'))


        for author_name in authors:
            author, created = Authors.objects.get_or_create(
                name=author_name["name"], 
                firstname=author_name["firstname"], 
                is_alive=author_name["is_alive"], 
                birthday=author_name["birthday"], 
                civilite_id=author_name["civilite_id"], 
                country_id=author_name["country_id"] 
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Author "{author_name}" created'))
            else:
                self.stdout.write(self.style.WARNING(f'Author "{author_name}" already exists'))
            
        
        for editor_name in editors:
            editor, created = Editors.objects.get_or_create(
                name=editor_name["name"],
                adress=editor_name["adress"],
                web_site=editor_name["web_site"],
                logo=editor_name["logo"],
                email=editor_name["email"],
                country_id=editor_name["country_id"]                                    )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Editor "{editor_name}" created'))
            else:
                self.stdout.write(self.style.WARNING(f'Editor "{editor_name}" already exists'))


        for book_name in books:
            book, created = Books.objects.get_or_create(
                name=book_name["name"],
                isbn=book_name["isbn"],
                summary=book_name["summary"],
                price=book_name["price"],
                picture=book_name["picture"],
                quantity=book_name["quantity"],
                author_id=book_name["author_id"],
                category_id=book_name["category_id"],
                editor_id=book_name["editor_id"],
                format_id=book_name["format_id"],
                language_id=book_name['language_id'],
                state_id=book_name["state_id"],
                year_of_publication=book_name["year_of_publication"]
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'Book "{book_name}" created'))
            else:
                self.stdout.write(self.style.WARNING(f'Book "{book_name}" already exists'))