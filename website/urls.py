from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from website import views


# Site URLS
urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    # Others
    url(r'^members/$', views.members, name='members'),
    url(r'^events/', include('events.urls', namespace='events')),
    # Auth
    url(r'^login/$', 'myauth.views.login', name='login'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
)
