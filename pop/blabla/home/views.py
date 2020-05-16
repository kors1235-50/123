from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'base.html')

def other(request):
    return render(request, 'others.html')

def other1(request):
    return render(request, 'others1.html')

def other2(request):
    return render(request, 'others2.html')
