from django.conf.urls import patterns,url
from orfik import views
urlpatterns=patterns('',
    url(r'^$',views.home,name='home'),
    url(r'^(?P<q_no>\d+)/$',views.question,name='question'),
    url(r'^(?P<q_no>\d+)/hint/$',views.hint,name='hint'),
    url(r'^leaderboard/$',views.leader,name='leader'),
    url(r'^instructions/$',views.instructions,name='instructions'),
)
