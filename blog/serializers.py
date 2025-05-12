from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.StringRelatedField(read_only=True, source='author')
    author = serializers.PrimaryKeyRelatedField(write_only=True, queryset=User.objects.all())

    class Meta:
        model = Post
        fields = '__all__'
