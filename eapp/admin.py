from django.contrib import admin
from eapp.models import Category, Products
# Register your models here.


class categoryAdmin(admin.ModelAdmin):
    list_display=['id', 'name']
admin.site.register(Category, categoryAdmin)


class productAdmin(admin.ModelAdmin):
    list_display=['id','name','price','category','description','image','stock','available','created','updated']
    list_editable=['price','stock','available']
    list_per_page= 20
admin.site.register(Products, productAdmin)