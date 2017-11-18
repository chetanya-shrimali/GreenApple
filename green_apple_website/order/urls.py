from django.conf.urls import url
from django.views.generic import TemplateView
from order import views

app_name = 'order'
urlpatterns = [
    url(r'^$', views.order, name='order'),
    url(r'details/$', views.order_details, name='order_details'),
    url(r'^(?P<pk1>[0-9]+)/add_detail/(?P<pk2>[0-9]+)/order/$',
        views.add_order, name='add_detail'),
    url(r'^details/pick-up/$', views.pick_up, name='pick-up'),
    url(r'^details/home-delivery/$', views.home_delivery,
        name='home-delivery'),
    url(r'^(?P<pk>[0-9]+)/mail_order/$',
        views.mail_order, name='mail_order'),
    url(r'^order_confirmation/$', views.mail_order, name='order_confirm'),
    url(r'^pickup_confirmation/$', views.mail_order, name='pickup_confirm')
]
