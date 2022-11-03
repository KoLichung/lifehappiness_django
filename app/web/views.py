from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request,'web/index.html')

def breadboard(request):
    return render(request,'web/breadboard.html')

def cuttingboard(request):
    return render(request,'web/cuttingboard.html')

def pizzaboard(request):
    return render(request,'web/pizzaboard.html')

def terms(request):
    return render(request,'web/terms.html')

def faq(request):
    return render(request,'web/faq.html')

