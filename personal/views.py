from django.shortcuts import render
from personal.models import BlogPost

BlogPost.objects.create(title="Post 1", body="This is the first post.", signature="Love Yourself")
BlogPost.objects.create(title="Post 2", body="This is the second post.", signature="Let Go And Let God")
def home(request):
    return render(request, 'personal/home.html')

def about(request):
    return render(request, 'personal/about.html')

def contact(request):
    return render(request, 'personal/contact.html')

def projects(request):
    return render(request, 'personal/projects.html')

def blog_view(request):
    posts = BlogPost.objects.all()
    return render(request, "personal/blog.html", {"posts": posts})


