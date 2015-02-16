from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from website import views


urlpatterns = patterns('',
    url(r'^$',views.home,name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$',views.contact,name='contact'),
    url(r'^about/$',views.about,name='about'),
    #---------authentication
    #url(r'^accounts/', include('allauth.urls')),
    url(r'^login/$','django.contrib.auth.views.login',{'template_name':'login.html'},name='login'),
    url(r'^logout/$','django.contrib.auth.views.logout',{'template_name':'logged_out.html'},name='logout'),
    url(r'^logout/$','django.contrib.auth.views.logout',{'template_name':'logged_out.html'},name='password_change_done'),
    url(r'^register/$',views.register,name='register'),
    #url(r'^change/$','django.contrib.auth.views.password_change',{'template_name':'pwd_reset.html'},name='password_change'),
    #---------apps
    url(r'^orfik/',include('orfik.urls',namespace='orfik')),
    url(r'^logo/',include('logo.urls',namespace='logo')),
)
#---------event flatpages
urlpatterns += patterns('django.contrib.flatpages.views',
    (r'^(?P<url>.*/)$', 'flatpage'),
    )
