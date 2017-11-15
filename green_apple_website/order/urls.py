from django.conf.urls import url
from django.views.generic import TemplateView
from order import views

app_name = 'order'
urlpatterns = [
    url(r'^$', views.order, name='order'),

    url(r'details/$',
        TemplateView.as_view(template_name='order/order_details.html'),
        name='order_details'),
    url(r'^(?P<pk>[0-9]+)/add_detail/$', views.add_order, name='add_detail'),
    url(r'^details/pick-up/$', views.pick_up, name='pick-up'),
    url(r'^details/home-delivery/$', views.home_delivery,
        name='home-delivery'),

]
