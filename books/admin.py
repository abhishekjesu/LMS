from django.contrib import admin
from .models import BooksDB

# Register your models here.

@admin.register(BooksDB)
class UserAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publisher', 'language' , 'copies')




