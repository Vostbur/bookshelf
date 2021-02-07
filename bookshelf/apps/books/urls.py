from django.urls import path

from . import views


urlpatterns = [
    path('api/book/', views.BookListCreate.as_view()),
    path('', views.index, name='index'),
]
