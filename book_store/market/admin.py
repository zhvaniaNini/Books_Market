from django.contrib import admin
from .models import Book

# Register your models here.

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = Book.DisplayFields
    search_fields = Book.SearchableFields