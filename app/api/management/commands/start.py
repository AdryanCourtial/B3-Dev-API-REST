from django.core.management.commands.runserver import Command as RunserverCommand

class Command(RunserverCommand):
    def inner_run(self, *args, **options):

        print(f"Le serveur est disponible à l'adresse : http://{self.addr}:{self.port}/swagger")
        print("Appuyez sur Ctrl+C pour arrêter.")
        
        super().inner_run(*args, **options)