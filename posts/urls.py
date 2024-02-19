from . import views
from django.urls import path, include

urlpatterns = [
    # path("homepage/", views.homepage, name="homepage"),
    path("", views.PostListCreateView.as_view(), name="create_list_post"),
    path(
        "<int:pk>/",
        views.UpdateDeleteDetailView.as_view(),
        name="delete_update_detail_post",
    ),
]
