from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView

from .models import PostModel
from .serializers import PostModelSerializer
from django.shortcuts import get_object_or_404


# create class based apiviews for create and list posts
class PostListCreateView(
    generics.GenericAPIView, mixins.CreateModelMixin, mixins.ListModelMixin
):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.all()

    def get(self, request: Request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UpdateDeleteDetailView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.all()

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
