from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver


# Modèle utilisateur simplifié
class User(models.Model):
    username = models.CharField(max_length=50, default='default_username')

    def __str__(self):
        return self.username

# Modèle livre simplifié
class Book(models.Model):
    title = models.CharField(max_length=100)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.title
    
# Modèle prêt simplifié
class Loan(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    loan_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    return_processed = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.user} borrowed {self.book}"



@receiver(post_delete, sender=Loan)
def update_book_on_loan_delete(sender, instance, **kwargs):
    book = instance.book
    book.available = True
    book.save()


class ReturnHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    return_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.username} returned {self.book.title} on {self.return_date}"
