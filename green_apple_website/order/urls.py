from django.conf.urls import url

from order import views

app_name = 'order'
urlpatterns = [
    url(r'^$', views.order, name='order'),
    url(r'order_details/$', views.order_details, name='order_details')
]
