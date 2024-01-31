from rest_framework import serializers
from .models import PostModel


class PostModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = ["id", "title", "content", "created"]
