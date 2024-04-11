from django.shortcuts import render
from django.http import JsonResponse
from market.models import Book
from django.shortcuts import get_object_or_404, render

# Create your views here.
def listed_books(request):
    books = Book.objects.all()
    return_books = []
    for book in books:
        return_books.append({
            'name': book.name,
            'page_count': book.page_count,
            'category': book.category,
            'author_name': book.author_name,
            'price': book.price,
            'discription': book.discription,
        })
    print(return_books)
    return JsonResponse({'books': return_books})

def book_information(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'book_detail.html', {'book': book})

    

    
