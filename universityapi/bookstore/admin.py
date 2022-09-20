from django.contrib import admin

# Register your models here.
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['id','title','no_of_pages']

    fields = ('title',)
    exclude = ('publish_date',)

