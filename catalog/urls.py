from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index, contacts, base, AlbumListView, CodeDetailView, BlogPostView, BlogPostCreateView, \
    BlogPostDetailView

urlpatterns = [
                  path("base/", base, name="base"),
                  path("", index),
                  path('contacts/', contacts, name='contacts'),
                  path('album/', AlbumListView.as_view(), name='album'),
                  #  path('album/', album, name='album'),
                  path('album/<int:pk>/', CodeDetailView.as_view(), name='code_detail'),
                  path("blog_post/", BlogPostView.as_view(), name='blog_post'),

                  path("create/", BlogPostCreateView.as_view(), name='blog_create'),
                  path('blog/<int:pk>/', BlogPostDetailView.as_view(), name='blog_detail')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
