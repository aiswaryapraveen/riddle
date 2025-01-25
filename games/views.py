from django.shortcuts import render

def home(request):
    return render(request, 'games/base.html')

def about(request):
    return render(request, 'games/about.html' )
