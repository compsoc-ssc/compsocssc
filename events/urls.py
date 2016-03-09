from django.conf.urls import patterns, include, url
from events import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^logo/', include('events.logo.urls', namespace='logo')),
    # url(r'^orfik/', include('events.orfik.urls', namespace='orfik')),
)
