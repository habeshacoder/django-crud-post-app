from django.contrib import admin
from django.urls import path, include
from posts.views import PostViewSet

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("account.urls")),
    path("posts/", include("posts.urls")),
]
