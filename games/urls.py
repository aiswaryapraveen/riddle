from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='games/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('games/', views.play, name='play' ),
]
