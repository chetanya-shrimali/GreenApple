from django.conf import settings
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/', include('about_us.urls')),
    url(r'^book_a_table/', include('book_a_table.urls')),
    url(r'^events/', include('events.urls')),
    url(r'^home/', include('home.urls')),
    url(r'^menu/', include('menu.urls')),
    url(r'^order/', include('order.urls')),
    url(r'^drop_a_note/', include('drop_a_note.urls'))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
