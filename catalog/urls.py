from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from catalog.views import index, contacts, album

urlpatterns = [
                  path("", index),
                  path('contacts/', contacts, name='contacts'),
                  path('album/', album, name='album'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
