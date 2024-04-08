from django.shortcuts import render
from django.http import JsonResponse
from .models import Book

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
    book = Book.objects.get(pk=book_id)
    if book is not None:
        book_info = {
            'name': book.name,
            'author_name': book.author_name,
            'category': book.category,
        }
        return JsonResponse(book_info)
    else:
        return JsonResponse({'error': 'Can not find the book'}, status=404)
    

    

    