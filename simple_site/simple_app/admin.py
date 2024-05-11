from django.contrib import admin
from .models import *
# Register your models here.
# admin.site.register(Phone)

admin.site.register(Menu)
admin.site.register(ModelDevice)

@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    #show field
    list_display = ('id','name','image','is_published')
    # set links for field
    list_display_links = ('id','name',)
    #automatic field completion
    prepopulated_fields = {"slug":("name",)}
    #sort
    ordering = ['name']
    list_editable = ('is_published',)
    list_per_page = 5

@admin.register(HeadPhone)
class HeadphoneAdmin(admin.ModelAdmin):
    list_display = ('id','name','image','is_published')
    list_display_links = ('id','name')
    prepopulated_fields = {"slug":("name",)}
    list_editable = ('is_published',)
    list_per_page = 5


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug":("name",)}

admin.site.site_header = "Панель администрирования"
admin.site.index_title = "TimeShopping"
