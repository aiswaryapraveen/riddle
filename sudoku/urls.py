from django.urls import path
from . import views

urlpatterns = [
    path('sudoku/', views.sudoku_game, name='sudoku_game'),
]
