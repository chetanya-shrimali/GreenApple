from book_a_table import views
from django.conf.urls import url

app_name = 'book_a_table'

urlpatterns = [
    url(r'^$', views.BookFormView.as_view(), name='book'),
]
