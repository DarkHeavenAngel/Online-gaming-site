from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from main.views import GamesList, GameDetail, AuthorsList, AuthorDetail, PublisherDetail

urlpatterns = [
    path('games/', GamesList.as_view()),
    path('games/<int:pk>/', GameDetail.as_view()),
    path('authors/', AuthorsList.as_view()),
    path('authors/<int:pk>/', AuthorDetail.as_view()),
    path('publishers/', PublisherDetail.as_view()),
    path('publishers/<int:pk>/', PublisherDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)