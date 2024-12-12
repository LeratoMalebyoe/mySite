from django.contrib import admin
from django.urls import path
from personal import views

urlpatterns = [
    path('', views.home, name='home'),  # Root URL
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
]
