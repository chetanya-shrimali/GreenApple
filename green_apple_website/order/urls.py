from django.conf.urls import url

from order import views

app_name = 'order'
urlpatterns = [
    url(r'^$', views.order, name='order'),
    url(r'order_details/$', views.order_details, name='order_details'),
    url(r'^(?P<pk1>[0-9]+)/add_detail/(?P<pk2>[0-9]+)/order/$',
        views.add_order,
        name='add_detail')
]
