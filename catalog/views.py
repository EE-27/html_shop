from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils import timezone
from django.views.generic import ListView, DetailView, CreateView

from catalog.models import Product, BlogPost


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


class BlogPostView(ListView):
    model = BlogPost
    template_name = 'catalog/blog_post.html'


class BlogPostCreateView(CreateView):
    model = BlogPost
    fields = ('title', 'content')
    template_name = 'catalog/blog_create.html'

    def form_valid(self, form):
        # Set the creation_date to the current date
        form.instance.creation_date = timezone.now().date()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog_post')


class BlogPostDetailView(DetailView):
    model = BlogPost
    template_name = 'catalog/blog_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.number_of_views += 1
        self.object.save()
        return self.object
