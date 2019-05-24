from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from posts.models import Post
from posts.permissions import PostPermission
from posts.serializers import PostListSerializer, PostSerializer
from posts.views import PostList


class PostsAPI(PostList, ListCreateAPIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['title', 'description', 'url', 'owner__first_name', 'owner__last_name', 'text']
    ordering_fields = ['id', 'publication_date', 'modification_date', 'title']

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
