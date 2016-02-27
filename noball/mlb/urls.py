from django.conf.urls import url
from mlb.views import TopView, HomeView, PythagorasView, SabrView
from mlb import views


urlpatterns = [
    url(r'^$', TopView.as_view(), ),
    url(r'^player/$', HomeView.as_view(), ),
    url(r'^sabr/$', SabrView.as_view(), ),
    url(r'^pythagoras/$', PythagorasView.as_view(), ),
    url(r'^search/$', views.search),
    url(r'^pythagoras_search/$', views.pythagoras_search),
    url(r'^sabr_search/$', views.sabr_search),
]
