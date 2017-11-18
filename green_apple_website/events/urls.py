from django.conf.urls import url

from events import views

app_name = 'events'

urlpatterns = [
    url(r'^$', views.events, name='events')
]
