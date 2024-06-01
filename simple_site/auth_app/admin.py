from django.contrib import admin
from .models import *

# admin.site.register(User)


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ('id','username','email')
    list_display_links = ('id','username')
