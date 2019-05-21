from django.forms import ModelForm
from django import forms
from posts.models import Post


class PostForm(ModelForm):

    url = forms.CharField(required=False)


    class Meta:
        model = Post

        fields = ['title', 'description', 'url', 'text', ]


