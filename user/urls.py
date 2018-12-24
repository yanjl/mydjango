from django.urls import path

from .views import login2, logout, register, set_password

app_name = "user"  # namespace
urlpatterns = [
    path("login/", login2, name="login"),
    path("register/", register, name="register"),
    path("setpassword/", set_password, name="set_password"),
    path("logout/", logout, name="logout"),
]
