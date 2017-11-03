from django.conf.urls import url

from book_a_table import views

urlpatterns = [
    url(r'^$', views.formDetail, name='form')
]
