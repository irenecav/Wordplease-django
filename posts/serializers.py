from rest_framework.serializers import ModelSerializer

from posts.models import Post


class PostListSerializer(ModelSerializer):


    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'description']


class PostSerializer(ModelSerializer):

     class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'description', 'text', 'creation_date', 'modification_date', 'owner',
                  'categories' ]

        read_only_fields = ['id','creation_date', 'modification_date']