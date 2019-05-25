import datetime

from django.contrib.auth.models import User
from django.db.models import Q, QuerySet
from rest_framework import status
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import get_object_or_404, GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.serializers import PostListSerializer, PostSerializer
from posts.views import PostList
from users.permissions import UserPermission
from users.serializers import UserSerializer, UserListSerializer, WriteUserSerializer, BlogListSerializer


class BlogsAPI(GenericAPIView):

    def get(self, request):
        users = User.objects.all()
        paginated_users = self.paginate_queryset(users)
        serializer = BlogListSerializer(paginated_users, many=True)
        return self.get_paginated_response(serializer.data)


class UserBlogAPI(ListCreateAPIView):

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description', 'url', 'text']
    ordering_fields = ['id', 'description', 'title']

    def get(self, request, username):
        owner = get_object_or_404(User, username=username)
        blog_posts = owner.posts.order_by(
            '-publication_date')

        if not self.request.user.is_authenticated:
            blog_posts = blog_posts.filter(publication_date__lte=datetime.datetime.now())
        elif not self.request.user.is_superuser:
            blog_posts = blog_posts.filter(Q(publication_date__lte=datetime.datetime.now()) | Q(owner=self.request.user))


        response = []
        for post in blog_posts:
            serializer = PostListSerializer(post)
            response.append(serializer.data)

        return Response(response)



class UsersAPI(GenericAPIView):

    permission_classes = [UserPermission]



    def get(self, request):
        users = User.objects.all()
        paginated_users = self.paginate_queryset(users)
        serializer = UserListSerializer(paginated_users, many=True)

        return self.get_paginated_response(serializer.data)



    def post(self, request):
        serializer = WriteUserSerializer(data=request.data)
        if serializer.is_valid():
            new_user = serializer.save()
            user_serializer = UserSerializer(new_user)
            return Response(user_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class UserDetailAPI(APIView):

    permission_classes = [UserPermission]



    def get(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)

        serializer = UserSerializer(user)
        return Response(serializer.data)

    def delete(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)


        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


    def put(self, request, pk):
        user = get_object_or_404(User, pk=pk)
        self.check_object_permissions(request, user)


        serializer = WriteUserSerializer(user, data=request.data)
        if serializer.is_valid():
            updated_user = serializer.save()
            user_serializer = UserSerializer(updated_user)
            return Response(user_serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

