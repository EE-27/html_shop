from django.shortcuts import render

from catalog.models import Product


# Create your views here.

def index(request):
    return render(request, 'catalog/index.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone});\n{message}")
    return render(request, 'catalog/contacts.html')

def album(request):
    product_list = Product.objects.all()
    context = {
        "object_list":product_list
    }
    return render(request, 'catalog/album.html', context)