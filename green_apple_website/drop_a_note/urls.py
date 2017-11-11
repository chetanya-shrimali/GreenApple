from django.conf.urls import url

from . import views

app_name = 'drop_a_note'
urlpatterns = [
    url(r'^$', views.drop_note, name='drop_note')
]
