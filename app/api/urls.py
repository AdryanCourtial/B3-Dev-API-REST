from django.urls import path 
from .views import get_users, create_user, user_detail, add_book, borrow_book, return_book,get_user_loans, get_book_details, list_books, get_languages, get_civilites, get_countries, get_categories, get_states

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:pk>', user_detail, name='user_detail'),
    path('users/<int:user_id>/loans/', get_user_loans, name='get_user_loans'),

    path('books/add/', add_book, name='add_book'),
    path('books/', list_books, name='list_books'),
    path('books/<int:book_id>/', get_book_details, name='get_book_details'),

    path('languages/', get_languages, name='get_languages'),

    path('civilites/', get_civilites, name='get_languages'),

    path('countries/', get_countries, name='get_countries'),

    path('categories/', get_categories, name='get_categories'),

    path('states/', get_states, name='get_states'),

    path('borrow/', borrow_book, name='borrow_book'),

    path('return/<int:pk>/', return_book, name='return_book'),


]
