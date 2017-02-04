from django.conf.urls import patterns, url
from events.orfik import views


urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
    url(r'^(?P<q_no>\d+)/$', views.question, name='question'),
    url(r'^leaderboard/$', views.leader, name='leader'),
    url(r'^instructions/$', views.instructions, name='instructions'),
    url(r'^remind/',views.authorize,name='authorize'),
    url(r'^auth',views.add_event,name='add'),
)
