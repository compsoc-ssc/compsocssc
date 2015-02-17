from django.conf.urls import patterns, url
from logo import views


urlpatterns=patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^gallery/$',views.gallery,name='gallery'),
    url(r'^submission/$', views.submission, name='submission'),
    url(r'^success/$', views.success, name='success'),
)
