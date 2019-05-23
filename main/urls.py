"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from posts.api import PostsAPI
from posts.views import NewPostView, PostDetailView, LatestPostsView
from users.api import UsersAPI, UserDetailAPI
from users.views import LogoutView, LoginView, BlogListView, SignUpView, BlogView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Users
    path('login', LoginView.as_view(), name='login'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('signup', SignUpView.as_view(), name='signup'),

    # Blogs
    path('blogs/', BlogListView.as_view(), name='blogs'),
    path('blogs/<str:username>/', BlogView.as_view(), name='user_blog'),


    # Posts
    path('posts/new/', NewPostView.as_view(), name='new_post'),
    path('posts/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('', LatestPostsView.as_view(), name='home'),


    # API
    path('api/users/', UsersAPI.as_view(), name='users_api'),
    path('api/users/<int:pk>/', UserDetailAPI.as_view(), name='user_detail'),
    path('api/posts/', PostsAPI.as_view(), name='posts_api')




]
