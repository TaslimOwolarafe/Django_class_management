from django.shortcuts import render
from django.contrib.auth import login
from . forms import LoginForm
from django.http import HttpResponseRedirect
# Create your views here.

def login_view(request):
    form = LoginForm(request.POST or None)
    if request.POST and form.is_valid():
        user = form.login(request)
        if user:
            login(request, user)
            return HttpResponseRedirect("users/home.html")
    return render(request, 'registration/login.html', {'login_form': form })

def home(request):
    return render(request, "users/home.html")