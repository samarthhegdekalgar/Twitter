from rest_framework.generics import ListAPIView
from .serializer import UserSerializer
from .models import User


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

