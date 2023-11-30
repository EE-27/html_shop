from django.db import models

# Create your models here.
"""


Task 4
For the displayed image on the page, implement a template filter that converts the passed path 
to the full path to access the media file:

<!-- Source --> 
<img src="/media/{{{ object.image }}}" />
<!-- Final version -->
<img src="{{ object.image|mediapath }}" /> />

Implement the described functionality using a template tag:

<!-- Source variant -->
<img src="/media/{{ object.image }}}" />
<!-- Final version -->
<img src="{% mediapath object.image %}" /> />

* Optional task
Add functionality to create a product via front-end without using the standard admin.
Implement page-by-page output of the product list.

Translated with www.DeepL.com/Translator (free version)
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
