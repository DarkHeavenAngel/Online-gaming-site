from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from main.views import GamesList, GameDetail, AuthorsList, AuthorDetail, PublisherDetail, PublishersList

urlpatterns = [
    path('games/', GamesList.as_view()),
    path('games/<int:pk>/', GameDetail.as_view()),
    path('authors/', AuthorsList.as_view()),
    path('authors/<int:pk>/', AuthorDetail.as_view()),
    path('publishers/', PublishersList.as_view()),
    path('publishers/<int:pk>/', PublisherDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)