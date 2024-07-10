
from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):
    return render(request, "plano/home.html")

def evento(request):
    return render(request, "plano/evento.html")

def fixture(request):
    return render(request, "plano/fixture.html")

def torneo(request):
    return render(request, "plano/torneo.html")