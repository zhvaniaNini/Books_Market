from django.shortcuts import render
from django.http import JsonResponse
from market.models import Book
from django.shortcuts import get_object_or_404, render

# Create your views here.
def listed_books(request):
    books = Book.objects.values_list('id', 'name', 'author_name', 'price')
    serializer = BookSerializer(books, many=True)
    return JsonResponse(serializer.data, safe=False)

def book_information(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

    

    
