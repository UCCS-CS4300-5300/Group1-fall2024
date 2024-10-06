from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from cookapp.admin import admin_site  # the custom admin site

urlpatterns = [
    path('admin/', admin_site.urls),
    path('', include('cookapp.urls')),
]

# MEDIA and STATIC files aren’t based off of root url, but are instead based on their own path such as media/ and static/.
# ex. http://cookapp.com/media/somefile.jpg
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)