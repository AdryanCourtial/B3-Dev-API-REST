from rest_framework import serializers
from .models import User, Books, Loan, Languages, Civilites, Countries, Categories, States

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields = '__all__'
    
class LanguagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Languages
        fields = '__all__'

class CivilitesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Civilites
        fields = '__all__'

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'
    
class StatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = '__all__'

        