from django.urls import path
from . import views

urlpatterns = [
    path('neasy/', views.neasy, name='neasy'),
    path('nmedium/',views.nmedium,name='nmedium'),
    path('nhard/',views.nhard,name='nhard'),
]