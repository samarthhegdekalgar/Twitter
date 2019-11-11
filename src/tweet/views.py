from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from .serializer import TweetSerializer
from .models import Tweet
from rest_framework.generics import ListAPIView, CreateAPIView


class TweetListAPIView(ListAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializer


class TweetCreateAPIView(CreateAPIView):
    serializer_class = TweetSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


