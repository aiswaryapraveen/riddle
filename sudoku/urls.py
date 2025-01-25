from django.urls import path
from . import views

urlpatterns = [
    path('easy/',views.easy,name='easy'),
    path('medium/',views.medium,name='medium'),
    path('hard/',views.hard,name='hard'),

]
