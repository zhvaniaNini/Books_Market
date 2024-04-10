from django.db import models
from django.core.serializers import serialize

# Create your models here.

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    page_count = models.IntegerField()
    category = models.CharField(max_length=200)
    author_name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='book_image/', null=True)
    discription = models.TextField()

    def __str__(self):
        return self.name
        


    
