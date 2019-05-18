from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

from posts.models import Post


def latest_posts(request):
    #Recuperar los ultimos post de la base de datos
    posts = Post.objects.all().order_by('-modification_date')

    #Creamos el contexto
    context = {'latest_posts': posts[:6]}

    #Crear repuesta HTML con los posts
    html = render(request, 'posts/lastest.html', context)

    #Devolver la respueste HTTP
    return  HttpResponse(html)


def post_detail(request, pk):
    try:

        post = Post.objects.get(pk=pk)

    except Post.DoesNotExist:
        return HttpResponseNotFound()

    #Crear un contexto para pasar la informacion a plantilla
    context = {'post': post}

    #Renderiza plantilla
    html = render(request,'posts/detail.html', context)

    #devolver respuesta HTTP
    return HttpResponse(html)




