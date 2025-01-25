from django.shortcuts import render

def sudoku_game(request):
    return render(request, 'sudoku/sudoku_game.html')

def easy(request):
    return render(request, 'sudoku/easy.html')

def medium(request):
    return render(request, 'sudoku/medium.html')

def hard(request):
    return render(request, 'sudoku/hard.html')

