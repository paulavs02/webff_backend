from django.shortcuts import render
from .models import Escuadra
# Create your views here.
def fixture(request):
    escuadras = Escuadra.objects.all()
    return render(request, "fixture/fixture.html", {'escuadras': escuadras})
