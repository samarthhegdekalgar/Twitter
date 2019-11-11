from django.urls import path
from .views import TweetListAPIView, TweetCreateAPIView


urlpatterns = [
    path('', TweetListAPIView.as_view(), name='tweet-list'),
    path('create/', TweetCreateAPIView.as_view(), name='create-tweet'),
]
