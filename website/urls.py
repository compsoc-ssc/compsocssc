from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from website import views


# Site URLS
urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name':'login.html'}, name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name':'logged_out.html'}, name='logout'),
    url(r'^register/$', views.register, name='register'),
    # ----- Events
    # url(r'^logo/', include('events.logo.urls', namespace='logo')),
    # url(r'^orfik/', include('events.orfik.urls', namespace='orfik')),
)

# Event Flatpages
urlpatterns += patterns(
    'django.contrib.flatpages.views',
    (r'^(?P<url>.*/)$', 'flatpage'),
    
)
