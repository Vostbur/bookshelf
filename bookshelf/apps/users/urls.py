from django.urls import path

from . import views


urlpatterns = [
    path('registr/', views.RegistrUserView.as_view(), name='registr'),
]
