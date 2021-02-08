from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('apps.books.urls')),
    path('', include('apps.frontend.urls')),
    path('admin/', admin.site.urls),
]
