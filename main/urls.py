from django.urls import path
from .views import GenreAPIView,DeatilGenreView

urlpatterns = [
    path('',GenreAPIView ),
    path('<int:pk>/',DeatilGenreView.as_view())
]