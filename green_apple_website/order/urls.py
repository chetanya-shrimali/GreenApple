from django.conf.urls import url

from order import views

app_name = 'order'
urlpatterns = [
    url(r'^$', views.order, name='order'),
    url(r'order_details/$', views.order_details, name='order_details'),
    url(r'^(?P<pk>[0-9]+)/add_detail/$', views.add_order,
        name='add_detail')
]
