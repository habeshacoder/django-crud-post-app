from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status, generics, mixins, viewsets
from rest_framework.decorators import api_view, APIView

from .models import PostModel
from .serializers import PostModelSerializer
from django.shortcuts import get_object_or_404


# create class based apiviews for create and list posts
class PostViewSet(viewsets.ViewSet):
    def list(self, request: Request):
        queryset = PostModel.objects.all()
        serializer = PostModelSerializer(instance=queryset, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request: Request, pk=None):
        post = get_object_or_404(PostModel, pk=pk)
        serializer = PostModelSerializer(instance=post)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = PostModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
