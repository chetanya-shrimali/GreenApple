from django.conf.urls import url

from . import views

app_name = 'drop_a_note'

urlpatterns = [
    url(r'^$', views.contact_us, name='drop_note'),
    # url(r'^contact/$', views.contact_us, name='contact'),
]
