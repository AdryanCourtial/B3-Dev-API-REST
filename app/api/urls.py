from django.urls import path 
from .views import get_users, create_user, user_detail, add_book, borrow_book, return_book,get_user_loans, get_book_details, list_books, get_user_return_history, update_book, delete_book

urlpatterns = [
    path('users/', get_users, name='get_users'),
    path('users/create/', create_user, name='create_user'),
    path('users/<int:pk>', user_detail, name='user_detail'),
    path('users/loans/<int:user_id>', get_user_loans, name='get_user_loans'),
    path('users/history/<int:user_id>', get_user_return_history, name='get_user_return_history'),



    path('books/add/', add_book, name='add_book'),
    path('books/<int:book_id>/', get_book_details, name='get_book_details'),
    path('books/', list_books, name='list_books'),
    path('books/<int:book_id>/update/', update_book, name='update_book'),
    path('books/<int:book_id>/delete/', delete_book, name='delete_book'),


    path('borrow/', borrow_book, name='borrow_book'),


    path('return/<int:pk>/', return_book, name='return_book'),

    
]
