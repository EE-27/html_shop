from django.contrib import admin

from catalog.models import Product, Category, BlogPost, Version


# Register your models here.

# py manage.py createsuperuser

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price_per_piece', 'category',)
    list_filter = ('category',)
    search_fields = ('name', 'description',)
@admin.register(Version)
class VersionAdmin(admin.ModelAdmin):
    list_display = ("product", "version_number", "version_name", "current_version")

@admin.register(Category)
class Category(admin.ModelAdmin):
    list_display = ('id', 'name', 'description',)
    search_fields = ('name', 'description',)


@admin.register(BlogPost)
class BlogPost(admin.ModelAdmin):
    list_display = ('title', 'creation_date', 'publication_sign', 'number_of_views')
    search_fields = ('title', 'creation_date')
    list_filter = ('publication_sign',)