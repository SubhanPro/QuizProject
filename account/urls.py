from django.urls import path
from account import views

urlpatterns = [
    path("signup/", views.register_user, name = "register"),
    path("login/", views.login_user, name = "login"),
    path("logout/", views.logout_user, name = "logout")
]