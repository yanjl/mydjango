from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render


# Create your views here.
def login2(request):
    unit_2 = "/user/register.html"
    unit_2_name = "Register"

    unit_1 = "/user/setpassword.html"
    unit_1_name = "Change password"
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=username):
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                return redirect("/user/login/")
            else:
                tips = "password or username error, please input once again."
        else:
            tips = "user not exist,please register."
    return render(request, "user/user.html", locals())


def register(request):
    pass


def set_password(request):
    pass


def logout(request):
    pass
