from django.conf.urls import url

from .views import (
    new_member_form,
    join_success,
)

urlpatterns = [
    url(r'^$', new_member_form, name='home'),
    url(r'^success/$', join_success, name="success")
]
