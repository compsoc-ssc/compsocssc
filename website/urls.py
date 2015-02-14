from django.conf.urls import patterns, include, url
from django.contrib import admin
from website import views
urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.home,name='home'),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^orfik/',include('orfik.urls',namespace='orfik')),
)
