from django.contrib import admin

# Register your models here.
from .models import Lecturer

class LecturerAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


admin.site.register(Lecturer, LecturerAdmin)
