from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index, contacts, album, code_detail, base

urlpatterns = [
                  path("base/", base, name="base"),
                  path("", index),
                  path('contacts/', contacts, name='contacts'),
                  path('album/', album, name='album'),
                  path('item/<int:pk>/', code_detail, name='code_detail'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
