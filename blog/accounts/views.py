from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.urls import reverse
from .forms import RegisterForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        form.save()
        homeurl = reverse("my_home")
        return HttpResponseRedirect(homeurl)
    else:
        form = RegisterForm()
    return render(request, "accounts/register.html", {'form':form})

def auth_login(request):
    if request.method == "POST":
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            print(user.is_superuser)
            if user is not None:
                homeurl = reverse("my_home")
                return HttpResponseRedirect(homeurl)
    else:
    
        form = LoginForm()
    return render(request, "accounts/login.html", {'form':form})

def auth_logout(request):
    logout(request)
    homeurl = reverse("login")
    return HttpResponseRedirect(homeurl)
    