from django.db import models

# Create your models here.
class Book(models.Model):
    title=models.CharField(max_length=200)
    no_of_pages=models.IntegerField()
    quantity=models.IntegerField()
    publish_date=models.DateField()

    def __str__(self):
        return book.title