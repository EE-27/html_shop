from django.db import models

# Create your models here.
"""
Task 2 In the catalogue application, create models:

Product, Category.

Describe the initial settings for them.

Task 3 For each model, describe the following fields:

Product: name, description, image (preview), category, price per piece, creation date,
 last modified date. Category: name, description.
"""


# pip install Pillow
# py manage.py makemigrations - také update

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.CharField(max_length=255, verbose_name="Description")
    image = models.ImageField(verbose_name="Image", null=True, blank=True)
    category = models.CharField(max_length=100, verbose_name="Category")
    price_per_piece = models.IntegerField(verbose_name="Price per Piece")
    creation_date = models.DateField(verbose_name="Creation Date")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("name",)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.CharField(max_length=255, verbose_name="Description")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("name",)
