from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from website import views


# Site URLS
urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^members/$', views.members, name='members'),
    url(r'^events/$', include('events.urls', namespace='events')),

    # url(r'^login/$', 'django.contrib.auth.views.login', 
    #     {'template_name' : 'auth/login.html'}, name='login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', 
    #     {'template_name' : 'auth/ogged_out.html'}, name='logout'),
    # url(r'^register/$', views.register, name='register'),
    # ----- Events
)

# Event Flatpages
urlpatterns += patterns(
    'django.contrib.flatpages.views',
    (r'^(?P<url>.*/)$', 'flatpage'),
    
)
