from django.conf.urls import url

from book_a_table import views

app_name = 'book_a_table'

urlpatterns = [
    url(r'^$', views.book, name='book')
]
