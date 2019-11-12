from django.db import models
from user.models import User


class Tweet(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=140)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username.name
