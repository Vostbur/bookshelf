from django.urls import path

from . import views


urlpatterns = [
    path('api/book/', views.BookListView.as_view()),
    path('api/book/<int:pk>', views.BookDetailView.as_view()),
]
