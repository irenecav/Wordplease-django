from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostListSerializer, PostSerializer
from posts.views import PostList


class PostsAPI(PostList, ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    queryset = Post.objects.all()

    def get_serializer_class(self):

        return PostListSerializer if self.request.method == 'GET' else PostSerializer


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)




class PostDetailAPI(RetrieveUpdateDestroyAPIView):

    permission_classes = [PostPermission]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_update(self, serializer):
        serializer.save(owner=self.request.user)
