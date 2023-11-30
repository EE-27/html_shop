from django.contrib import admin

from catalog.models import Product, Category, BlogPost


# Register your models here.

# py manage.py createsuperuser

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_per_piece', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    search_fields = ('name', 'description',)


@admin.register(BlogPost)
class BlogPost(admin.ModelAdmin):
    list_display = ('title', 'creation_date', 'publication_sign', 'number_of_views')
    search_fields = ('title', 'creation_date')
    list_filter = ('publication_sign',)