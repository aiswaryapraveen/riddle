from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='games/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user/settings/', views.user_settings, name='user_settings'),
    path('games/', views.play, name='play' ),
    path('',include('sudoku.urls')),
    path('',include('numbersliding.urls')),
    path('',include('memory.urls')),
    path('type/',include('type.urls')),
]
