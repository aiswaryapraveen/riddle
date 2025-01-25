from django.urls import path
from . import views

urlpatterns = [
    path('measy/',views.measy,name='measy'),
    path('mmedium/',views.mmedium,name='mmedium'),
    path('mhard/',views.mhard,name='mhard'),
]
