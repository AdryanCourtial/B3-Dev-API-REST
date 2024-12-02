from rest_framework.response import Response
from api.models import User, Books, Loan, ReturnHistory, Languages, Civilites, Countries, Categories, States
from api.serializer import UserSerializer, BooksSerializer, LoanSerializer, LanguagesSerializer, CivilitesSerializer, CountriesSerializer, CategoriesSerializer, StatesSerializer

def filterBooks(arg, request):
    books = Books.objects.all()
    for filter in arg:
        print(filter)
        match filter:
            case "author":
                id = request.GET.getlist('filter_author')
                books= books.filter(author_id__in=id)
            case "category":
                id = request.GET.getlist('filter_category')
                books= books.filter(category_id__in=id)
            case "editor":
                id = request.GET.getlist('filter_editor')
                books= books.filter(editor_id__in=id)
            case "format":
                id = request.GET.getlist('filter_format')
                books= books.filter(format_id__in=id)
            case "language":
                id = request.GET.getlist('filter_language')
                books= books.filter(language_id__in=id)
            case _:
                return Response('Le filtre ne contient aucun argument valable')
        print(BooksSerializer(books, many=True).data)
    
    print(BooksSerializer(books, many=True).data)
    return BooksSerializer(books, many=True)