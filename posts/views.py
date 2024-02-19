from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins
from rest_framework.decorators import api_view, APIView
from rest_framework.permissions import IsAuthenticated
from .models import PostModel
from .serializers import PostModelSerializer
from django.shortcuts import get_object_or_404


# create class based apiviews for create and list posts
from rest_framework import generics, mixins


# class PostListCreateView(
#     mixins.ListModelMixin,
#     mixins.RetrieveModelMixin,
#     mixins.CreateModelMixin,
#     generics.GenericViewSet,
# ):
#     queryset = PostModel.objects.all()
#     serializer_class = PostModelSerializer
#     Permission_classes = [IsAuthenticated]

#     def list(self, request: Request):
#         return self.list(request)

#     # def retrieve(self, request: Request, pk=None):
#     #     return self.retrieve(request, pk)

#     def create(self, request):
#         return self.create(request)


class PostListCreateView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = PostModel.objects.all()
    serializer_class = PostModelSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request: Request, *args, **kwargs):
        return self.list(request)

    def post(self, request: Request, *args, **kwargs):
        return self.create(request)


class UpdateDeleteDetailView(
    generics.GenericAPIView,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
):
    serializer_class = PostModelSerializer
    queryset = PostModel.objects.all()
    permission_classes = [IsAuthenticated]

    def delete(self, request: Request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request: Request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def get(self, request: Request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
