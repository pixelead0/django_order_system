
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('v1/users/', include('app.users.urls')),
    # path('v1/zipcodes/', include('app.zipcodes.urls')),
    # path('v1/', include('app.people.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
