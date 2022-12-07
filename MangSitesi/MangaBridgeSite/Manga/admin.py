from django.contrib import admin

# Register your models here.
from .models import Manga, Chapter

admin.site.register(Manga)
admin.site.register(Chapter)