from django.conf.urls import include, url
from django.conf.urls.static import static
from noball.settings import STATIC_ROOT, STATIC_URL
from mlb import urls

urlpatterns = [
                  url(r'^mlb/', include(urls)),
              ] + static(STATIC_URL, document_root=STATIC_ROOT)
