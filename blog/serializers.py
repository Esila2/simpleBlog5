from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField(read_only=True)
    author = serializers.PrimaryKeyRelatedField(write_only=True)

    class Meta:
        model = Post
        fields = '__all__'
