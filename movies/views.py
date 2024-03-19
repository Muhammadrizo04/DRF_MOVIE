from rest_framework import generics
from django.db import models

from .service import get_client_ip
from .models import Movie, Actor
from .serializers import *

class MovieListView(generics.ListAPIView):
    """Вывод списка фильмов"""

    serializer_class = MovieListSerializer
    def get_queryset(self):
        movies = Movie.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings",
                                      filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return movies


class MovieDetailView(generics.RetrieveAPIView):
    """Вывод фильмов"""

    queryset = Movie.objects.filter(draft=False)
    serializer_class = MovieDetailSerializer
    


class ReviewCreateView(generics.CreateAPIView):
    """Добавление отзыва к филму"""
    serializer_class = ReviewCreateSerializer
    


class AddStarRatingView(generics.CreateAPIView):
    """Добавление рейтинга фильму"""
    
    serializer_class = CreateRatingSerializer
    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))


class ActorsLitView(generics.ListAPIView):
    """Вывод списка актеров"""
    queryset = Actor.objects.all()
    serializer_class = ActorListSerializer


class ActorsDetailView(generics.RetrieveAPIView):
    """Вывод актера или режиссера"""
    queryset = Actor.objects.all()
    serializer_class = ActorDetailSerializer