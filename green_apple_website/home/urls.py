from django.conf.urls import url

from home import views

app_name = 'home'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^maps/$', views.maps_api, name='maps'),
    # url(r'^msgs/$', views.message_api, name='msgs')
]
