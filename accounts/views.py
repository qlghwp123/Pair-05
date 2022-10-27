from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
# Create your views here.

def index(request):
    users = get_user_model().objects.all()
    context = {
        "users": users,
    }
    return render(request, "accounts/index.html", context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect("reviews:index")
    else:
        form = CustomUserCreationForm()
    context = {
        "form":form,
    }
    return render(request, "accounts/signup.html", context)

def detail(request, user_pk):
    user = get_user_model().objects.get(pk=user_pk)

    context = {
        "user": user,
    }
    return render(request, "account/detail.html", context)
