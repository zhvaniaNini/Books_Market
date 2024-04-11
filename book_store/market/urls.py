from django.urls import path
from .views import listed_books, book_information, home

urlpatterns = [
    path('books/', listed_books, name='list_books'),
    path('product1/<int:book_id>/', book_information, name='book1_description'),
    path('product2/<int:book_id>/', book_information, name='book2_description'),
    path('', home, name='books-home'),
]