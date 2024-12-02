from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User, Loan, Books
from .serializer import UserSerializer, LoanSerializer, BooksSerializer
from django.utils import timezone
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.decorators import permission_classes

from django.urls import reverse


############################################################
# USER 
############################################################


@api_view(['GET'])
@permission_classes([AllowAny])  
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


@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_loans(request, user_id):
    loans = Loan.objects.filter(user_id=user_id, return_date=None)
    serializer = LoanSerializer(loans, many=True)
    loan_data = serializer.data

    for loan in loan_data:
        loan_id = loan['id']
        loan['return_link'] = request.build_absolute_uri(reverse('return_book', args=[loan_id]))
        del loan['id']
        del loan['return_date']

    # Créer un lien pour l'historique des prêts
    history_link = request.build_absolute_uri(reverse('get_user_return_history', args=[user_id]))

    # Créer la réponse structurée
    response_data = {
        "loans": loan_data,
        "history_link": history_link
    }

    return Response(response_data)



@api_view(['GET'])
@permission_classes([AllowAny])
def get_user_return_history(request, user_id):
    return_history = Loan.objects.filter(user_id=user_id).exclude(return_date=None)
    serializer = LoanSerializer(return_history, many=True)

    return Response(serializer.data)

############################################################
# BOOK 
############################################################


@api_view(['POST'])
def add_book(request):
    serializer = BooksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([AllowAny])
def list_books(request):
    books = Books.objects.all()
    data = []
    for book in books:
        book_info = {
            'name': book.name,
            'available': book.available,
            'detail_url': request.build_absolute_uri(reverse('get_book_details', args=[book.id]))
        }
        data.append(book_info)
    return Response(data)



@api_view(['GET'])
@permission_classes([AllowAny]) 
def get_book_details(request, book_id):
    try:
        book = Books.objects.get(id=book_id)
        serializer = BooksSerializer(book)
        return Response(serializer.data)
    except Books.DoesNotExist:
        return Response({'error': 'Book not found'}, status=404)
    

@api_view(['PUT'])
@permission_classes([IsAdminUser])
def update_book(request, book_id):
    try:
        book = Books.objects.get(pk=book_id)
    except Books.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = BooksSerializer(book, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def delete_book(request, book_id):
    try:
        book = Books.objects.get(pk=book_id)
        book.delete()
        return Response({'message': 'Book deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Books.DoesNotExist:
        return Response({'error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)




############################################################
# BORROW 
############################################################

@api_view(['POST'])
@permission_classes([IsAdminUser])
def borrow_book(request):
    serializer = LoanSerializer(data=request.data)
    if serializer.is_valid():
        book = Books.objects.get(pk=request.data['book'])
        if book.available:
            book.available = False
            book.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': 'Book is not available'}, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



############################################################
# RETURN 
############################################################


@api_view(['GET','POST'])
@permission_classes([IsAdminUser])
def return_book(request, pk):
    try:
        loan = Loan.objects.get(pk=pk)
        if loan.return_date:
            return Response({'error': 'Return already processed'}, status=status.HTTP_400_BAD_REQUEST)
        
        loan.return_date = timezone.now()
            
        # Mettre à jour la disponibilité du livre
        loan.book.available = True           
        loan.book.save()
        loan.save()

        return Response({'message': 'Book returned successfully'}, status=status.HTTP_200_OK)

    except Loan.DoesNotExist:
        return Response({'error': f'Loan with id {pk} not found'}, status=status.HTTP_404_NOT_FOUND)


