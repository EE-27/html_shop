from django.db import models

# Create your models here.
"""



Task 2 Create a new blog post model with the following fields:

title, 
slug (implement via CharField), 
content, preview (image), 
creation date, 
publication sign, 
number of views. 

Implement a CRUD for the new model to work with the blog.
--Slug - a human-understandable URL, is a set of characters that can be read as coherent words or 
--sentences in the address bar, serves as a unique record identifier within a single model and consists 
--of characters that are safe for query processing:

0-9 ,
a-z (usually lower case), 
character - .

Task 3 Modify the output and query processing by adding the following logic at the controller level:

when opening an individual article, 
increase the view counter; 
display in the list of articles only those that have a positive publication sign; 
when creating, dynamically generate a slug name for the title; 
after successfully editing an entry, redirect the user to view that article. 

* Additional task When an article reaches 100 views, send yourself an email 
congratulating yourself on the achievement.

Note: we recommend using the Yandex mail service to send emails.
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
