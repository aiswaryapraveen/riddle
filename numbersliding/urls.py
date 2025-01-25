from django.urls import path
from . import views

urlpatterns = [
    path('neasy/', views.neasy, name='neasy'),
    
]