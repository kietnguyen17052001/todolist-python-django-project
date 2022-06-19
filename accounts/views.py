from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render

from accounts.forms import LoginForm, RegistrationForm
from tasks.forms import TaskForm


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=request.POST["username"], password=request.POST["password"]
            )
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect("tasks:index")
        else:
            return render(request, "login.html", {"form": form})
    else:
        return render(request, "login.html", {"form": LoginForm()})

    return redirect("tasks:index")


def register_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=request.POST["username"],
                email=request.POST["email"],
                password=request.POST["password"],
            )
            return redirect("auth:login")
        else:
            return render(request, "register.html", {"form": form})
    else:
        return render(request, "register.html", {"form": RegistrationForm()})


def logout_view(request):
    logout(request)
    return redirect("tasks:index")
