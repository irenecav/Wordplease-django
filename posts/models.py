from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    text = models.TextField()
    url = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)


    def __str__(self):
        return self.title




