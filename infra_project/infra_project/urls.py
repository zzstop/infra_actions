from django.contrib import admin
from django.urls.conf import include, path

urlpatterns = [
    path('', include('infra_app.urls', namespace='infra_app')),
    path('admin/', admin.site.urls),
]
