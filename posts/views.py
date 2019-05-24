import datetime

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.views.generic import ListView

from posts.forms import PostForm
from posts.models import Post, Category


class LatestPostsView(View):

    def get(self, request):
        # Recuperar los ultimos post de la base de datos
        posts = Post.objects.filter(publication_date__lte=datetime.datetime.now()).order_by(
            '-publication_date').select_related('owner')
        # Creamos el contexto
        context = {'latest_posts': posts[:6]}

        # Crear repuesta HTML con los posts
        html = render(request, 'posts/lastest.html', context)

        # Devolver la respueste HTTP
        return HttpResponse(html)


class PostDetailView(View):
    def get(self, request, pk):
        post = get_object_or_404(Post.objects.select_related('owner'), pk=pk )

        # Crear un contexto para pasar la informacion a plantilla
        context = {'post': post}

        # Renderiza plantilla
        html = render(request, 'posts/detail.html', context)

        # devolver respuesta HTTP
        return HttpResponse(html)


class NewPostView(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()

        context = {'form': form}
        return render(request, 'posts/new.html', context)

    def post(self, request):
        post = Post()
        post.owner = request.user
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            new_post = form.save()
            messages.success(request, 'Post successfully created')
            form = PostForm()

        context = {'form': form}
        return render(request, 'posts/new.html', context)

