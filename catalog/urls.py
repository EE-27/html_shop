from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.views.decorators.cache import cache_page

from catalog.views import index, contacts, base, AlbumListView, CodeDetailView, BlogPostView, BlogPostCreateView, \
    BlogPostDetailView, BlogPostUpdateView, BlogPostDelete, ProductCreateView, ProductUpdateView, CategoryListView

urlpatterns = [
                  path("base/", base, name="base"),
                  path("", index),
                  path('contacts/', contacts, name='contacts'),
                  path('album/', AlbumListView.as_view(), name='album'),
                  #  path('album/', album, name='album'),
                  path('album/<int:pk>/',cache_page(60)(CodeDetailView.as_view()), name='code_detail'),
                  path('album_form/<int:pk>/', ProductUpdateView.as_view(), name="code_update"),
                  path("create_product/", ProductCreateView.as_view(), name="product_create"),

                  path("blog_post/", BlogPostView.as_view(), name='blog_post'),

                  path("create/", BlogPostCreateView.as_view(), name='blog_create'),
                  path('blog_post/<int:pk>/', BlogPostDetailView.as_view(), name='blog_detail'),
                  path('blog_update/<int:pk>/', BlogPostUpdateView.as_view(), name='blog_update'),
                  path('blog_delete/<int:pk>/', BlogPostDelete.as_view(), name='blog_delete'),

                  path('categories/', CategoryListView.as_view(), name='all_categories'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
