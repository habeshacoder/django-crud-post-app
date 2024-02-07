from django.urls import path
from . import views

urlpatterns = [
    path("create_user", views.SignUpView.as_view(), name="create_user"),
    path("users", views.SignUpView.as_view(), name="get_all"),
    path("user/<pk>", views.SignUpView.as_view(), name="get_user"),
    path("user/update/<int:user_id>", views.SignUpView.as_view(), name="update_user"),
    path("user/delete/<int:user_id>", views.SignUpView.as_view(), name="delete_user"),
]
