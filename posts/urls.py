from . import views
from django.urls import path, include

urlpatterns = [
    # path("homepage/", views.homepage, name="homepage"),
    path("", views.PostViewSet.as_view({"get": "list"}), name="create_list_post"),
    path(
        "<pk>/",
        views.UpdateDeleteDetailView.as_view(),
        name="delete_update_detail_post",
    ),
]
