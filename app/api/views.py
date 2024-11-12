from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Book, Loan, ReturnHistory
from .serializer import UserSerializer, BookSerializer, LoanSerializer
from django.utils import timezone
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.decorators import permission_classes

from django.urls import reverse




@api_view(['GET'])
@permission_classes([AllowAny])  # Désactiver l'authentification pour cette vue
def get_users(request):
    users = User.objects.all()
    serialazer = UserSerializer(users, many=True)
    return Response(serialazer.data)
 

@api_view(['POST'])
@permission_classes([AllowAny]) 
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@permission_classes([AllowAny]) 
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = UserSerializer(user)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


@api_view(['POST'])
def add_book(request):
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAdminUser])
def borrow_book(request):
    serializer = LoanSerializer(data=request.data)
    if serializer.is_valid():
        book = Book.objects.get(pk=request.data['book'])
        if book.available:
            book.available = False
            book.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Book is not available'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Teste
# @api_view(['GET','POST'])
# @permission_classes([IsAdminUser])
# def return_book(request, pk):
#     try:
#         loan = Loan.objects.get(pk=pk)
#         if loan.return_processed:
#             return Response({'error': 'Return already processed'}, status=status.HTTP_400_BAD_REQUEST)
        
#         loan.return_date = timezone.now()
#         loan.return_processed = True
        
#         # Mettre à jour la disponibilité du livre
#         loan.book.available = True
#         loan.book.save()

#         # Enregistrer l'historique du retour dans ReturnHistory
#         ReturnHistory.objects.create(user=loan.user, book=loan.book, return_date=loan.return_date)

#         # Supprimer l'entrée de Loan après enregistrement du retour
#         loan.delete()

#         return Response({'message': 'Book returned successfully'}, status=status.HTTP_200_OK)
    
#     except Loan.DoesNotExist:
#         return Response({'error': 'Loan not found'}, status=status.HTTP_404_NOT_FOUND)

    
@api_view(['GET','POST'])
@permission_classes([IsAdminUser])
def return_book(request, pk):
    try:
        loan = Loan.objects.get(pk=pk)
        if loan.return_processed:
            return Response({'error': 'Return already processed'}, status=status.HTTP_400_BAD_REQUEST)
        
        loan.return_date = timezone.now()
        loan.return_processed = True
        
        # Mettre à jour la disponibilité du livre
        loan.book.available = True
        loan.book.save()

        # Enregistrer l'historique du retour dans ReturnHistory
        ReturnHistory.objects.create(user=loan.user, book=loan.book, return_date=loan.return_date)

        # Supprimer l'entrée de Loan après enregistrement du retour
        loan.delete()

        return Response({'message': 'Book returned successfully'}, status=status.HTTP_200_OK)
    
    except Loan.DoesNotExist:
        return Response({'error': f'Loan with id {pk} not found'}, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
@permission_classes([AllowAny]) 
def get_user_loans(request, user_id):
    loans = Loan.objects.filter(user_id=user_id, return_processed=False)
    serializer = LoanSerializer(loans, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny]) 
def get_book_details(request, book_id):
    try:
        book = Book.objects.get(id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data)
    except Book.DoesNotExist:
        return Response({'error': 'Book not found'}, status=404)
    

@api_view(['GET'])
@permission_classes([AllowAny])
def list_books(request):
    books = Book.objects.all()
    data = []
    for book in books:
        book_info = {
            'title': book.title,
            'available': book.available,
            'detail_url': request.build_absolute_uri(reverse('get_book_details', args=[book.id]))
        }
        data.append(book_info)
    return Response(data)