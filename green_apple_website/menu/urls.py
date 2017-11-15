from django.conf.urls import url

from menu import views

app_name = 'menu'

urlpatterns = [
    url(r'^$', views.sub_menu, name='menu'),
    # url(r'^(?P<pk>[0-9]+)/submenu/$', views.sub_menu, name='sub_menu')
]
