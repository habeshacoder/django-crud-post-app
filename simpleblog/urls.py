from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.views import PostViewSet

router = DefaultRouter()
router.register("", PostViewSet, basename="post_list_retrieval")
urlpatterns = [
    path("admin/", admin.site.urls),
    path("posts/", include(router.urls)),
]
