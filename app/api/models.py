from django.db import models

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
    isbn = models.IntegerField(max_length=13)
    editor = models.ForeignKey(Editors, on_delete=models.CASCADE)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    summary = models.TextField()
    price = models.CharField(max_length=15)
    picture = models.CharField(max_length=255)
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    format = models.ForeignKey(Formats, on_delete=models.CASCADE)
    quantity = models.IntegerField()
