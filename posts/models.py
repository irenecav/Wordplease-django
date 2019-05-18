from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=300)
    text = models.TextField()
    url = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)



