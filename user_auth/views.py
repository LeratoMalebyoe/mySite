from django.shortcuts       import render, redirect
from django.contrib.auth    import authenticate, login, logout
from django.contrib.auth.models import User
from django.http            import HttpResponseRedirect
from django.urls            import reverse

def user_login(request):
    return render(request, 'authentication/login.html')

def authenticate_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        return HttpResponseRedirect(reverse('user_auth:login'))
    login(request, user)
    return HttpResponseRedirect(reverse('user_auth:profile'))

def signup(request):
    if request.method == 'POST':
        uname = request.POST['username']
        pwd   = request.POST['password']
        fname = request.POST['first_name']
        if User.objects.filter(username=uname).exists():
            return render(request, 'authentication/signup.html', {'error': 'Username taken'})
        User.objects.create_user(username=uname, password=pwd, first_name=fname)
        return HttpResponseRedirect(reverse('user_auth:login'))
    return render(request, 'authentication/signup.html')

def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('user_auth:login'))

def show_user(request):
    return render(request, 'authentication/user.html', {
        'username': request.user.username,
        'first_name': request.user.first_name
    })
