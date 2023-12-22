from django.core.exceptions import PermissionDenied

from config import settings
from django.db import models

# Create your models here.
"""
Add a new model "Version", which should contain the following fields:

product, version number, version name, current version attribute. 
If there is an active version, implement output of information about the active version to the product list.
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

    is_published = models.BooleanField(default=False, verbose_name="Published")

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        # Check if the user is the owner
        user = kwargs.pop('user', None)
        if user and user != self.owner:
            raise PermissionDenied("You do not have permission to edit this product.")

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
        ordering = ("name",)


class Version(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='versions', verbose_name="Product")
    version_number = models.IntegerField(verbose_name="Version Number")
    version_name = models.CharField(max_length=100, verbose_name="Version Name")
    current_version = models.BooleanField(verbose_name="Current Version")

    def __str__(self):
        return f"{self.product.name} - Version {self.version_number} ({self.version_name})"

    class Meta:
        verbose_name = "Version"
        verbose_name_plural = "Versions"

    @property
    def is_active(self):
        return self.current_version


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    description = models.CharField(max_length=255, verbose_name="Description")

    def __str__(self):
        return f"{self.name}"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ("name",)


class BlogPost(models.Model):
    title = models.CharField(max_length=100, verbose_name="Title")
    slug = models.CharField(max_length=100, verbose_name="Slug")
    content = models.TextField(verbose_name="Content")
    preview = models.ImageField(verbose_name="Preview", null=True, blank=True)
    creation_date = models.DateField(verbose_name="Creation Date")
    publication_sign = models.BooleanField(default=False, verbose_name="Publication sign")
    number_of_views = models.PositiveIntegerField(default=0, verbose_name="Number of Views")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "Blog post"
        verbose_name_plural = "Blog posts"
