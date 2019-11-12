from django.shortcuts import render
from django.views.generic import ListView
from .serializer import UserSerializer
from .models import User


class UserListView(ListView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
