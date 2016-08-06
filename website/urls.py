from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from website import views
from django.conf.urls.static import static


# Site URLS
urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^admin/', include(admin.site.urls)),
    # Others
    url(r'^members/$', views.members, name='members'),
    url(r'^events/', include('events.urls', namespace='events')),
    # Auth
    url(r'^login/$', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^logout/$', views.logout, name='logout'),
    # CompSoc join
    url(r'^join/', include('join.urls', namespace='join')),
)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)