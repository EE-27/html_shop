from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index, contacts, base, AlbumListView, CodeDetailView

urlpatterns = [
                  path("base/", base, name="base"),
                  path("", index),
                  path('contacts/', contacts, name='contacts'),
                  path('album/', AlbumListView.as_view(), name='album'),
                  #  path('album/', album, name='album'),
                  path('album/<int:pk>/', CodeDetailView.as_view(), name='code_detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
