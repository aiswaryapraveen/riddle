from django.shortcuts import render

def measy(request):
    return render(request,'memory/easy.html')

def mmedium(request):
    return render(request,'memory/medium.html')

def mhard(request):
    return render(request,'memory/hard.html')
