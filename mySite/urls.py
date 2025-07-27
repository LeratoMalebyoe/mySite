from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from personal import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('projects/', views.projects, name='projects'),
    path('blog/', views.blog_view, name='blog'),
    path('polls/', include(('polls.urls', 'polls'), namespace='polls')),
    path('auth/', include(('user_auth.urls', 'user_auth'), namespace='user_auth')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
