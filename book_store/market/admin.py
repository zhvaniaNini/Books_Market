from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'page_count', 'category', 'author_name', 'price']
    search_fields = ['name', 'author_name']
