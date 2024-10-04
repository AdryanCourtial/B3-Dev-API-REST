from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import Book, Loan, ReturnHistory

admin.site.register(Book)
admin.site.register(Loan)
admin.site.register(ReturnHistory)