from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostListSerializer(ModelSerializer):


    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'description', 'publication_date']


class PostSerializer(ModelSerializer):

     class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'description', 'text', 'publication_date', 'owner',
                  'categories' ]

        read_only_fields = ['id', 'modification_date']