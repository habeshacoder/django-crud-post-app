from django.urls import path
from . import views

urlpatterns = [
    path("create_user", views.SignUpView.as_view(), name="create_user"),
    path("sign_in", views.SignInView.as_view(), name="sign_in"),
]
