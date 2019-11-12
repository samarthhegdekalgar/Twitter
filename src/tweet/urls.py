from django.urls import path
from .views import TweetListAPIView, TweetCreateAPIView, TweetUpdateAPIView, TweetDestroyAPIView

urlpatterns = [
    path('', TweetListAPIView.as_view(), name='tweet-list'),
    path('create/', TweetCreateAPIView.as_view(), name='create-tweet'),
    path('update/<int:pk>', TweetUpdateAPIView.as_view(), name='update-tweet'),
    path('delete/<int:pk>', TweetDestroyAPIView.as_view(), name='delete-tweet'),
]