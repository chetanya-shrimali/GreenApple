from django.conf.urls import url

from order import views

app_name = 'order'
urlpatterns = [
    url(r'^$', views.order, name='order')
]
