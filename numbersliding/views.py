from django.shortcuts import render

# Create your views here.

def neasy(request):
    return render(request,'numbersliding/easy.html')
def nmedium(request):
    return render(request,'numbersliding/medium.html')
def nhard(request):
    return render(request,'numbersliding/hard.html')