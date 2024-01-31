from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from .models import PostModel
from .serializers import PostModelSerializer
from django.shortcuts import get_object_or_404


# Create your views here.
@api_view(http_method_names=["GET"])
def homepage(request: Request):
    response = {"message": "hello django"}
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET", "POST"])
def allPosts(request: Request):
    if request.method == "POST":
        data = request.data
        serializer = PostModelSerializer(data=data)
        print("serializer:", serializer)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "post created",
                "data": serializer.data,
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(
            data={"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
        )
    posts = PostModel.objects.all()
    serializer = PostModelSerializer(instance=posts, many=True)
    print("serializer:", serializer)

    return Response(data=serializer.data, status=status.HTTP_200_OK)


@api_view(http_method_names=["GET"])
def post_detail(request: Request, post_id):
    post = get_object_or_404(PostModel, pk=post_id)

    serializer = PostModelSerializer(instance=post)
    response = {
        "message": "post",
        "data": serializer.data,
    }
    return Response(data=response, status=status.HTTP_200_OK)


@api_view(http_method_names=["DELETE"])
def delete_post(request: Request, post_id):
    post = get_object_or_404(PostModel, pk=post_id)
    post.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(http_method_names=["PUT"])
def update_post(request: Request, post_id: int):
    post = get_object_or_404(PostModel, pk=post_id)
    data = request.data
    print("data------------", data)
    print("post------------", post)
    serializer = PostModelSerializer(instance=post, data=data)
    print("serializer:", serializer)
    if serializer.is_valid():
        serializer.save()
        response = {
            "message": "post updated successfully",
            "data": serializer.data,
        }
        return Response(data=response, status=status.HTTP_200_OK)
    return Response(
        data={"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
    )
