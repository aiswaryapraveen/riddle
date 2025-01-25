from django.shortcuts import render

# Create your views here.

def neasy(request):
    return render(request,'numbersliding/easy.html')