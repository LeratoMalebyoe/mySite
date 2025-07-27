from django.urls import path
from . import views

app_name = 'user_auth'

urlpatterns = [
    path('',                views.user_login,        name='login'),
    path('authenticate/',   views.authenticate_user, name='authenticate_user'),
    path('signup/',         views.signup,            name='signup'),
    path('logout/',         views.user_logout,       name='logout'),
    path('profile/',        views.show_user,      name='profile'),

]
