from django.conf.urls import patterns, include, url
from mlb.views import TopView, HomeView, PythagorasView, SabrView


urlpatterns = patterns('',
    url(r'^$', TopView.as_view()),
    url(r'^player/$', HomeView.as_view(), ),
    url(r'^sabr/$', SabrView.as_view(), ),
    url(r'^pythagoras/$', PythagorasView.as_view(), ),
    url(r'^search/$', 'mlb.views.search'),
    url(r'^pythagoras_search/$', 'mlb.views.pythagoras_search'),
    url(r'^sabr_search/$', 'mlb.views.sabr_search'),
)
