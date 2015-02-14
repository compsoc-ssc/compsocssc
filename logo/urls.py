from django.conf.urls import patterns, url
from logo import views


urlpatterns=patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^success/$', views.success, name='success'),
    # url(r'^instructions/$', views.instructions, name='instructions'),
)
