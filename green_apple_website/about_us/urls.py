from django.conf.urls import url

from about_us import views

app_name = 'about_us'
urlpatterns = [
    url(r'^$', views.about, name='about')
]
