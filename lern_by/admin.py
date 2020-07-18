from django.contrib import admin
from .models import Song,Vocabulary

admin.site.register(Song) # register database to admin page
admin.site.register(Vocabulary) # register database to admin page
# Register your models here.
