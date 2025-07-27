from django.shortcuts import render

def home(request):
    """"Home page popup"""
    return render(request, 'personal/home.html')

def about(request):
    return render(request, 'personal/about.html')

def contact(request):
    return render(request, 'personal/contact')

def projects(request):
    return render(request, 'personal/projects.html')

def blog(request):
    return render(request, 'personal/blog.html')
