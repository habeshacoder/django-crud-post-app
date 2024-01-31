from . import views
from django.urls import path, include

urlpatterns = [
    path("homepage/", views.homepage, name="homepage"),
    path("", views.PostListCreateView.as_view(), name="create_delete_post"),
    path(
        "<int:post_id>/",
        views.UpdateDeleteDetailView.as_view(),
        name="post_delete_update_detail",
    ),
    path("update/<int:post_id>", views.update_post, name="update_post"),
    path("delete/<int:post_id>", views.delete_post, name="delete_post"),
]
