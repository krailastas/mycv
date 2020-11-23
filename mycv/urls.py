from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(('data.urls', 'data'), namespace='reviews')),
]


if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
