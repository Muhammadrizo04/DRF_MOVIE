from django.urls import path
from .views import *

urlpatterns = [
    path('movie/', MovieListView.as_view()),
    path('movie/<int:pk>/', MovieDetailView.as_view()),
    path("review/", ReviewCreateView.as_view()),
    path("rating/", AddStarRatingView.as_view()),
    path("actors/", ActorsLitView.as_view()),
    path("actors/<int:pk>/", ActorsDetailView.as_view()),

]