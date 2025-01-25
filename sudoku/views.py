from django.shortcuts import render

def sudoku_game(request):
    return render(request, 'sudoku_game.html')
