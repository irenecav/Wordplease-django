from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)


    def __str__(self):
        return self.name




class Post(models.Model):

    title = models.CharField(max_length=80)
    description = models.CharField(max_length=190)
    text = models.TextField()
    url = models.URLField()
    creation_date = models.DateTimeField(auto_now_add=True)
    modification_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)



    def __str__(self):
        return self.title






