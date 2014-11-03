from django.conf.urls import patterns, include, url

from noball.settings import STATIC_ROOT

urlpatterns = patterns('',
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve'
    ,{'document_root': STATIC_ROOT}),
    url(r'^mlb/', include('mlb.urls')),
)

