from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Product


# Create your views here.

def index(request):
    return render(request, 'catalog/index.html')


def base(request):
    return render(request, 'catalog/base.html')


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(f"{name} ({phone});\n{message}")
    return render(request, 'catalog/contacts.html')


# def album(request):
#     product_list = Product.objects.all()
#     context = {
#         "object_list":product_list
#     }
#     return render(request, 'catalog/album.html', context)

class AlbumListView(ListView):
    model = Product
    template_name = 'catalog/album.html'


# def code_detail(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     context = {
#         'product': product
#     }
#     return render(request, 'catalog/code_detail.html', context)


class CodeDetailView(DetailView):
    model = Product
    template_name = 'catalog/code_detail.html'
