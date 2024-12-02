from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Modèle utilisateur simplifié
class User(models.Model):
    username = models.CharField(max_length=50, default='default_username')

    def __str__(self):
        return self.username



class Countries(models.Model):
    name = models.CharField(max_length=30)


class Civilites(models.Model):
    name = models.CharField(max_length=30)

class Authors(models.Model):
    name = models.CharField(max_length=30)
    firstname = models.CharField(max_length=30)
    is_alive = models.BooleanField(default=True)
    birthday = models.TextField()
    civilite = models.ForeignKey(Civilites, on_delete=models.CASCADE)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)

class Editors(models.Model):
    name = models.CharField(max_length=30)
    adress = models.CharField(max_length=100)
    web_site = models.CharField(max_length=255)
    logo = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)


class Languages(models.Model): 
    name = models.CharField(max_length=50)


class Categories(models.Model):
    name = models.CharField(max_length=30)

class States(models.Model):
    name = models.CharField(max_length=30)

class Formats(models.Model):
    name = models.CharField(max_length=40)

class Books(models.Model):
    name = models.CharField(max_length=40)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    year_of_publication = models.TextField()
    isbn = models.IntegerField()
    editor = models.ForeignKey(Editors, on_delete=models.CASCADE)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    summary = models.TextField()
    price = models.CharField(max_length=15)
    picture = models.CharField(max_length=255)
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    format = models.ForeignKey(Formats, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    available = models.BooleanField(default=True)


# Modèle prêt simplifié
class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Books, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)


    def __str__(self):
        return f"{self.user} borrowed {self.book}"


@receiver(post_delete, sender=Loan)
def update_book_on_loan_delete(sender, instance, **kwargs):
    book = instance.book
    book.available = True
    book.save()


